from src.laboratory_6.stack import Stack, Node
from src.repositories.base import BaseRepository
import csv
from src.laboratory_3.items.labtop.laptop import Laptop


class LaptopRepositoryStack(BaseRepository):
    filename = "laptop_stack.csv"
    instance = Laptop

    def __init__(self):
        super().__init__()
        self.stack = Stack()

    def read(self):
        """
        Прочитать данные из тектстового файла в стек. Записи добавляются по одной c
        использованием метода push().
        """
        self.stack = Stack()

        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Просто читаем и добавляем в стек
            for row in reader:
                laptop = self.instance.convert_to_object(row)
                self.stack.push(laptop)

        return self.stack

    def write(self, stack_storage):
        """
        Записать данные в текстовый файл из стека, с использованием метода top(),
        тем самым освобождая стек.
        """
        with open(self.file_path, "w", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.instance.fieldnames)
            writer.writeheader()

            # Просто извлекаем и записываем, пока стек не опустеет
            while not stack_storage.is_empty():
                laptop = stack_storage.pop()
                writer.writerow(laptop.characteristics)
