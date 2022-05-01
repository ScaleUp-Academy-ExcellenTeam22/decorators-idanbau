import decorator


@decorator.decorator
def call_function_twice(func, *args, **kwargs):
    """
    :param func: The function which we like to execute
    :param args: The wanted function arguments
    :param kwargs: The wanted function optional arguments
    :return: A list with 2 elements that returned from the function
    """
    return [func(*args, **kwargs) for _ in range(2)]


@call_function_twice
def times2(num):
    """
    An example function that using decorators
    :param num: Num to calculate in the function
    :return: The doubled num which the function received
    """
    return num * 2

