from src.laboratory_3.repositories.base import BaseRepository
from src.laboratory_3.items.labtop.laptop import Laptop


class LaptopRepository(BaseRepository):
    filename = "laptop.csv"
    instance = Laptop
