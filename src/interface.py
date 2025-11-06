from src.dir_laptop.laptop import Laptop
import csv


class Interface:
    __fieldnames: dict = {
        0: "model",
        1: "proc_frequency",
        2: "number_of_cores",
        3: "amount_ram",
        4: "amount_external_memory",
        5: "amount_video_memory",
        6: "price",
    }
    __filename: str = "laptop"

    def __init__(self):
        self.storage = []

    def __repr__(self):
        return str(self.storage)

    @property
    def fieldnames(self):
        return self.__fieldnames

    @property
    def filename(self) -> str:
        return self.__filename

    def reading_file(self):
        result = []
        try:
            with open(f'{self.filename}.csv', mode="r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    laptop_data = {
                        'proc_frequency': int(row.get('proc_frequency', "None")),
                        'number_of_cores': int(row.get('number_of_cores', "None")),
                        'amount_ram': int(row.get('amount_ram', "None")),
                        'amount_external_memory': int(row.get('amount_external_memory', "None")),
                        'amount_video_memory': int(row.get('amount_video_memory', "None")),
                        'price': int(row.get('price', "None"))
                    }
                    laptop = Laptop(**laptop_data)
                    laptop._Laptop__model = int(row.get('model', "None"))
                    result.append(laptop)
        except FileNotFoundError:
            print("Файл не найден")
        return result

    def writing_file(self):
        with open(f'{self.filename}.csv', 'w', encoding="utf-8", newline='') as csvfile:
            fieldnames = list(self.fieldnames.values())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            for item in self.storage:
                writer.writerow(item.to_dict())

    def adding_one_entry(self):
        self.storage.append(Laptop())
        self.writing_file()

    def search_for_an_entry(self):
        item_id = int(input("Введите модель ноутбука: "))
        for item in self.storage:
            if item.model == item_id:
                print(item)
                return item

        else:
            print(f"Ноутбука модели {item_id} нет!")

    def editing_a_post(self):
        flag_break = False
        while True:
            item_id = int(input("Введите модель ноутбука: "))
            for item in self.storage:
                if item.model == item_id:
                    print(
                        "\n".join(f"{key}. {value}" for key, value in self.fieldnames.items() if key != 0),
                        sep="\n",
                    )
                    number_field = int(input("Укажите поле, которую хотите изменить: "))
                    field = self.fieldnames[number_field]
                    match number_field:
                        case 1:
                            new_value = int(input(f"Введите новое значение для поля {field}: "))
                            setattr(item, field, new_value)
                        case 2:
                            new_value = int(input(f"Введите новое значение для поля {field}: "))
                            setattr(item, field, new_value)
                        case 3:
                            new_value = int(input(f"Введите новое значение для поля {field}: "))
                            setattr(item, field, new_value)
                        case 4:
                            new_value = int(input(f"Введите новое значение для поля {field}: "))
                            setattr(item, field, new_value)
                        case 5:
                            new_value = int(input(f"Введите новое значение для поля {field}: "))
                            setattr(item, field, new_value)
                        case 6:
                            new_value = int(input(f"Введите новое значение для поля {field}: "))
                            setattr(item, field, new_value)

                    self.writing_file()
                    flag_break = True
                    break
            else:
                print(f"Ноутбука модели {item_id} нет!")

            if flag_break:
                break

    def deleting_an_entry(self):
        item_id = int(input("Введите модель ноутбука: "))
        for item in self.storage:
            if item.model == item_id:
                self.storage.remove(item)
                self.writing_file()
                break
        else:
            print(f"Ноутбука с id-{item_id} нет!")

    def print_information(self):
        size_format = []
        for field_name in self.__fieldnames.values():
            size = len(str(field_name)) + 1
            size_format.append(size)

            print(field_name.ljust(size), end="")

        print(end="\n")

        for item in self.storage:
            for value, size in zip(item.characteristics, size_format):
                print(str(value).ljust(size), end="")

            print()

    def start(self):
        while True:
            print(
                "1. Чтение данных из файла",
                "2. Запись данных в файл",
                "3. Поиск записи по модели ноутбука",
                "4. Измененение поля записи",
                "5. Удаление записи по модели ноутбука",
                "6. Добавление записи в список",
                "7. Показать содерживое списка",
                "8. Выйти из интерфейса",
                sep="\n",
            )

            choice: int = int(input("Выберите действие: "))
            match choice:
                case 1:
                    print(self.reading_file())
                case 2:
                    self.writing_file()
                case 3:
                    self.search_for_an_entry()
                case 4:
                    self.editing_a_post()
                case 5:
                    self.deleting_an_entry()
                case 6:
                    self.adding_one_entry()
                case 7:
                    self.print_information()
                case 8:
                    break
