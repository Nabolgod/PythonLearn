from abc import ABC, abstractmethod


class Item(ABC):
    fieldnames: list[str] = []

    def __init__(self, id_obj: int):
        self.__id = id_obj

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.characteristics.items())
        return f"Laptop({attrs})"

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

    @staticmethod
    @abstractmethod
    def create_obj(id_obj: int, random: bool = False):
        pass

    @staticmethod
    @abstractmethod
    def convert_to_object(characteristics: dict):
        pass
