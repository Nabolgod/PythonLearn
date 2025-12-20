import sys
from pathlib import Path

from src.laboratory_6.stack import Stack

sys.path.append(str(Path(__file__).parent.parent))

from src.laboratory_4.sorting import Sorting
from src.utils import generate_array_random, search_test
from src.laboratory_3.interface import Interface
from src.repositories.laptop_list import LaptopRepositoryList
from src.laboratory_5.search import Search


def start_laboratory_3():
    interface = Interface(LaptopRepositoryList())
    interface.start()


def start_laboratory_4():
    not_sorted_array = generate_array_random(10_000)
    sorted_array = sorted(not_sorted_array)
    reverse_sorted_array = sorted(not_sorted_array, reverse=True)

    not_sorted_manager = Sorting(not_sorted_array)
    not_sorted_manager.compare_all()

    sorted_manager = Sorting(sorted_array)
    sorted_manager.compare_all()

    reverse_sorted_manager = Sorting(reverse_sorted_array)
    reverse_sorted_manager.compare_all()


def start_laboratory_5():
    not_sorted_array = generate_array_random(10_000, -200_000, 200_000)

    sorted_info = Sorting(not_sorted_array).introsort()
    sorted_array = sorted_info[0]
    sorted_time = sorted_info[1]

    not_sorted_search = Search(not_sorted_array)
    sorted_search = Search(sorted_array)

    # Тестируем разные методы поиска
    linear_time = search_test(not_sorted_search, 'linear_search')
    binary_time = search_test(sorted_search, 'binary_search')
    interp_time = search_test(sorted_search, 'interpolation_search')
    jump_time = search_test(sorted_search, 'jump_search')

    print("Время работы линейного поиска: ", linear_time)
    print("Время работы сортировки с бинарным поиском: ", sorted_time + binary_time)
    print("Время работы сортировки с интерполяционным поиском: ", sorted_time + interp_time)
    print("Время работы сортировки с поиском прыжками: ", sorted_time + jump_time)


def start_laboratory_6():
    storage = Stack()


if __name__ == "__main__":
    start_laboratory_4()
