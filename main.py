import Factory_decorator
import Print_Surprise
import Decorates_twice
import Build_In_Decorators
if __name__ == "__main__":
    print(Factory_decorator.times2(3))
    Print_Surprise.times2(3)
    print(Decorates_twice.times2(3))
    print(Build_In_Decorators.fib(100))
    print(Build_In_Decorators.C.f())
