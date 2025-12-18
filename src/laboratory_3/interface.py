class Interface:
    def __init__(self, repository):
        self.repository = repository

    def additional_functionality(self):
        """Дополнительные функции"""
        options = {
            "1": "Проверка наличия объекта в массиве по ID",
            "2": "Сортировка по возрастанию по одному из полей",
            "3": "Сортировка по убыванию по одному из полей",
            "4": "Сравнение объектов",
            "5": "Присвоить данные одного ноутбука другому",
            "6": "Назад"
        }

        while True:
            print("\n".join(f"{key}. {value}" for key, value in options.items()))

            try:
                choice = input("Выберите действие: ").strip()

                if choice == "1":
                    id_obj = self.choice_id()
                    exists = self.repository.search(id_obj) is not None
                    print(f"Объект с ID {id_obj} {'найден' if exists else 'не найден'}")

                elif choice == "2":
                    field = self.choice_field()
                    sorted_items = self.repository.get_sorted_items(field, reverse=False)
                    self.repository.info(sorted_items)

                elif choice == "3":
                    field = self.choice_field()
                    sorted_items = self.repository.get_sorted_items(field, reverse=True)
                    self.repository.info(sorted_items)

                elif choice == "4":
                    self.compare_items()

                elif choice == "5":
                    self.assign_item_data()

                elif choice == "6":
                    break

                else:
                    print("Неверный выбор. Попробуйте снова.")

            except ValueError:
                print("Ошибка ввода. Введите число.")
            except Exception as e:
                print(f"Ошибка: {e}")

    def compare_items(self):
        """Сравнение двух элементов"""
        print("Сравнение двух ноутбуков:")
        id1 = self.choice_id()
        id2 = self.choice_id()

        item1 = self.repository.search(id1)
        item2 = self.repository.search(id2)

        if not item1 or not item2:
            print("Один или оба ноутбука не найдены")
            return

        print("\nСравнение:")
        print("-" * 40)

        # Сравниваем по всем полям кроме id
        fields = self.repository.instance.fieldnames[2:]  # Пропускаем id и model

        for field in fields:
            val1 = getattr(item1, field, None)
            val2 = getattr(item2, field, None)

            if val1 == val2:
                print(f"{field}: одинаковые ({val1})")
            else:
                print(f"{field}: {val1} vs {val2} ({'>' if val1 > val2 else '<'})")

    def assign_item_data(self):
        """Копирование данных одного ноутбука в другой"""
        print("Копирование данных ноутбука:")
        src_id = self.choice_id("Выберите ID ноутбука-источника: ")
        dst_id = self.choice_id("Выберите ID ноутбука-приёмника: ")

        # Нельзя копировать в самого себя
        if src_id == dst_id:
            print("Нельзя копировать данные в самого себя!")
            return

        src_item = self.repository.search(src_id)
        dst_item = self.repository.search(dst_id)

        if not src_item or not dst_item:
            print("Один или оба ноутбука не найдены")
            return

        # Подтверждение
        print(f"\nВы копируете данные из ноутбука {src_id} в ноутбук {dst_id}")
        confirm = input("Вы уверены? (да/нет): ").lower()
        if confirm not in ['да', 'д', 'yes', 'y']:
            print("Операция отменена")
            return

        # Копируем все поля кроме id и model
        fields = self.repository.instance.fieldnames[2:]  # Пропускаем id и model

        # Способ 1: Обновляем через update для каждого поля (простой)
        updated_fields = []
        for field in fields:
            src_value = getattr(src_item, field, None)
            dst_value = getattr(dst_item, field, None)

            if src_value != dst_value:  # Обновляем только если значения разные
                # Обновляем объект в памяти
                setattr(dst_item, field, src_value)
                # Обновляем в репозитории
                self.repository.update(dst_id, field, src_value)
                updated_fields.append(field)

        if updated_fields:
            print(f"Скопированы поля: {', '.join(updated_fields)}")
            print(f"Данные ноутбука {src_id} успешно скопированы в ноутбук {dst_id}")
        else:
            print("Все поля уже идентичны, копирование не требуется")

    def choice_id(self, prompt: str = None) -> int:
        """Выбор ID с валидацией"""
        if prompt is None:
            prompt = "Выберите ID ноутбука: "

        valid_ids = self.repository.get_all_ids()

        while True:
            try:
                id_obj = int(input(prompt))
                if id_obj in valid_ids:
                    return id_obj
                print(f"ID {id_obj} не существует. Доступные ID: {valid_ids}")
            except ValueError:
                print("Пожалуйста, введите целое число.")

    def choice_field(self) -> str:
        """Выбор поля для работы"""
        fieldnames = self.repository.instance.fieldnames[2:]

        print("\nДоступные поля:")
        for ind, attr in enumerate(fieldnames, start=1):
            print(f"{ind}. {attr}")

        while True:
            try:
                choice = int(input("Выберите поле: "))
                if 1 <= choice <= len(fieldnames):
                    return fieldnames[choice - 1]
                print(f"Введите число от 1 до {len(fieldnames)}")
            except ValueError:
                print("Пожалуйста, введите число.")

    def _check_data_exists(self) -> bool:
        """Проверка наличия данных в репозитории"""
        if not self.repository.is_empty():
            print("В файле нет данных")
            return False
        return True

    def start(self):
        """Главный цикл интерфейса"""
        options = {
            "1": "Чтение данных из файла",
            "2": "Поиск записи по ID ноутбука",
            "3": "Изменение поля записи по ID ноутбука",
            "4": "Удаление записи по ID ноутбука",
            "5": "Добавление записи со случайными данными",
            "6": "Добавление записи с ручным вводом данных",
            "7": "Показать содержимое списка",
            "8": "Дополнительные действия",
            "9": "Выйти из интерфейса"
        }

        while True:
            print("\n" + "=" * 40)
            print("ГЛАВНОЕ МЕНЮ")
            print("=" * 40)
            print("\n".join(f"{key}. {value}" for key, value in options.items()))
            print("=" * 40)

            try:
                choice = input("Выберите действие: ").strip()

                if choice == "1":
                    if self._check_data_exists():
                        items = self.repository.read()
                        print(f"\nНайдено {len(items)} записей:")
                        for item in items:
                            print(f"  {item}")

                elif choice == "2":
                    if self._check_data_exists():
                        id_obj = self.choice_id()
                        obj = self.repository.search(id_obj)
                        if obj:
                            print(f"\nНайден ноутбук:\n{obj}")
                        else:
                            print("Ноутбук не найден")

                elif choice == "3":
                    if self._check_data_exists():
                        id_obj = self.choice_id()
                        field = self.choice_field()

                        while True:
                            try:
                                new_value = int(input(f"Введите новое значение для поля {field}: "))
                                break
                            except ValueError:
                                print("Введите целое число")

                        result = self.repository.update(id_obj, field, new_value)
                        if result:
                            print(f"Поле '{field}' обновлено на значение {new_value}")
                        else:
                            print("Ошибка обновления")

                elif choice == "4":
                    if self._check_data_exists():
                        id_obj = self.choice_id()
                        if self.repository.delete(id_obj):
                            print(f"Запись с ID {id_obj} удалена")
                        else:
                            print("Запись не найдена")

                elif choice == "5":
                    obj = self.repository.add(True)
                    print(f"Добавлен ноутбук со случайными данными:\n{obj}")

                elif choice == "6":
                    obj = self.repository.add(False)
                    print(f"Добавлен ноутбук:\n{obj}")

                elif choice == "7":
                    if self._check_data_exists():
                        items = self.repository.read()
                        self.repository.info(items)

                elif choice == "8":
                    self.additional_functionality()

                elif choice == "9":
                    print("Выход из программы...")
                    break

                else:
                    print("Неверный выбор. Попробуйте снова.")

            except ValueError:
                print("Ошибка ввода. Введите число от 1 до 9.")
            except KeyboardInterrupt:
                print("\n\nПрограмма прервана пользователем")
                break
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
