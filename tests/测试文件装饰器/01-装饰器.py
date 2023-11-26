import os
from functools import wraps


def validate_file_path(func):
    print('开始执行 validate_file_path')

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('开始执行 wrapper')
        # 假设文件路径是第一个参数，你可以根据需要调整这里的逻辑
        print(*args, **kwargs)
        file_path = args[0]

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        if not os.path.isfile(file_path):
            raise ValueError(f"The path '{file_path}' is not a file.")
        print('结束执行 wrapper')
        return func(*args, **kwargs)

    print('结束执行 validate_file_path')
    return wrapper


# 使用装饰器的示例
@validate_file_path
def process_file(file_path, type):
    print(f"Processing file: {file_path}")
    # 在这里添加处理文件的代码
