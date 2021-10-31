# Написать декоратор для логирования типов позиционных аргументов функции

from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        list = [el for el in (*args, *kwargs.values())]
        n = [f'{func.__name__}({el}: {type(el)})' for el in list]
        print(*n, *func(*args, **kwargs))

    return wrapper

@logger
def calc_cube(*a, **b):
    list = [el for el in (*a, *b.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in list]

a = calc_cube(5)
print(calc_cube.__name__)