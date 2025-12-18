class Interface:

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
