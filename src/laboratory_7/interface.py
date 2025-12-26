from src.laboratory_3.items.labtop.laptop import Laptop
from src.laboratory_7.annular_list import CircularDoublyLinkedList
from src.repositories.laptop_annular_list import LaptopRepositoryCircularList


class InterfaceCircularList:
    def __init__(self):
        self.list = CircularDoublyLinkedList()
        self.repository = LaptopRepositoryCircularList()
        self.last_id = 0

    def _get_next_id(self):
        self.last_id += 1
        return self.last_id

    def menu(self):
        while True:
            print("\n" + "=" * 60)
            print("ДВУСВЯЗНЫЙ КОЛЬЦЕВОЙ СПИСОК НОУТБУКОВ")
            print("=" * 60)
            print("1.  Добавить в начало списка")
            print("2.  Загрузить из файла")
            print("3.  Обход списка (шагать)")
            print("4.  Показать текущий элемент (полная информация)")
            print("5.  Редактировать текущий элемент")
            print("6.  Поиск элемента")
            print("7.  Вставить после текущего")
            print("8.  Удалить из начала")
            print("9.  Сохранить в файл")
            print("10. Проверить пустоту")
            print("11. Показать структуру списка")
            print("12. Заполнить случайными данными")
            print("13. Очистить список")
            print("0.  Выход")
            print("=" * 60)

            choice = input("Выберите действие: ").strip()

            try:
                if choice == "1":
                    self.add_to_beginning()
                elif choice == "2":
                    self.load_from_file()
                elif choice == "3":
                    self.traverse()
                elif choice == "4":
                    self.show_current()
                elif choice == "5":
                    self.edit_current()
                elif choice == "6":
                    self.search()
                elif choice == "7":
                    self.insert_after_current()
                elif choice == "8":
                    self.delete_from_beginning()
                elif choice == "9":
                    self.save_to_file()
                elif choice == "10":
                    self.check_empty()
                elif choice == "11":
                    self.show_structure()
                elif choice == "12":
                    self.fill_random()
                elif choice == "13":
                    self.clear_list()
                elif choice == "0":
                    print("Выход из программы.")
                    break
                else:
                    print("Неверный выбор. Попробуйте снова.")

            except IndexError as e:
                print(f"⚠️ Ошибка: {e}")
            except Exception as e:
                print(f"❌ Неожиданная ошибка: {e}")

    # ========== ОСНОВНЫЕ ФУНКЦИИ ==========

    def add_to_beginning(self):
        """1. Добавить в начало списка"""
        print("\n" + "═" * 40)
        print("ДОБАВЛЕНИЕ В НАЧАЛО СПИСКА")
        print("═" * 40)

        mode = input("1. Вручную\n2. Случайные данные\nВыберите: ")

        laptop_id = self._get_next_id()

        if mode == "1":
            laptop = Laptop.create_obj(laptop_id, random=False)
        else:
            count = int(input("Сколько ноутбуков добавить? ") or "1")
            for _ in range(count):
                laptop = Laptop.create_obj(self._get_next_id(), random=True)
                self.list.add_to_beginning(laptop)
            print(f"✅ Добавлено {count} ноутбуков")
            return

        self.list.add_to_beginning(laptop)
        print(f"✅ Ноутбук ID={laptop_id} добавлен в начало")
        print(f"Размер списка: {self.list.size}")

    def load_from_file(self):
        """2. Загрузить из файла"""
        print("\n" + "═" * 40)
        print("ЗАГРУЗКА ИЗ ФАЙЛА")
        print("═" * 40)

        if not self.list.is_empty():
            confirm = input("Список не пустой. Очистить перед загрузкой? (y/n): ")
            if confirm.lower() == 'y':
                self.list = CircularDoublyLinkedList()

        try:
            old_size = self.list.size
            self.repository.read(self.list)
            loaded = self.list.size - old_size

            print(f"✅ Загружено {loaded} записей из файла")
            print(f"Общий размер списка: {self.list.size}")

            # Обновляем last_id
            if not self.list.is_empty():
                max_id = 0
                current = self.list.head
                for _ in range(self.list.size):
                    if current.data.id > max_id:
                        max_id = current.data.id
                    current = current.next
                self.last_id = max_id

        except FileNotFoundError:
            print("❌ Файл не найден. Сначала сохраните данные.")
        except Exception as e:
            print(f"❌ Ошибка загрузки: {e}")

    def traverse(self):
        """3. Обход списка (шагать)"""
        if self.list.is_empty():
            print("❌ Список пуст!")
            return

        print("\n" + "═" * 40)
        print("ОБХОД СПИСКА")
        print("═" * 40)
        print("n - следующий, p - предыдущий, q - выход")
        print("-" * 40)

        while True:
            try:
                current_data = self.list.get_current_data()
                print(f"\nТЕКУЩИЙ ЭЛЕМЕНТ:")
                print(f"  Адрес в памяти: {hex(id(self.list.current))}")
                print(f"  ID: {current_data.id}")
                print(f"  Модель: {current_data.model}")
                print(f"  Процессор: {current_data.proc_frequency} GHz")
                print(f"  Цена: ${current_data.price}")
                print(f"  (Элемент {self._get_current_position()}/{self.list.size})")

                command = input("\nДействие (n/p/q): ").lower()

                if command == 'n':
                    self.list.move_next()
                elif command == 'p':
                    self.list.move_prev()
                elif command == 'q':
                    break
                else:
                    print("? Неизвестная команда")

            except IndexError as e:
                print(f"⚠️ {e}")
                break

    def show_current(self):
        """4. Показать текущий элемент (полная информация)"""
        print("\n" + "═" * 60)
        print("ПОЛНАЯ ИНФОРМАЦИЯ О ТЕКУЩЕМ ЭЛЕМЕНТЕ")
        print("═" * 60)

        try:
            laptop = self.list.get_current_data()

            print("📋 ХАРАКТЕРИСТИКИ НОУТБУКА:")
            print("-" * 40)

            for key, value in laptop.characteristics.items():
                print(f"{key:25}: {value}")

            print(f"\n📍 ИНФОРМАЦИЯ О УЗЛЕ:")
            print(f"  Адрес узла: {hex(id(self.list.current))}")
            if self.list.current:
                print(f"  prev узел: {hex(id(self.list.current.prev)) if self.list.current.prev else 'None'}")
                print(f"  next узел: {hex(id(self.list.current.next)) if self.list.current.next else 'None'}")

            print(f"\n📊 СТАТИСТИКА СПИСКА:")
            print(f"  Всего элементов: {self.list.size}")
            print(f"  Позиция: {self._get_current_position()}/{self.list.size}")

        except IndexError:
            print("❌ Нет текущего элемента. Список пуст или не выбран элемент.")

    def edit_current(self):
        """5. Редактировать текущий элемент"""
        if self.list.is_empty():
            print("❌ Список пуст!")
            return

        print("\n" + "═" * 40)
        print("РЕДАКТИРОВАНИЕ ТЕКУЩЕГО ЭЛЕМЕНТА")
        print("═" * 40)

        try:
            current_laptop = self.list.get_current_data()

            print(f"Редактируем ноутбук ID={current_laptop.id}")
            print("Оставьте поле пустым, чтобы сохранить текущее значение")
            print("-" * 40)

            new_data = {}
            for field in Laptop.fieldnames:
                if field in ("id", "model"):
                    continue

                current_value = getattr(current_laptop, field, "")
                new_value = input(f"{field} [{current_value}]: ").strip()

                if new_value:
                    if field in ['proc_frequency', 'amount_external_memory']:
                        # Проверка на целое число
                        if not new_value.isdigit():
                            print(f"⚠️ {field} должно быть числом. Используется текущее значение.")
                            new_value = current_value
                    new_data[field] = new_value
                else:
                    new_data[field] = current_value

            # Создаем новый объект с обновленными данными
            updated_laptop = Laptop(
                id_obj=current_laptop.id,
                proc_frequency=int(new_data['proc_frequency']),
                number_of_cores=int(new_data['number_of_cores']),
                amount_ram=int(new_data['amount_ram']),
                amount_external_memory=int(new_data['amount_external_memory']),
                amount_video_memory=int(new_data['amount_video_memory']),
                price=int(new_data['price'])
            )
            updated_laptop.model = current_laptop.model

            self.list.set_current_data(updated_laptop)
            print("✅ Элемент обновлен!")

        except ValueError as e:
            print(f"❌ Ошибка ввода данных: {e}")
        except Exception as e:
            print(f"❌ Ошибка: {e}")

    def search(self):
        """6. Поиск элемента"""
        if self.list.is_empty():
            print("❌ Список пуст!")
            return

        print("\n" + "═" * 40)
        print("ПОИСК ЭЛЕМЕНТА")
        print("═" * 40)
        print("1. Поиск по ID")
        print("2. Поиск по модели")
        print("3. Поиск по диапазону цены")
        print("4. Расширенный поиск")

        choice = input("Выберите тип поиска: ")

        try:
            if choice == "1":
                search_id = int(input("Введите ID для поиска: "))
                result = self.list.find_by_field("id", search_id)

            elif choice == "2":
                model = input("Введите модель для поиска (например, LABTOP_): ")
                result = self.list.find_by_field("model", model)

            elif choice == "3":
                min_price = int(input("Минимальная цена: "))
                max_price = int(input("Максимальная цена: "))

                found = []
                current = self.list.head
                for _ in range(self.list.size):
                    if min_price <= current.data.price <= max_price:
                        found.append(current)
                    current = current.next

                if found:
                    print(f"✅ Найдено {len(found)} элементов:")
                    for node in found:
                        print(f"  ID: {node.data.id}, Модель: {node.data.model}, Цена: ${node.data.price}")

                    # Устанавливаем первый найденный как текущий
                    self.list.current = found[0]
                    result = found[0]
                else:
                    result = None

            elif choice == "4":
                print("\nВведите значения для поиска (оставьте пустым, чтобы игнорировать):")
                criteria = {}

                for field in Laptop.fieldnames:
                    if field == "id":
                        continue
                    value = input(f"{field}: ").strip()
                    if value:
                        criteria[field] = value

                if criteria:
                    result = self.list.find_by_characteristics(criteria)
                else:
                    print("❌ Не указаны критерии поиска")
                    return
            else:
                print("❌ Неверный выбор")
                return

            if result:
                print(f"✅ Элемент найден! ID={result.data.id}")
                self.show_current()
            else:
                print("❌ Элемент не найден")

        except ValueError:
            print("❌ Неверный формат данных")
        except Exception as e:
            print(f"❌ Ошибка поиска: {e}")

    def insert_after_current(self):
        """7. Вставить после текущего"""
        if self.list.is_empty():
            print("❌ Список пуст! Добавляем в начало.")
            self.add_to_beginning()
            return

        print("\n" + "═" * 40)
        print("ВСТАВКА ПОСЛЕ ТЕКУЩЕГО")
        print("═" * 40)

        laptop_id = self._get_next_id()

        mode = input("1. Вручную\n2. Случайные данные\nВыберите: ")

        if mode == "1":
            laptop = Laptop.create_obj(laptop_id, random=False)
        else:
            laptop = Laptop.create_obj(laptop_id, random=True)

        self.list.insert_after_current(laptop)
        print(f"✅ Ноутбук ID={laptop_id} вставлен после текущего")
        print(f"Размер списка: {self.list.size}")

    def delete_from_beginning(self):
        """8. Удалить из начала"""
        print("\n" + "═" * 40)
        print("УДАЛЕНИЕ ИЗ НАЧАЛА")
        print("═" * 40)

        if self.list.is_empty():
            print("❌ Список пуст!")
            return

        try:
            deleted = self.list.delete_from_beginning()
            print(f"✅ Удален элемент из начала:")
            print(f"  ID: {deleted.id}")
            print(f"  Модель: {deleted.model}")
            print(f"  Цена: ${deleted.price}")
            print(f"Новый размер списка: {self.list.size}")

        except IndexError as e:
            print(f"❌ {e}")

    def save_to_file(self):
        """9. Сохранить в файл"""
        print("\n" + "═" * 40)
        print("СОХРАНЕНИЕ В ФАЙЛ")
        print("═" * 40)

        if self.list.is_empty():
            print("❌ Список пуст! Нечего сохранять.")
            return

        try:
            saved_count = self.repository.write(self.list)
            print(f"✅ Сохранено {saved_count} записей в файл '{self.repository.filename}'")

        except Exception as e:
            print(f"❌ Ошибка сохранения: {e}")

    def check_empty(self):
        """10. Проверить пустоту"""
        print("\n" + "═" * 40)
        print("ПРОВЕРКА ПУСТОТЫ")
        print("═" * 40)

        if self.list.is_empty():
            print("✅ Список ПУСТ")
        else:
            print(f"✅ Список НЕ ПУСТ")
            print(f"Количество элементов: {self.list.size}")

    def show_structure(self):
        """11. Показать структуру списка"""
        self.list.display_structure()

    def fill_random(self):
        """12. Заполнить случайными данными"""
        print("\n" + "═" * 40)
        print("ЗАПОЛНЕНИЕ СЛУЧАЙНЫМИ ДАННЫМИ")
        print("═" * 40)

        count = int(input("Сколько ноутбуков добавить? ") or "5")

        for i in range(count):
            laptop_id = self._get_next_id()
            laptop = Laptop.create_obj(laptop_id, random=True)
            self.list.add_to_beginning(laptop)

        print(f"✅ Добавлено {count} случайных ноутбуков")
        print(f"Размер списка: {self.list.size}")

    def clear_list(self):
        """13. Очистить список"""
        print("\n" + "═" * 40)
        print("ОЧИСТКА СПИСКА")
        print("═" * 40)

        if self.list.is_empty():
            print("✅ Список уже пуст")
            return

        confirm = input(f"Очистить список ({self.list.size} элементов)? (y/n): ")

        if confirm.lower() == 'y':
            self.list = CircularDoublyLinkedList()
            print("✅ Список очищен")
        else:
            print("❌ Отменено")

    def _get_current_position(self):
        """Получить позицию текущего элемента"""
        if self.list.is_empty() or self.list.current is None:
            return 0

        pos = 1
        current = self.list.head

        while current != self.list.current:
            current = current.next
            pos += 1
            if current == self.list.head:  # Защита от бесконечного цикла
                break

        return pos


