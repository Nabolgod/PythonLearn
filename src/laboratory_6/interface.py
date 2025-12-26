from src.laboratory_3.items.labtop.laptop import Laptop
from src.laboratory_6.stack import Stack
from src.repositories.laptop_stack import LaptopRepositoryStack


class InterfaceStack:
    def __init__(self, stack_storage: Stack = None):
        self.stack_storage = stack_storage if stack_storage else Stack()
        self.repository = LaptopRepositoryStack()
        self.last_id = 0

    def _get_next_id(self):
        self.last_id += 1
        return self.last_id

    def menu(self):
        while True:
            print("\n" + "=" * 40)
            print("СТЕК НОУТБУКОВ")
            print("=" * 40)
            print("1. push() - добавить элемент")
            print("2. push_random() - добавить случайный")
            print("3. read() - загрузить из файла в стек")
            print("4. peek() - посмотреть верхний элемент")
            print("5. pop() - взять верхний элемент")
            print("6. write() - сохранить стек в файл (pop)")
            print("7. is_empty() - проверить пустоту")
            print("8. size() - размер стека")
            print("9. clear() - очистить стек")
            print("10. info() - посмотреть содержимое стека")
            print("11. Выход")
            print("=" * 40)

            choice = input("Выберите операцию: ")

            if choice == "1":
                self.push_operation()
            elif choice == "2":
                self.push_random_operation()
            elif choice == "3":
                self.read_operation()
            elif choice == "4":
                self.peek_operation()
            elif choice == "5":
                self.pop_operation()
            elif choice == "6":
                self.write_operation()
            elif choice == "7":
                self.is_empty_operation()
            elif choice == "8":
                self.size_operation()
            elif choice == "9":
                self.clear_operation()
            elif choice == "10":
                self.info()
            elif choice == "11":
                break

    def info(self):
        print(self.stack_storage)

    def push_operation(self):
        """push() - добавить элемент в стек"""
        laptop_id = self._get_next_id()
        laptop = Laptop.create_obj(laptop_id, random=False)
        self.stack_storage.push(laptop)
        print(f"✅ push(): добавлен ноутбук ID={laptop_id}")
        print(f"Размер стека: {self.stack_storage.size()}")

    def push_random_operation(self):
        """push() - добавить случайный элемент"""
        count = int(input("Сколько добавить? ") or "1")

        for _ in range(count):
            laptop_id = self._get_next_id()
            laptop = Laptop.create_obj(laptop_id, random=True)
            self.stack_storage.push(laptop)

        print(f"✅ push(): добавлено {count} случайных ноутбуков")
        print(f"Размер стека: {self.stack_storage.size()}")

    def read_operation(self):
        """read() - загрузить из файла в стек"""
        old_size = self.stack_storage.size()

        # Если стек не пустой, спрашиваем
        if old_size > 0:
            action = input(f"В стеке уже есть {old_size} элементов:\n"
                           "1. Очистить и загрузить заново\n"
                           "2. Добавить к существующим\n"
                           "Выбор: ")

            if action == "1":
                self.stack_storage = Stack()

        loaded_stack = self.repository.read()
        loaded_count = loaded_stack.size()

        # Переносим из загруженного стека в наш
        while not loaded_stack.is_empty():
            self.stack_storage.push(loaded_stack.pop())

        print(f"✅ read(): загружено {loaded_count} записей")
        print(f"Общий размер стека: {self.stack_storage.size()}")

    def peek_operation(self):
        """peek() - посмотреть верхний элемент"""
        if self.stack_storage.is_empty():
            print("❌ peek(): стек пуст")
            return

        laptop = self.stack_storage.peek()
        print("✅ peek(): верхний элемент:")
        for key, value in laptop.characteristics.items():
            print(f"  {key}: {value}")
        print(f"Размер стека остался: {self.stack_storage.size()}")

    def pop_operation(self):
        """pop() - взять верхний элемент"""
        if self.stack_storage.is_empty():
            print("❌ pop(): стек пуст")
            return

        laptop = self.stack_storage.pop()
        print("✅ pop(): извлечен элемент:")
        for key, value in laptop.characteristics.items():
            print(f"  {key}: {value}")
        print(f"Новый размер стека: {self.stack_storage.size()}")

    def write_operation(self):
        """write() - сохранить стек в файл"""
        if self.stack_storage.is_empty():
            print("❌ write(): стек пуст")
            return

        count = self.stack_storage.size()
        print(f"write(): в стеке {count} элементов")

        confirm = input("Сохранить и очистить стек? (y/n): ")
        if confirm.lower() != 'y':
            print("❌ Отменено")
            return

        # Создаем копию для демонстрации
        temp_stack = Stack()
        original_count = self.stack_storage.size()

        # Сохраняем в файл
        saved_count = self.repository.write(self.stack_storage)

        print(f"✅ write(): сохранено {saved_count} записей")
        print(f"Стек очищен. Размер: {self.stack_storage.size()}")

    def is_empty_operation(self):
        """is_empty() - проверить пустоту"""
        if self.stack_storage.is_empty():
            print("✅ is_empty(): True - стек пуст")
        else:
            print(f"✅ is_empty(): False - в стеке {self.stack_storage.size()} элементов")

    def size_operation(self):
        """size() - размер стека"""
        print(f"✅ size(): {self.stack_storage.size()} элементов")

    def clear_operation(self):
        """clear() - очистить стек"""
        if self.stack_storage.is_empty():
            print("✅ clear(): стек уже пуст")
            return

        count = self.stack_storage.size()
        confirm = input(f"Очистить стек ({count} элементов)? (y/n): ")

        if confirm.lower() == 'y':
            # Просто создаем новый пустой стек
            self.stack_storage = Stack()
            print(f"✅ clear(): стек очищен")
        else:
            print("❌ Отменено")
