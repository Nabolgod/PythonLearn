from src.items.labtop.laptopdes import LaptopDescriptor
from src.items.item import Item


class Laptop(Item):
    fieldnames = [
        "id",
        "model",
        "proc_frequency",
        "number_of_cores",
        "amount_ram",
        "amount_external_memory",
        "amount_video_memory",
        "price",
    ]

    # Свойства полей
    proc_frequency = LaptopDescriptor(1, 5)
    number_of_cores = LaptopDescriptor(1, 24, True)
    amount_ram = LaptopDescriptor(8, 64, True)
    amount_external_memory = LaptopDescriptor(1, 15)
    amount_video_memory = LaptopDescriptor(8, 32, True)
    price = LaptopDescriptor(999, 4500)

    def __init__(
            self,
            id_obj: int,
            proc_frequency: int = None,
            number_of_cores: int = None,
            amount_ram: int = None,
            amount_external_memory: int = None,
            amount_video_memory: int = None,
            price: int = None,
    ):
        super().__init__(id_obj)
        self.__model = f"LABTOP_{self.id}"
        self.proc_frequency = proc_frequency
        self.number_of_cores = number_of_cores
        self.amount_ram = amount_ram
        self.amount_external_memory = amount_external_memory
        self.amount_video_memory = amount_video_memory
        self.price = price

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"Laptop({attrs})"

    @property
    def records(self):
        return (
            self.id,
            self.model,
            self.proc_frequency,
            self.number_of_cores,
            self.amount_ram,
            self.amount_external_memory,
            self.amount_video_memory,
            self.price,
        )

    @property
    def model(self):
        return self.__model

    @staticmethod
    def create_obj(id_obj: int, random: bool = False):
        if random:
            return Laptop(id_obj)

        characteristics = {}
        for field in Laptop.fieldnames:
            if field in ("id", "model"):
                continue
            value = input(f"Введите значние для {field}: ")
            characteristics[field] = value

        obj = Laptop(id_obj, **characteristics)
        return obj

