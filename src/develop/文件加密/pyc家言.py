# import marshal
# import time
#
# # 定义要编译的源代码
# source_code = """
# def hello():
#     print("Hello, world!")
# """
#
# # 编译源代码
# compiled_code = compile(source_code, "<string>", "exec")
#
# # 创建元数据字典
# metadata = {
#     "source_timestamp": time.time(),  # 添加时间戳
#     "custom_salt": "your_salt_here"  # 添加自定义盐
# }
#
# # 将元数据和编译后的代码保存到 .pyc 文件
# with open("your_script.pyc", "wb") as pyc_file:
#     marshal.dump(metadata, pyc_file)
#     marshal.dump(compiled_code, pyc_file)
