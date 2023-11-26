import os
from functools import wraps

from tool.monitor.monitor import monitor_decorator


@monitor_decorator
def validate_file_path(func):
    """
    判断文件是否存在
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        file_path = args[0]
        print(file_path)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        if not os.path.isfile(file_path):
            raise ValueError(f"The path '{file_path}' is not a file.")
        return func(*args, **kwargs)

    return wrapper


def verify_individual_file_paths(func):
    """
    仅判断输入第一个参数 单个文件是否存在
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # 获取文件路径参数，假设文件路径是函数的第一个参数
        file_path = args[0] if args else kwargs.get('file_path')

        # 判断路径是否为文件
        if os.path.isfile(file_path):
            # 文件验证成功，执行原函数
            return func(*args, **kwargs)
        else:
            print("文件路径验证失败！")
            choice = input("请选择操作（1: 重新输入文件路径, 2: 不执行函数）: ")

            if choice == '1':
                # 重新输入文件路径
                new_file_path = input("请输入新的文件路径: ")
                # 将新的文件路径传递给原函数，并递归调用装饰的函数
                return wrapper(new_file_path, *args[1:], **kwargs) if args else wrapper(file_path=new_file_path,
                                                                                        **kwargs)
            elif choice == '2':
                # 不执行函数，返回 None 或者其他默认值，程序继续运行
                print("函数未执行.")
                return None
            else:
                print("无效的选择！函数未执行.")
                return wrapper(*args, **kwargs)

    return wrapper
