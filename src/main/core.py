from rich.console import Console

console = Console()

try:

    import os

    console.print("初始化执行 ", style="bold blue", end='')
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

except Exception as e:
    console.print("环境初始化报错{}".format(e), style="bold red")

try:
    import pandas as pd
    import numpy as np
    import uuid
    import torch
except Exception as e:
    console.print('导入下载包报错{}'.format(e), style="bold red")

try:
    from tool.database.mysql import OperationMysqlData
    from tool import BasicTool, random_password
except Exception as e:
    console.print('导入自定义包报错{}'.format(e), style="bold red")

try:
    from src.config import file_path_name, MYSQL_ENGINE
except Exception as e:
    console.print('导入自定义参数报错{}'.format(e), style="bold red")

if __name__ == '__main__':
    try:
        console.print("--> 初始化完成开始启动\n", style="bold blue")
        random_password()
        # path = '/Users/li/Downloads'
        # FileAll(path, ).remove_file_model(path, "file")
        # file_path = '/Users/li/Downloads/ROW_2.csv'
        # OperationMysqlData(MYSQL_ENGINE).write_data(file_path, 1000, 'ROW_2', 'append', )

        # BasicTool()
        # torch.nn.L1Loss(reduction='mean')
        # random_password()
        pass
    except Exception as e:
        print('都怪它-> {}'.format(e))
