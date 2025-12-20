from src.laboratory_3.items.item import Item
from abc import ABC, abstractmethod
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

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def add(self, random: bool = False):
        pass


