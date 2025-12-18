from src.repositories.base import BaseRepository
from src.items.labtop.laptop import Laptop


class LaptopRepository(BaseRepository):
    filename = "laptop"
    instance = Laptop
