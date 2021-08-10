import functools


def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        func(*args, **kwargs)
        return wrapper.count
    wrapper.count = 0
    return wrapper

