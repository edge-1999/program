import os


def validate_file_path(func):
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
                return None

    return wrapper


# 使用装饰器
@validate_file_path
def process_file(file_path):
    print(f"处理文件：{file_path}")


# 示例
file_path_to_process = "example.txt"
result = process_file(file_path_to_process)
print("函数执行结果:", result)
