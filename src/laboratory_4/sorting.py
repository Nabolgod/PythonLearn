import math
from src.decorators import timer_decorate


class Sorting:
    def __init__(self, array):
        self.array = array.copy()  # Создаем копию, чтобы не изменять оригинал
        self.original = array.copy()  # Сохраняем оригинал для сброса

    def reset(self):
        """Сбросить массив к исходному состоянию"""
        self.array = self.original.copy()
        return self.array

    @timer_decorate
    def bubble_sort(self):
        """
        Пузырьковая сортировка.
        Возвращает отсортированную копию массива.
        """
        arr = self.array.copy()  # Работаем с копией, чтобы не менять self.array
        n = len(arr)

        for i in range(n - 1):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if not swapped:
                break

        return arr

    @timer_decorate
    def selection_sort(self):
        """
        Сортировка выбором.
        Возвращает отсортированную копию массива.
        """
        arr = self.array.copy()
        n = len(arr)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr

    @timer_decorate
    def introsort(self):
        """
        Интроспективная сортировка (Introsort).
        Возвращает отсортированную копию массива.
        """
        arr = self.array.copy()

        def _introsort(arr, start, end, max_depth):
            if end - start < 16:
                _insertion_sort(arr, start, end)
                return

            if max_depth == 0:
                _heapsort(arr, start, end)
                return

            pivot_idx = _partition(arr, start, end)
            _introsort(arr, start, pivot_idx - 1, max_depth - 1)
            _introsort(arr, pivot_idx + 1, end, max_depth - 1)

        def _partition(arr, start, end):
            mid = (start + end) // 2

            if arr[mid] < arr[start]:
                arr[start], arr[mid] = arr[mid], arr[start]
            if arr[end] < arr[start]:
                arr[start], arr[end] = arr[end], arr[start]
            if arr[mid] < arr[end]:
                arr[mid], arr[end] = arr[end], arr[mid]

            pivot = arr[end]
            i = start - 1

            for j in range(start, end):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[end] = arr[end], arr[i + 1]
            return i + 1

        def _heapsort(arr, start, end):
            def _heapify(arr, n, i, start):
                largest = i
                left = 2 * i + 1
                right = 2 * i + 2

                if left < n and arr[start + left] > arr[start + largest]:
                    largest = left
                if right < n and arr[start + right] > arr[start + largest]:
                    largest = right

                if largest != i:
                    arr[start + i], arr[start + largest] = arr[start + largest], arr[start + i]
                    _heapify(arr, n, largest, start)

            n = end - start + 1

            for i in range(n // 2 - 1, -1, -1):
                _heapify(arr, n, i, start)

            for i in range(n - 1, 0, -1):
                arr[start], arr[start + i] = arr[start + i], arr[start]
                _heapify(arr, i, 0, start)

        def _insertion_sort(arr, start, end):
            for i in range(start + 1, end + 1):
                key = arr[i]
                j = i - 1

                while j >= start and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1

                arr[j + 1] = key

        n = len(arr)
        if n <= 1:
            return arr

        max_depth = 2 * math.floor(math.log2(n))
        _introsort(arr, 0, n - 1, max_depth)

        return arr

    @staticmethod
    def formated_array(array, size: int = 5):
        return f"[{', '.join(map(str, array[:size]))}, ..., {', '.join(map(str, array[-size:]))}]"

    def compare_all(self):
        """Сравнить все алгоритмы сортировки"""
        print(f"\nИсходный массив (первые 10 элементов): {self.array[:10]}...")
        print(f"Длина массива: {len(self.array)}")
        print("-" * 50)

        print("Программа начала работу!")
        results = {}

        # Список алгоритмов для тестирования
        algorithms = [
            ('bubble', self.bubble_sort, 'Пузырьковая сортировка'),
            ('selection', self.selection_sort, 'Сортировка выбором'),
            ('introsort', self.introsort, 'Интроспективная сортировка')
        ]

        for algo_name, algo_func, algo_display in algorithms:
            self.reset()
            result, time_taken = algo_func()
            results[algo_name] = self.formated_array(result)
            print(f"{algo_display}: {results[algo_name]}")
            print(f"Время: {time_taken:.6f} сек")

        print("\nПрограмма закончила работу!")
        return results
