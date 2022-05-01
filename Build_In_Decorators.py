import atexit
import functools


@atexit.register
def registered_function():
    """
    Execute when finish the module
    """
    print("Bye Bye")


@functools.lru_cache(maxsize=None)
def fib(n):
    """
    Fibonnaci function to calculate N number
    :param n: Number limit in the series
    :return: The fibonnaci N number in the series
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


class C:
    @staticmethod
    def f():
        print("I'm static!!")
