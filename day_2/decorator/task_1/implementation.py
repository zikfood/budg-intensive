import functools
import time


def time_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        exec_time = end_time - start_time
        print(exec_time)
        return value
    return wrapper
