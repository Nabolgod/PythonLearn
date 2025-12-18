from src.items.item import Item
from abc import ABC
import csv
from pathlib import Path


class BaseRepository(ABC):
    filename: str | None = None
    instance: Item | None = None

    def __init__(self):
        self.file_path = Path(self.filename)

    def read(self) -> list:
        """Чтение данных из cvs файла в список объектов"""
        result = []
        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if isinstance(row, dict):
                    laptop = self.instance.convert_to_object(row)
                result.append(laptop)

        return result

    def write(self, data: list):
        """Запись данных в csv файл из список объектов"""

        with open(self.file_path, "w", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.instance.fieldnames)
            writer.writeheader()

            for item in data:
                writer.writerow(item.characteristics)

    def add(self, random: bool = False) -> Item:
        """Добавление объекта в cvs файл с пользовательскими или случайными данными"""
        next_id = self.get_next_id_generator()
        obj = self.instance.create_obj(next_id, random)

        file_exists = self.file_path.exists() and self.file_path.stat().st_size > 0

        with open(self.file_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.instance.fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(obj.characteristics)

        return obj

    def search(self, id_obj: int) -> Item | None:
        """Поиск объекта в csv файле по id"""
        for obj in self.read():
            if obj.id == id_obj:
                return obj
        return None

    def delete(self, id: int) -> bool:
        """Удаление объекта в cvs файлe по id"""
        # Читаем все объекты
        items = self.read()  # Предполагается, что у вас есть метод read()

        # Фильтруем
        filtered_items = [item for item in items if item.id != id]

        # Если ничего не удалили
        if len(filtered_items) == len(items):
            return False

        # Записываем обратно
        self.write(filtered_items)
        return True

    def update(self, id_obj: int, key: str, value) -> Item | bool:
        """Обновление объекта по id"""

        items = self.read()

        obj_to_update = None
        for i, item in enumerate(items):
            if item.id == id_obj:
                obj_to_update = item

                setattr(obj_to_update, key, value)

                items[i] = obj_to_update
                break

        if obj_to_update is None:
            return False

        self.write(items)
        return obj_to_update

    def info(self):
        """Простой табличный вывод"""
        objects = self.read()
        if not objects:
            print("Нет данных для отображения")
            return

        headers = list(objects[0].characteristics.keys())

        # Вычисляем ширину колонок
        col_widths = []
        for i, header in enumerate(headers):
            max_width = len(header)
            for obj in objects:
                value_len = len(str(obj.characteristics.get(header, '')))
                max_width = max(max_width, value_len)
            col_widths.append(max_width + 2)  # +2 для отступов

        # Выводим заголовок
        header_line = ""
        for i, header in enumerate(headers):
            header_line += f" {header:<{col_widths[i]}}"
        print(header_line)
        print("-" * (sum(col_widths) + len(headers)))

        # Выводим данные
        for obj in objects:
            row_line = ""
            for i, header in enumerate(headers):
                value = str(obj.characteristics.get(header, ''))
                row_line += f" {value:<{col_widths[i]}}"
            print(row_line)

    def get_next_id_generator(self):
        """
        Версия с использованием генератора для обработки больших файлов.
        Не загружает весь файл в память.
        """

        if not self.file_path.exists() or self.file_path.stat().st_size == 0:
            return 1

        with open(self.file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            if not reader.fieldnames:
                return 1

            # Определяем колонку с ID
            actual_id_column = None
            for field in reader.fieldnames:
                if field.lower() == "id":
                    actual_id_column = field
                    break

            if not actual_id_column:
                actual_id_column = reader.fieldnames[0]

            # Используем генератор для чтения файла
            max_id = 0
            for row in reader:
                if row.get(actual_id_column):
                    try:
                        current_id = int(row[actual_id_column])
                        # Поскольку ID отсортированы, последний будет максимальным
                        # Но для надежности все равно проверяем
                        if current_id > max_id:
                            max_id = current_id
                    except ValueError:
                        continue

            return max_id + 1 if max_id > 0 else 1
