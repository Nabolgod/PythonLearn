from src.dir_laptop.laptopdes import LaptopDescriptor
from src.dir_base.item import ItemsShop


class Laptop(ItemsShop):
    __instance_count: int = 0

    # Свойства полей
    proc_frequency = LaptopDescriptor(1, 5)
    number_of_cores = LaptopDescriptor(1, 24, True)
    amount_ram = LaptopDescriptor(8, 64, True)
    amount_external_memory = LaptopDescriptor(1, 15)
    amount_video_memory = LaptopDescriptor(8, 32, True)
    price = LaptopDescriptor(999, 4500)

    def __init__(
            self,
            proc_frequency: int = None,
            number_of_cores: int = None,
            amount_ram: int = None,
            amount_external_memory: int = None,
            amount_video_memory: int = None,
            price: int = None,
    ):
        self.__model = self.__assign_model()
        self.proc_frequency = proc_frequency
        self.number_of_cores = number_of_cores
        self.amount_ram = amount_ram
        self.amount_external_memory = amount_external_memory
        self.amount_video_memory = amount_video_memory
        self.price = price

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"Laptop({attrs})"

    @classmethod
    def __assign_model(cls) -> int:
        """Метод для создания номера модели ноутбука"""
        cls.__instance_count += 1
        return cls.__instance_count

    @property
    def characteristics(self):
        return list(self.__dict__.values())

    @property
    def model(self):
        return self.__model

    def to_dict(self):
        return {
            'model': self.model,
            'proc_frequency': self.proc_frequency,
            'number_of_cores': self.number_of_cores,
            'amount_ram': self.amount_ram,
            'amount_external_memory': self.amount_external_memory,
            'amount_video_memory': self.amount_video_memory,
            'price': self.price
        }
