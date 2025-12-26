# laptop_circular_list.py
import csv

from src.laboratory_3.items.labtop.laptop import Laptop
from src.repositories.base import BaseRepository


class LaptopRepositoryCircularList(BaseRepository):
    filename = "laptops_circular.csv"

    def read(self, circular_list):
        """
        Загрузка данных из файла в кольцевой список.
        Каждая запись добавляется в начало.
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"Файл {self.filename} не найден")

        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                laptop = Laptop.convert_to_object(row)
                circular_list.add_to_beginning(laptop)

        return circular_list

    def write(self, circular_list):
        """
        Сохранение данных из списка в файл через обход.
        """
        if circular_list.is_empty():
            return 0

        with open(self.file_path, "w", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.instance.fieldnames)
            writer.writeheader()

            count = 0
            # Начинаем обход с головы
            current = circular_list.head

            for _ in range(circular_list.size):
                writer.writerow(current.data.characteristics)
                current = current.next
                count += 1

        return count
