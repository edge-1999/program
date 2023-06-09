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

    pass
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
        # path = '/Users/li/Downloads/EQUITYRATIO_STRUCTURE.csv'
        # OperationMysqlData(MYSQL_ENGINE).write_data(
        #     filepath=path, chunk_size=1000, table_name='EQUITYRATIO_STRUCTURE',)
        judgment_data = "01.000000000000000009we123-er"  # 处理的数据
        _, data = fahrenheit_celsius(judgment_data, else_unit=['-'], numerical_not_unit='1')
        print(f"{judgment_data} ->\n    {_} : {data}")

        pass
    except Exception as e:
        print('都怪它-> {}'.format(e))
    finally:
        console.print("\nprogram end!", style="bold blue")
