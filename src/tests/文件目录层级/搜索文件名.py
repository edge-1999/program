import os


def _gain_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            for i in s_s:
                if i in file:
                    print(f'{root}/{file}')

        for dir_ in dirs:
            for i in s_s:
                if i in dir_:
                    print(f'{root}/{dir_}')


s_s = ['科研']
_gain_directory('/Volumes/LaCie/MyWork/石化盈科信息技术有限公司/基础管理/系统管理/内部系统')

