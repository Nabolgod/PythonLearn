import random
import math


def generate_random_number(start, end):
    return random.randint(start, end)


def generate_random_power_two(start, end):
    min_power = math.ceil(math.log2(start))
    max_power = math.floor(math.log2(end))

    return 2 ** generate_random_number(min_power, max_power)


class LaptopDescriptor:
    def __set_name__(self, owner, name):
        self.name = f"__{owner.__name__}_{name}"

    def __init__(self, lower_limit=1, upper_limit=10, power_of_two=False):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.power_of_two = power_of_two

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self.name not in instance.__dict__:
            raise AttributeError(f"Атрибут не создан")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value is None:
            value = (
                generate_random_power_two(self.lower_limit, self.upper_limit)
                if self.power_of_two else
                generate_random_number(self.lower_limit, self.upper_limit)
            )
            instance.__dict__[self.name] = value
        else:
            instance.__dict__[self.name] = value
