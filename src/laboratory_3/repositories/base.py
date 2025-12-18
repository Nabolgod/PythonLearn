from src.laboratory_3.items.item import Item
from abc import ABC
import csv
from pathlib import Path


class BaseRepository(ABC):
    filename: str | None = None
    instance: Item | None = None

    def __init__(self):
        if self.filename is None:
            raise ValueError("filename должен быть задан в дочернем классе")
        self.file_path = Path(self.filename)

        # Создаем файл если его нет
        if not self.file_path.exists():
            self._create_empty_file()

    def _create_empty_file(self):
        """Создает пустой файл с заголовком"""
        with open(self.file_path, "w", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.instance.fieldnames)
            writer.writeheader()


    def is_empty(self) -> bool:
        """Проверка на пустоту файла (без загрузки всех объектов)"""
        return bool(self.read())

    def read(self) -> list:  # Убрать параметр force_refresh
        """Чтение данных из csv файла в список объектов"""
        result = []
        if not self.file_path.exists():
            return result

        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row:
                    obj = self.instance.convert_to_object(row)
                    result.append(obj)

        return result

    def write(self, data: list):
        """Запись данных в csv файл из список объектов"""
        with open(self.file_path, "w", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.instance.fieldnames)
            writer.writeheader()

            for item in data:
                writer.writerow(item.characteristics)

    def add(self, random: bool = False) -> Item:
        """Добавление объекта в csv файл с пользовательскими или случайными данными"""
        next_id = self.get_next_id_generator()
        obj = self.instance.create_obj(next_id, random)

        file_exists = self.file_path.exists() and self.file_path.stat().st_size > 0

        with open(self.file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.instance.fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(obj.characteristics)

        return obj

    def search(self, id_obj: int) -> Item | None:
        """Поиск объекта в csv файле по id (оптимизированный)"""
        # Используем кэшированные данные
        for obj in self.read():
            if obj.id == id_obj:
                return obj
        return None

    def delete(self, id: int) -> bool:
        """Удаление объекта в csv файле по id"""
        items = self.read()

        # Используем фильтрацию без лишних итераций
        original_count = len(items)
        filtered_items = []
        found = False

        for item in items:
            if item.id == id:
                found = True
            else:
                filtered_items.append(item)

        if not found:
            return False

        self.write(filtered_items)
        return True

    def update(self, id_obj: int, key: str, value) -> Item | bool:
        """Обновление объекта по id"""
        items = self.read()

        for i, item in enumerate(items):
            if item.id == id_obj:
                setattr(item, key, value)
                self.write(items)
                return item

        return False

    @staticmethod
    def info(objects: list):
        """Простой табличный вывод"""
        if not objects:
            print("Нет данных для отображения")
            return

        headers = list(objects[0].characteristics.keys())

        # Вычисляем ширину колонок за один проход
        col_widths = [len(header) for header in headers]

        for obj in objects:
            char = obj.characteristics
            for i, header in enumerate(headers):
                value_len = len(str(char.get(header, '')))
                if value_len > col_widths[i]:
                    col_widths[i] = value_len

        # Добавляем отступы
        col_widths = [width + 2 for width in col_widths]

        # Выводим заголовок
        print("".join(f" {header:<{col_widths[i]}}" for i, header in enumerate(headers)))
        print("-" * (sum(col_widths) + len(headers)))

        # Выводим данные
        for obj in objects:
            char = obj.characteristics
            print("".join(f" {str(char.get(header, '')):<{col_widths[i]}}"
                          for i, header in enumerate(headers)))

    def get_sorted_items(self, field: str, reverse: bool = False) -> list:
        """Получение отсортированного списка"""
        items = self.read()

        # Проверяем существование поля
        if items and not hasattr(items[0], field):
            raise AttributeError(f"Поле '{field}' не существует")

        return sorted(items, key=lambda item: getattr(item, field), reverse=reverse)

    def get_next_id_generator(self) -> int:
        """Получение следующего ID (оптимизированная версия)"""
        items = self.read()

        if not items:
            return 1

        # Используем генераторное выражение для экономии памяти
        max_id = 0
        for item in items:
            if hasattr(item, 'id') and item.id is not None:
                try:
                    item_id = int(item.id)
                    if item_id > max_id:
                        max_id = item_id
                except (ValueError, TypeError):
                    continue

        return max_id + 1 if max_id > 0 else 1

    def get_all_ids(self) -> list[int]:
        """Получение списка всех ID (оптимизировано)"""
        return [item.id for item in self.read() if hasattr(item, 'id') and item.id is not None]
