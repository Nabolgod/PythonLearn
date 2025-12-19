import math
from src.decorators import timer_decorate


class Search:
    def __init__(self, array):
        self.array = array

    @timer_decorate
    def linear_search(self, target):
        """Алгоритм линейного поиска."""
        for i, value in enumerate(self.array):
            if value == target:
                return i
        return None

    @timer_decorate
    def binary_search(self, target):
        """Алгоритм бинарного поиска в отсортированном массиве."""
        left, right = 0, len(self.array) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if self.array[mid] == target:
                return mid
            elif self.array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return None

    @timer_decorate
    def interpolation_search(self, target):
        """
        Алгоритм интерполяционного поиска в отсортированном массиве.
        """
        left = 0
        right = len(self.array) - 1

        # Проверяем, что target находится в пределах массива
        if right < 0 or target < self.array[left] or target > self.array[right]:
            return -1

        while left <= right and self.array[left] <= target <= self.array[right]:
            # Если границы совпали
            if left == right:
                if self.array[left] == target:
                    return left
                return -1

            # Вычисляем позицию с помощью интерполяционной формулы
            # pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
            pos = left + ((target - self.array[left]) * (right - left)) // (self.array[right] - self.array[left])

            # Проверяем границы pos
            if pos < left:
                pos = left
            if pos > right:
                pos = right

            # Сравниваем элемент в позиции pos с target
            if self.array[pos] == target:
                return pos
            elif self.array[pos] < target:
                left = pos + 1
            else:
                right = pos - 1

        return -1

    @timer_decorate
    def jump_search(self, target, step=None):
        """Алгоритм прыжкового поиска в отсортированном массиве."""
        n = len(self.array)

        # Вычисляем оптимальный шаг, если не указан
        if step is None:
            step = int(math.sqrt(n))

        # Прыжки вперед
        prev = 0
        while prev < n and self.array[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1

        # Линейный поиск в блоке
        while prev < min(step, n):
            if self.array[prev] == target:
                return prev
            prev += 1

        return None
