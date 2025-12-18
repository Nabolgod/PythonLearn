from abc import ABC, abstractmethod


class Item(ABC):
    fieldnames: list[str] = []

    def __init__(self, id_obj: int):
        self.__id = id_obj

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.characteristics)
        return f"Laptop({attrs})"

    def __str__(self) -> str:
        record = ""
        for key, size in self.size_formatted.items():
            record += str(self.characteristics[key]).ljust(size)
        return record

    @property
    def characteristics(self) -> dict:
        return {key: value for key, value in zip(self.fieldnames, self.records)}

    @property
    def id(self):
        return self.__id

    @property
    @abstractmethod
    def records(self):
        pass

    @property
    def size_formatted(self):
        return {key: max(len(key), len(str(value))) for key, value in self.characteristics.items()}

    @staticmethod
    @abstractmethod
    def create_obj(id_obj: int, random: bool = False):
        pass
