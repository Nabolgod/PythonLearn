from src.dir_laptop.laptop import Laptop, example
import csv


class Interface:
    __filename: str = "laptop"

    def __init__(self):
        self.storage = []

    def __repr__(self):
        return str(self.storage)

    @property
    def filename(self) -> str:
        return self.__filename

    def print_information(self, storage=None, size_add=2):
        storage = self.storage if storage is None else storage

        if storage:
            columns = example.characteristics.keys()

            for name_column in columns:
                print(name_column.ljust(example.size_formated.get(name_column) + size_add), end="")
            print()

            for labtop in storage:
                for col, info in labtop.characteristics.items():
                    print(str(info).ljust(example.size_formated.get(col) + size_add), end="")
                print()

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
                    laptop._Laptop__model = row.get("model", "None")
                    laptop._Laptop__id = int(row.get('id', "None"))
                    result.append(laptop)
        except FileNotFoundError:
            print("Файл не найден")
        self.storage = result
        return self.storage

    def writing_file(self):
        with open(f'{self.filename}.csv', 'w', encoding="utf-8", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=example.fieldnames, delimiter=';')
            writer.writeheader()
            for item in self.storage:
                writer.writerow(item.characteristics)

    def adding_one_entry_random(self):
        self.storage.append(Laptop())

    def adding_one_entry_hands(self):
        data_info = {}
        for column in example.fieldnames[2:]:
            value = int(input(f"Введите данныe для поля {column}="))
            data_info.setdefault(column, value)
        self.storage.append(Laptop(**data_info))

    def search_for_an_entry(self):
        item_id = int(input("Введите ID ноутбука: "))
        for item in self.storage:
            if item.id == item_id:
                print(item)
                return item
        else:
            print(f"Ноутбука модели {item_id} нет!")

    def deleting_an_entry(self):
        item_id = int(input("Введите ID ноутбука: "))
        for item in self.storage:
            if item.id == item_id:
                self.storage.remove(item)
                break
        else:
            print(f"Ноутбука с id-{item_id} нет!")

    def editing_a_post(self):
        flag_break = False
        while True:
            item_id = int(input("Введите ID ноутбука: "))
            for item in self.storage:
                if item.id == item_id:
                    print(
                        "\n".join(f"{key}. {value}" for key, value in enumerate(example.fieldnames[2:], start=1) if key != 0),
                        sep="\n",
                    )

                    number_field = int(input("Укажите поле, которую хотите изменить: "))
                    while not 1 <= number_field <= 6:
                        number_field = int(input("Укажите поле, которую хотите изменить: "))

                    field = example.fieldnames[number_field + 1]

                    new_value = int(input(f"Введите новое значение для поля {field}: "))
                    setattr(item, field, new_value)

                    flag_break = True
                    break
            else:
                print(f"Ноутбука ID {item_id} нет!")

            if flag_break:
                break

    def additional_functionality(self):
        while True:
            print(
                "1. Проверка наличия объекта в массиве по ID",
                "2. Сортировка по возрастанию по одному из полей",
                "3. Сортировка по убыванию по одному из полей",
                "4. Сравнение элементов по одному или нескольким полям",
                "5. Присвоить данные одного ноутбука другому",
                "6. Назад",
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
                    break

    def start(self):
        while True:
            print(
                "1. Чтение данных из файла",
                "2. Запись данных в файл",
                "3. Поиск записи по модели ноутбука",
                "4. Измененение поля записи",
                "5. Удаление записи по модели ноутбука",
                "6. Добавление записи в список со случайными данными",
                "7. Добавление записи в список с ручным вводом данных",
                "8. Показать содерживое списка",
                "9. Дополнительные действия",
                "10. Выйти из интерфейса",
                sep="\n",
            )

            choice: int = int(input("Выберите действие: "))
            match choice:
                case 1:
                    file_contents = self.reading_file()
                    self.print_information(file_contents)
                case 2:
                    self.writing_file()
                case 3:
                    self.search_for_an_entry()
                case 4:
                    self.editing_a_post()
                case 5:
                    self.deleting_an_entry()
                case 6:
                    self.adding_one_entry_random()
                case 7:
                    self.adding_one_entry_hands()
                case 8:
                    self.print_information()
                case 9:
                    self.additional_functionality()
                case 10:
                    break
