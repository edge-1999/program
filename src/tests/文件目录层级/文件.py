import os

import numpy as np
import pandas as pd


class FileTree(object):
    def __init__(self, directory_path, to_excel_path):
        """
        directory_path:目录例如：'/Users/li/Downloads/2023.0619集团公司总部内控手册'
        to_excel_path:保存为excel_path的路径 例如：'/Users/li/Downloads/工作簿1_out.xlsx'
        header_title：标题 例如：["类型", "文件路径", "文件目录", "父级目录"]
        """
        self.directory_path = directory_path
        self.to_excel_path = to_excel_path
        self.data = []  # 替换为 np 或 pd
        self.status = False

    def _gain_directory(self, directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if '._' == file[:2] or '.DS_Store' == file:
                    continue
                p1 = str(root + '/' + file).replace(self.directory_path, '')
                p2 = root.replace(self.directory_path, '')
                pd_data = [
                    "文件", p1.replace('/', '', 1) if '/' == p1[:1] else p1,
                    file, p2.replace('/', '', 1) if '/' == p2[:1] else p2]
                print(pd_data)
                self.data.append(pd_data)
            for dir_ in dirs:
                if '._' == dir_[:2]:
                    continue
                p1 = str(root + '/' + dir_).replace(self.directory_path, '')
                p2 = root.replace(self.directory_path, '')
                pd_data = [
                    "目录", p1.replace('/', '', 1) if '/' == p1[:1] else p1, dir_,
                    p2.replace('/', '', 1) if '/' == p2[:1] else p2]
                print(pd_data)
                self.data.append(pd_data)
        # return self.data

    def _to_excel_file(self, data, to_excel_path):
        pd.DataFrame(data).to_excel(to_excel_path, index=False, header=["类型", "文件路径", "文件目录", "父级目录"])
        self.status = True
        return self.status

    def run(self):
        self._gain_directory(self.directory_path)
        return self._to_excel_file(np.array(self.data), self.to_excel_path)


st = FileTree(
    # '/Users/li/Downloads/2023.0619集团公司总部内控手册',
    '/Users/li/Downloads/thing',
    '/Users/li/Downloads/工作簿1_out.xlsx',
)
st.run()
print('ok')
