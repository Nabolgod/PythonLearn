class Interface:
    def __init__(self, repository):
        self.repository = repository

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

    def choice_id(self):
        id_obj = int(input("Выберите ID ноутбука: "))

        while id_obj not in map(lambda obj: obj.id, self.repository.read()):
            id_obj = int(input("Такого ID не существует, попробуйте ещё раз: "))
        return id_obj

    def start(self):
        while True:
            print(
                "1. Чтение данных из файла",
                "2. Поиск записи по ID ноутбука",
                "3. Измененение поля записи по ID ноутбука",
                "4. Удаление записи по ID ноутбука",
                "5. Добавление записи в список со случайными данными",
                "6. Добавление записи в список с ручным вводом данных",
                "7. Показать содерживое списка",
                "8. Дополнительные действия",
                "9. Выйти из интерфейса",
                sep="\n",
            )

            choice: int = int(input("Выберите действие: "))
            match choice:
                case 1:
                    print(*self.repository.read(), sep="\n")
                case 2:
                    obj = self.repository.search(self.choice_id())
                    if obj:
                        print(obj)
                    else:
                        print("Такого ноутбука нет")
                case 3:
                    fieldnames = self.repository.instance.fieldnames[2:]
                    id_obj = self.choice_id()

                    for ind, attr in enumerate(fieldnames, start=1):
                        print(f"{ind}. {attr}")
                    choice_update = int(input("Выберите значение для изменения: "))
                    while not 1 <= choice_update <= 6:
                        choice_update = int(input("Выберите значение для изменения: "))

                    field = fieldnames[choice_update - 1]
                    new_value = int(input(f"Введите новое значение для поля {field}: "))
                    self.repository.update(id_obj, field, new_value)
                case 4:
                    self.repository.delete(self.choice_id())
                case 5:
                    self.repository.add(True)
                case 6:
                    self.repository.add()
                case 7:
                    self.repository.info()
                case 8:
                    self.additional_functionality()
                    pass
                case 9:
                    break
