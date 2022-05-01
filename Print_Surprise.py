from functools import wraps


def decorator(function):
    """
    :param function: A function which we like to execute
    :return: The inner function output
    """
    @wraps(function)
    def print_surprise(function_object):
        print("surprise!")
    return print_surprise


@decorator
def times2(num):
    """
    An example function that using decorators
    :param num: Num to calculate in the function
    :return: The doubled num which the function received
    """
    return num * 2
