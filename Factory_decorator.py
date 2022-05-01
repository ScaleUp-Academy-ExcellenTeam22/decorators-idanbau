from functools import wraps


def type_check(correct_type: type):
    """
    The Function receives object type and checks if the object inserted is in the same instance
    :param correct_type: The type to check
    :return: the results of the function otherwise error.
    """
    def decorator_factory(function):
        """
        The function wraps another function to check if it in the same instance.
        :param function: The wanted function to execute.
        :return: Itself using the wrapped function which we called.
        """
        @wraps(function)
        def check_type(function_object):
            """
            The function check if the type is in the same instance of the type, if not it raises an error.
            :param function_object: the object to pass to the function
            :return: the function results
            """
            if not isinstance(function_object, correct_type):
                raise Exception("Not the correct type")
            return function(function_object)

        return check_type

    return decorator_factory


@type_check(int)
def times2(num):
    """
    An example function that using decorators
    :param num: Num to calculate in the function
    :return: The doubled num which the function received
    """
    return num * 2
