import re


# 1
def to_camel_case(text):
    return re.split('_|-', text)[0].title() + ''.join(word.title() for word in re.split('_|-', text)[1::])


# 2
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# 3
# PEP 8: E731 do not assign a lambda expression, use a def.
lambda_count_bits = lambda n: bin(number).count('1')


# PEP 8 way:
def count_bits(number):
    return bin(number).count('1')


# 4
def do_less_then_ten(number):
    return number if number < 10 else do_less_then_ten(sum(map(int, str(number))))


# 5
# PEP 8: E731 do not assign a lambda expression, use a def
lambda_even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"


# # PEP 8 way:
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


