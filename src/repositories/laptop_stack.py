from src.laboratory_3.items.labtop.laptop import Laptop
from src.repositories.base import BaseRepository


class LaptopRepositoryStack(BaseRepository):
    filename = "laptop.csv"
    instance = Laptop

    def read(self):
        pass

    def write(self, data):
        pass

    def add(self, random: bool = False):
        pass
