import functools
from functools import wraps, lru_cache
from day_2.common import MyException

# готовое решение для хранения кэша - декоратор @lru_cache(maxsize=32)
# реализация хранения кэша вручную ниже в def memorize


def memorize(function):
    memo = {}

    @wraps(function)
    def wrapper(*args):
        try:
            return memo[args]
        except KeyError:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper


@memorize
def check_value(func):
    @functools.wraps(func)
    def wrapper(arg):
        if type(arg) is int and arg >= 0:
            value = func(arg)
        else:
            raise MyException
        return value
    return wrapper



