def validate_input(expected_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, expected_type):
                    raise ValueError(f"Expected type {expected_type}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_input(int)
def process_number(num):
    # Function logic here
    # return num * 2
    print(num)
    return 'ok'


a = process_number(1)
print(a)
