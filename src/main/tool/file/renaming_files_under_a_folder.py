import os


def get_folder_name(path) -> str:
    """获取文件夹的名称"""
    return os.path.basename(path)


def get_folder_path(path) -> str:
    """获取文件夹的路径"""
    return os.path.dirname(path)


def exists_path(path) -> bool:
    """判断文件或文件夹是否存在"""
    return os.path.exists(path)


def get_file_extension(path) -> str:
    """获取文件后缀名"""
    return os.path.splitext(path)[1].lstrip(".")


class FileRenamer:
    """
    使用方法：
        renamer = FileRenamer('/Users/li/Downloads/F_OP 20231017', '20231017')
        renamer.run()
    """

    def __init__(self, folder_path: str, format_time: str):
        self.folder_path_main = folder_path
        self.format_time = format_time
        self.file_zfill = 0
        if isinstance(folder_path, str) and os.path.isdir(folder_path):
            self.folder_path_main_name = get_folder_name(self.folder_path_main)
            self.folder_path_main_path = get_folder_path(self.folder_path_main)
            self.folder_path_work = self.folder_path_main
            self.folder_work_name = get_folder_name(self.folder_path_main)
            self.folder_work_path = get_folder_path(self.folder_path_main)
        else:
            raise '请输入正确的文件夹地址'

    def refresh_parameter(self, path):
        self.folder_path_work = path
        self.folder_work_name = get_folder_name(path)
        self.folder_work_path = get_folder_path(path)

    @property
    def def_file_zfill(self) -> int:
        """判断需要左填充几位数字0"""
        file_count, _ = self.count_files_and_folders
        return len(str(file_count))

    @property
    def count_files_and_folders(self) -> (int, int):
        """只获取子目录下文件与文件夹数量，不获取子目录下级的数量"""
        file_count = 0
        folder_count = 0
        for item in os.listdir(self.folder_path_work):
            item_path = os.path.join(self.folder_path_work, item)
            if os.path.isfile(item_path) and item not in [".DS_Store", ".localized"]:
                file_count += 1
            elif os.path.isdir(item_path):
                folder_count += 1

        return file_count, folder_count

    def main_folder_rename(self):
        new_folder_name = '{} {}'.format(input('请输入自定义文件夹名称：'), self.format_time)
        new_folder = os.path.join(self.folder_work_path, new_folder_name)
        if exists_path(new_folder):
            raise '文件夹存在，请重新输入'
        else:
            os.rename(self.folder_path_work, new_folder)
            self.refresh_parameter(new_folder)

    def run(self):
        # 当前输入文件夹是否重新命名
        mark = input('当前文件夹是否重命名(输入Y|y)：').upper()
        if mark and mark[0] == "Y":
            self.main_folder_rename()
        file_count, folder_count = self.count_files_and_folders
        if file_count > 0:
            str_name = input('请输入自定义名称：')
            new_str_name = '{} {}'.format(str_name, self.folder_work_name)
            list_dir = []
            for item in os.listdir(self.folder_path_work):
                item_path = os.path.join(self.folder_path_work, item)
                if os.path.isfile(item_path) and item not in [".DS_Store", ".localized"]:
                    list_dir.append(item_path)
            for i in range(1, file_count + 1):
                file_all = list_dir.pop()
                os.rename(file_all, '{}/{} {}.{}'.format(
                    get_folder_path(file_all), new_str_name,
                    str(i).zfill(self.def_file_zfill), get_file_extension(file_all)))
