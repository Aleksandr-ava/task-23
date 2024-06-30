def create_operation(operation):
    if operation == "multiplication":
        def multiplication(x, y):
            return x * y
        return multiplication
    elif operation == "division":
        def division(x, y):
            return x / y
        return division


my_func_multiplication = create_operation("multiplication")
my_func_division = create_operation("division")
print(my_func_multiplication(3, 2))
print(my_func_division(6, 3))


square = lambda x: x ** 2
print(square(4))


def square(x):
    return x ** 2


print(square(4))


class Rect:
    def __init__(self, a):
        self.value = a

    def __call__(self, b):
        return self.value * b


square = Rect(2)
print(square(4))
