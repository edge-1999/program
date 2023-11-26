from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 调用原始函数
        print('wrapper: ', *args, **kwargs)
        args[0] = 3
        result = func(*args, **kwargs)
        print('result: ', result)

        # 对返回值进行处理
        modified_result = result + 1
        print('modified_result: ', modified_result)

        # 返回处理后的值
        return modified_result

    return wrapper


@decorator
def add(a, b):
    print(a, b)
    return a + b


print(add(2, 3))  # 输出将会是 6 而不是 5
