import os


def generate_file_tree_local(path: str, depth: int, site: list):
    """
    递归打印文件目录树状图（使用局部变量）

    :param path: 根目录路径
    :param depth: 根目录、文件所在的层级号
    :param site: 存储出现转折的层级号
    :return: None
    """
    void_num = 0
    filenames_list = os.listdir(path)

    for item in filenames_list:
        if '._' == item[:2]:
            continue
        string_list = ["│   " for _ in range(depth - void_num - len(site))]
        for s in site:
            string_list.insert(s, "    ")

        if item != filenames_list[-1]:
            string_list.append("├── ")
        else:
            # 本级目录最后一个文件：转折处
            string_list.append("└── ")
            void_num += 1
            # 添加当前已出现转折的层级数
            site.append(depth)
        print("".join(string_list) + item)

        new_item = path + '/' + item
        if os.path.isdir(new_item):
            generate_file_tree_local(new_item, depth + 1, site)
        if item == filenames_list[-1]:
            void_num -= 1
            # 移除当前已出现转折的层级数
            site.pop()


if __name__ == '__main__':
    root_path = '/Volumes/LaCie/MyWork/石化盈科信息技术有限公司/项目管理/业审融合大数据项目(一期)/3.实施/1.数据专区/1.源系统数据调研/B01-需求清单/2.审计内控需求'
    print(os.path.abspath(root_path))
    generate_file_tree_local(root_path, depth=0, site=[])
