from rich.console import Console

console = Console()

try:

    import os

    console.print("初始化执行 ", style="bold blue", end='')
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

except Exception as e:
    console.print("环境初始化报错{}".format(e), style="bold red")

try:
    # import pandas as pd
    # import numpy as np
    # import uuid
    # import torch

    pass
except Exception as e:
    console.print('导入下载包报错{}'.format(e), style="bold red")

try:
    # from tool.database.mysql import OperationMysqlData
    # from tool import BasicTool, random_password
    from tool.data.celsius_to_fahrenheit import fahrenheit_celsius
    from tool.database.mysql_tool import OperationMysqlData
    from src.config import MYSQL_ENGINE


except Exception as e:
    console.print('导入自定义包报错{}'.format(e), style="bold red")

try:
    # from src.config import file_path_name, MYSQL_ENGINE

    pass
except Exception as e:
    console.print('导入自定义参数报错{}'.format(e), style="bold red")

if __name__ == '__main__':
    try:
        console.print("--> 初始化完成开始启动\n", style="bold blue")
        # from tool import random_password
        # random_password()
        from tool.database.mysql_tool import OperationMysqlData
        from src.config import MYSQL_ENGINE
        path = '/Users/li/Downloads/目标_角色_面板.csv'
        OperationMysqlData(MYSQL_ENGINE).write_data(
            filepath=path, chunk_size=1000, table_name='目标_角色_面板', )
        # judgment_data = "01.000000000000000009we123-er"  # 处理的数据
        # _, data = fahrenheit_celsius(judgment_data, else_unit=['-'], numerical_not_unit='1')
        # print(f"{judgment_data} ->\n    {_} : {data}")

        # from tool.file.file import FolderOperations

        # OperationMysqlData(MYSQL_ENGINE).write_data('/Users/li/Downloads/洞天.csv', 1000, '洞天')

        # FolderOperations('/Volumes/LaCie/MyWork/Pcitc').def_folder_remove_file_junk()

        pass
    except Exception as e:
        print('都怪它-> {}'.format(e))
    finally:
        console.print("\nprogram end!", style="bold blue")