# Демонстрационный скрипт
def demonstrate_circular_list():
    """Демонстрация работы кольцевого списка"""
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ КОЛЬЦЕВОГО ДВУСВЯЗНОГО СПИСКА")
    print("=" * 60)

    clist = CircularDoublyLinkedList()

    # 1. Добавление элементов
    print("\n1. Добавление 3 элементов в начало:")
    for i in range(1, 4):
        laptop = Laptop.create_obj(i, random=True)
        clist.add_to_beginning(laptop)
        print(f"   Добавлен ID={i}, размер={clist.size}")

    # 2. Обход
    print("\n2. Обход вперед (3 шага):")
    for i in range(3):
        current = clist.get_current_data()
        print(f"   Шаг {i + 1}: ID={current.id}, модель={current.model}")
        clist.move_next()

    # 3. Обход назад
    print("\n3. Обход назад (2 шага):")
    for i in range(2):
        current = clist.get_current_data()
        print(f"   Шаг {i + 1}: ID={current.id}")
        clist.move_prev()

    # 4. Вставка после текущего
    print("\n4. Вставка нового элемента после текущего:")
    new_laptop = Laptop.create_obj(99, random=True)
    clist.insert_after_current(new_laptop)
    print(f"   Добавлен ID=99, новый размер={clist.size}")

    # 5. Удаление из начала
    print("\n5. Удаление из начала:")
    deleted = clist.delete_from_beginning()
    print(f"   Удален ID={deleted.id}, новый размер={clist.size}")

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    # Для запуска демо
    # demonstrate_circular_list()

    # Для запуска интерфейса
    interface = InterfaceCircularList()
    interface.menu()
