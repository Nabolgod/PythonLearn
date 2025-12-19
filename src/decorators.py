import time
from functools import wraps


def timer_decorate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        diff = end - start

        return result, diff

    return wrapper
