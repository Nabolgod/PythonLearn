from src.items.item import Item
from abc import ABC, abstractmethod
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

    def add(self, random: bool = False) -> Item:
        """Добавление объекта в cvs файл с пользовательскими или случайными данными"""
        next_id = self.get_next_id_generator()
        obj = self.instance.create_obj(next_id, random)

        # Проверяем, существует ли файл
        file_exists = self.file_path.exists() and self.file_path.stat().st_size > 0

        # Определяем режим открытия файла
        mode = 'a' if file_exists else 'w'

        with open(self.file_path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.instance.fieldnames)

            # Если файл новый или пустой, пишем заголовок
            if not file_exists:
                writer.writeheader()

            # Добавляем строку
            writer.writerow(obj.characteristics)

        print(f"Данные добавлены в {self.file_path}")
        return obj

    def search(self, id: int) -> Item:
        """Поиск объекта в cvs файлe по id"""
        pass

    def delete(self, id: int) -> bool:
        """Удаление объекта в cvs файлe по id"""
        pass

    def update(self, id: int) -> Item:
        """Изменение объекта в cvs файлe по id"""
        pass

    @abstractmethod
    def convert_to_object(self) -> Item:
        pass

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
