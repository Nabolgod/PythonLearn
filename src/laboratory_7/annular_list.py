from src.laboratory_3.items.labtop.laptop import Laptop


class Node:
    """Узел двусвязного кольцевого списка"""

    def __init__(self, data: Laptop):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Node({self.data.id})"


class CircularDoublyLinkedList:
    """Двусвязный кольцевой список"""

    def __init__(self):
        self.head = None
        self.current = None  # Текущая позиция для обхода
        self.size = 0

    def is_empty(self) -> bool:
        """Проверка на пустоту"""
        return self.head is None

    def add_to_beginning(self, data: Laptop):
        """Добавление в начало списка"""
        new_node = Node(data)

        if self.is_empty():
            # Первый элемент - замыкаем сам на себя
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            # Вставляем перед head
            tail = self.head.prev

            new_node.next = self.head
            new_node.prev = tail

            self.head.prev = new_node
            tail.next = new_node

            self.head = new_node

        self.current = self.head  # Устанавливаем текущую позицию
        self.size += 1
        return new_node

    def add_to_end(self, data: Laptop):
        """Добавление в конец списка (эквивалентно вставке перед head)"""
        if self.is_empty():
            return self.add_to_beginning(data)

        new_node = Node(data)
        tail = self.head.prev

        new_node.next = self.head
        new_node.prev = tail

        tail.next = new_node
        self.head.prev = new_node

        self.size += 1
        return new_node

    def insert_after_current(self, data: Laptop):
        """Вставка после текущей позиции"""
        if self.is_empty() or self.current is None:
            return self.add_to_beginning(data)

        new_node = Node(data)
        next_node = self.current.next

        new_node.prev = self.current
        new_node.next = next_node

        self.current.next = new_node
        next_node.prev = new_node

        self.size += 1
        return new_node

    def delete_from_beginning(self):
        """Удаление из начала списка"""
        if self.is_empty():
            raise IndexError("Список пуст")

        if self.size == 1:
            # Единственный элемент
            deleted = self.head
            self.head = None
            self.current = None
        else:
            deleted = self.head
            tail = self.head.prev

            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head

            # Если current указывал на удаляемый элемент
            if self.current == deleted:
                self.current = self.head

        self.size -= 1
        deleted.next = None
        deleted.prev = None
        return deleted.data

    def move_next(self):
        """Переместиться к следующему элементу"""
        if self.is_empty():
            raise IndexError("Список пуст")

        if self.current is None:
            self.current = self.head
        else:
            self.current = self.current.next
        return self.current

    def move_prev(self):
        """Переместиться к предыдущему элементу"""
        if self.is_empty():
            raise IndexError("Список пуст")

        if self.current is None:
            self.current = self.head
        else:
            self.current = self.current.prev
        return self.current

    def get_current_data(self):
        """Получить данные текущего элемента"""
        if self.is_empty() or self.current is None:
            raise IndexError("Нет текущего элемента")
        return self.current.data

    def set_current_data(self, data: Laptop):
        """Обновить данные текущего элемента"""
        if self.is_empty() or self.current is None:
            raise IndexError("Нет текущего элемента")
        self.current.data = data

    def find_by_field(self, field_name: str, value):
        """Поиск по полю"""
        if self.is_empty():
            return None

        current = self.head
        for _ in range(self.size):
            if hasattr(current.data, field_name):
                field_value = getattr(current.data, field_name)
                if str(field_value) == str(value):
                    self.current = current
                    return current
            current = current.next

        return None

    def find_by_characteristics(self, characteristics: dict):
        """Поиск по всем характеристикам"""
        if self.is_empty():
            return None

        current = self.head
        for _ in range(self.size):
            match = True
            laptop_data = current.data.characteristics

            for key, value in characteristics.items():
                if key in laptop_data and str(laptop_data[key]) != str(value):
                    match = False
                    break

            if match:
                self.current = current
                return current

            current = current.next

        return None

    def __str__(self):
        """Строковое представление списка"""
        if self.is_empty():
            return "Список пуст"

        result = []
        current = self.head
        for i in range(self.size):
            is_current = " ←" if current == self.current else ""
            result.append(f"{i + 1}. ID: {current.data.id}{is_current}")
            current = current.next

        return "\n".join(result)

    def display_structure(self):
        """Отображение структуры списка с указателями"""
        if self.is_empty():
            print("Структура: пусто")
            return

        print("\nСТРУКТУРА СПИСКА:")
        print("═" * 50)

        current = self.head
        for i in range(self.size):
            prev_id = current.prev.data.id if current.prev else "None"
            next_id = current.next.data.id if current.next else "None"
            is_current = " ← ТЕКУЩИЙ" if current == self.current else ""

            print(f"[{i + 1}] Узел ID: {current.data.id}")
            print(f"    prev → {prev_id}")
            print(f"    next → {next_id}")
            print(f"    Данные: {current.data.model}{is_current}")
            print("-" * 30)

            current = current.next

        print(f"Всего элементов: {self.size}")
        print("═" * 50)
