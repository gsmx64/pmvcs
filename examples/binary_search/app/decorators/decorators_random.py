""" Decorators for Random Data file for Python MVC Shell Framework Package """
import functools

def remove_duplicates_decorator(func: list) -> list:
    """
    Decorator for removing duplicated numbers: Removes
    duplicates numbers in list()
    """
    @functools.wraps(func)
    def wrapped_remove_duplicates(self) -> list:
        test_list = func(self)
        value = []
        [value.append(x) for x in test_list if x not in value]
        return value
    return wrapped_remove_duplicates

def sorted_decorator(func: list) -> list:
    """
    Decorator for sorting numbers: Order from smallest
    to largest numbers in list()
    """
    @functools.wraps(func)
    def wrapped_sorted(self) -> list:
        value = func(self)
        return sorted(value)
    return wrapped_sorted
