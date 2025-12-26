import random
import math


def generate_random_number(start, end):
    return random.randint(start, end)


def generate_random_power_two(start, end):
    min_power = math.ceil(math.log2(start))
    max_power = math.floor(math.log2(end))

    return 2 ** generate_random_number(min_power, max_power)


def generate_array_random(size=100_000, start=-2_000_000, end=2_000_000):
    return [generate_random_number(start, end) for _ in range(size)]


def search_test(search_obj, search_method='linear_search', size=100_000, start=-200_000, end=200_000):
    """Тестирование производительности поиска"""
    total_time = 0
    for _ in range(size):
        target = generate_random_number(start, end)
        search_func = getattr(search_obj, search_method)
        _, time_taken = search_func(target)
        total_time += time_taken

    return total_time
