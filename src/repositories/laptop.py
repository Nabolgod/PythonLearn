from src.repositories.base import BaseRepository
from src.items.labtop.laptop import Laptop


class LaptopRepository(BaseRepository):
    filename = "laptop"
    instance = Laptop

    def convert_to_object(self, characteristics: dict) -> Laptop:
        laptop_data = {
            'proc_frequency': int(characteristics.get('proc_frequency', "None")),
            'number_of_cores': int(characteristics.get('number_of_cores', "None")),
            'amount_ram': int(characteristics.get('amount_ram', "None")),
            'amount_external_memory': int(characteristics.get('amount_external_memory', "None")),
            'amount_video_memory': int(characteristics.get('amount_video_memory', "None")),
            'price': int(characteristics.get('price', "None"))
        }
        laptop = self.instance(**laptop_data)
        laptop._Laptop__model = characteristics.get("model", "None")
        laptop._Laptop__id = int(characteristics.get('id', "None"))

        return laptop



