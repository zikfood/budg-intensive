import functools
import time
from day_2.common import MyException


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """

    def call_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for item in range(times):
                try:
                    result = func(*args, **kwargs)
                    break
                except:
                    time.sleep(delay)
            else:
                raise MyException
            return result
        return wrapper

    return call_func

