def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)

    print("Decorator 1 end")
    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)

    print("Decorator 2 end")
    return wrapper


@decorator1
@decorator2
def some_function():
    print("Function body")


some_function()
