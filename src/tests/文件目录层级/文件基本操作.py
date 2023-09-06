# import json
# import os
#
# import numpy as np
# import pandas as pd
# from docx import Document
# from decimal import Decimal
#
#
# class FileOperations(object):
#     def __init__(self, file_path):
#         """文件进行操作"""
#         self.file_path = None
#         self.file_size = Decimal(0)
#         self.identifying = False
#         self.error_message = []
#         try:
#             if isinstance(file_path, str) and os.path.isfile(file_path):
#                 self.file_path = file_path
#                 self.identifying = True
#             else:
#                 self.identifying = False
#                 self.error_message.append(f'当前文件 {self.file_path} 报错信息为：请输入正确的文件地址')
#         except Exception as e:
#             self.identifying = False
#             self.error_message.append(f'执行__init__初始化时报错，当前文件 {self.file_path} 报错信息为：{e}')
#
#     def def_file_json_load_manipulate(self):
#         """json文件读取操作"""
#
#         try:
#             if len(self.file_path) > 4 and self.file_path[-5:].upper() == '.JSON':
#                 with open(self.file_path, 'r', encoding="utf-8") as f:
#                     return json.load(f)
#             self.identifying = False
#             self.error_message.append(
#                 f'执行json文件读取操作时报错，当前文件 {self.file_path} 报错信息为：此文件不是json文件')
#         except Exception as e:
#             self.identifying = False
#             self.error_message.append(f'执行json文件读取操作时报错，当前文件 {self.file_path} 报错信息为：{e}')
#
#     def def_file_json_store_manipulate(self, data):
#         """json文件写入操作"""
#         try:
#             if len(self.file_path) > 4 and self.file_path[-5:].upper() == '.JSON':
#                 with open(self.file_path, 'w', encoding="utf-8") as file_write:
#                     file_write.write(json.dumps(dict(data, ensure_ascii=False)))
#                     # json.dump(data, file_write, ensure_ascii=False)
#                     self.identifying = True
#                     print(f'数据覆盖写入文件 {self.file_path} 成功')
#             self.identifying = False
#             self.error_message.append(
#                 f'执行json文件写入操作时报错，当前文件 {self.file_path} 报错信息为：此文件不是json文件')
#         except Exception as e:
#             self.error_message.append(f'执行json文件写入操作时报错，当前文件 {self.file_path} 报错信息为：{e}')
#
#     def def_file_xlsx_xls_search_for_manipulate(self, search_data):
#         """xlsx_xls 搜索操作"""
#         try:
#             if len(self.file_path) > 4 and self.file_path[-5:].upper() == '.XLSX':
#                 xlsx = pd.ExcelFile(self.file_path)
#                 for name in xlsx.sheet_names:
#                     data = pd.read_excel(xlsx, sheet_name=name, engine='openpyxl').fillna('')
#                     for x in data.values:
#                         for C in search_data:
#                             if C in ''.join(str(x)):
#                                 self.identifying = True
#                                 return self.identifying
#                                 # yield self.file_path  # 方便日后做其余操作
#             elif len(self.file_path) > 3 and self.file_path[-4:].upper() == '.XLS':
#                 xlsx = pd.ExcelFile(self.file_path)
#                 for name in xlsx.sheet_names:
#                     data = pd.read_excel(xlsx, sheet_name=name).fillna('')
#                     for x in data.values:
#                         for C in search_data:
#                             if C in ''.join(str(x)):
#                                 self.identifying = True
#                                 return self.identifying
#                                 # return self.identifying
#                                 # yield self.file_path  # 方便日后做其余操作
#             self.identifying = False
#             self.error_message.append(
#                 f'执行 xlsx_xls 文件搜索操作时报错，当前文件 {self.file_path} 报错信息为：此文件不是表格类型文件')
#             return self.identifying
#         except Exception as e:
#             print('ok')
#             self.identifying = False
#             self.error_message.append(f'执行 xlsx_xls 文件搜索操作时报错，当前文件 {self.file_path} 报错信息为：{e}')
#
#     def def_csv_search_for_manipulate(self, search_data):
#         try:
#             if len(self.file_path) > 3 and self.file_path[-4:].upper() == '.CSV':
#                 data_ = np.array(pd.read_csv(self.file_path).replace(np.nan, ''))
#                 for i in data_:
#                     for j in search_data:
#                         if j in i:
#                             self.identifying = True
#                             return self.identifying
#                             # yield self.file_path
#             self.identifying = False
#             self.error_message.append(
#                 f'执行 csv 文件搜索操作时报错，当前文件 {self.file_path} 报错信息为：此文件不是 csv 类型文件')
#         except Exception as e:
#             self.identifying = False
#             self.error_message.append(f'执行 csv 文件搜索操作时报错，当前文件 {self.file_path} 报错信息为：{e}')
#
#     def def_docx_search_for_manipulate(self, search_data):
#         """docx 文件搜索操作"""
#         try:
#             if len(self.file_path) > 4 and self.file_path[-5:].upper() == '.DOCX':
#                 doc = Document(self.file_path)
#                 docx_data = ""
#                 docx_data_tb = ""
#                 for para in doc.paragraphs:
#                     docx_data += para.text + "\n"
#                 tbs = doc.tables
#                 for tb in tbs:
#                     for row in tb.rows:
#                         for cell in row.cells:
#                             # docx_data_tb += f'{(cell.text):<5}'
#                             docx_data_tb += '{({}):<5}'.format(cell.text)
#                 for dt in search_data:
#                     if dt in docx_data or dt in docx_data_tb:
#                         self.identifying = True
#                         # return True
#                         return self.identifying
#                         # yield self.file_path
#             self.identifying = False
#             self.error_message.append(
#                 f'执行 docx 文件搜索操作时报错，当前文件 {self.file_path} 报错信息为：此文件不是 docx 类型文件')
#         except Exception as e:
#             self.identifying = False
#             self.error_message.append(f'执行 docx 文件搜索操作时报错，当前文件 {self.file_path} 报错信息为：{e}')
#
#     def def_txt_search_for_manipulate(self, search_data):
#         try:
#             if len(self.file_path) > 3 and self.file_path[-4:].upper() == '.TXT':
#                 txt_data = open(self.file_path)
#                 for dt in search_data:
#                     if dt in txt_data:
#                         self.identifying = True
#                         return self.identifying
#                         # yield self.file_path
#             self.identifying = False
#             self.error_message.append(
#                 f'执行 txt 文件搜索操作时报错，当前文件 {self.file_path} 报错信息为：此文件不是 txt 类型文件')
#         except Exception as e:
#             self.identifying = False
#             self.error_message.append(f'执行 txt 文件搜索操作时报错，当前文件 {self.file_path} 报错信息为：{e}')
#
#     @property
#     def def_file_filter_junk(self) -> bool:
#         """判断文件是否是垃圾文件"""
#         from src.config import file_path_name
#
#         file_filter = file_path_name["filter_rubbish_file"] + file_path_name["Mac_filter_rubbish_file"]
#
#         # file_name = os.path.dirname(self.file_path)
#         file_name = os.path.basename(self.file_path)
#
#         for file_filter_name in file_filter:
#             if file_filter_name == file_name[: len(file_filter_name)]:
#                 self.identifying = True
#                 return self.identifying
#         self.identifying = False
#         return self.identifying
#
#     @property
#     def def_file_filter_junk_remove(self) -> bool:
#         """删除垃圾文件"""
#         if self.def_file_filter_junk:
#             os.remove(self.file_path)
#             self.identifying = True
#             return self.identifying
#         self.identifying = False
#         return self.identifying
#
#     def def_file_filter_appoint(self, file_data) -> bool:
#         """判断文件是否是指定文件"""
#         if isinstance(file_data, (list, set)) and file_data:
#             for file_name in file_data:
#                 if os.path.basename(self.file_path) == os.path.basename(file_name):
#                     self.identifying = True
#             self.identifying = False
#         elif isinstance(file_data, str):
#             if os.path.basename(self.file_path) == os.path.basename(file_data):
#                 self.identifying = True
#             self.identifying = False
#
#         return self.identifying
#
#     def def_file_filter_appoint_remove(self, file_data) -> bool:
#         if self.def_file_filter_appoint(file_data):
#             os.remove(self.file_path)
#             self.identifying = True
#             return self.identifying
#         self.identifying = False
#         return self.identifying
#
#     @property
#     def def_file_size(self):
#         return Decimal(os.path.getsize(self.file_path))
#
#     @property
#     def def_file_output_size(self):
#         """返回文件大小描述"""
#
#         # from decimal import Decimal, getcontext
#         # getcontext().prec = 100
#         self.file_size = self.def_file_size
#         file_size_default_radix = Decimal(1024)
#         file_size_kb = self.file_size / file_size_default_radix
#         if file_size_kb >= file_size_default_radix:
#             file_size_mb = file_size_kb / file_size_default_radix
#             if file_size_mb >= file_size_default_radix:
#                 file_size_gb = file_size_mb / file_size_default_radix
#                 if file_size_gb >= file_size_default_radix:
#                     file_size_tb = file_size_gb / file_size_default_radix
#                     return f'文件 {self.file_path} 大小为：{file_size_tb} TB'
#                 else:
#                     return f'文件 {self.file_path} 大小为：{file_size_gb} GB'
#             else:
#                 return f'文件 {self.file_path} 大小为：{file_size_mb} MB'
#         else:
#             return f'文件 {self.file_path} 大小为：{file_size_kb} KB'
#
#
# class FolderOperations(object):
#     def __init__(self, folder_path):
#         """对此文件夹进行操作"""
#         self.identifying = False
#         self.file_output_data = []
#         self.error_message = []
#         try:
#             if isinstance(folder_path, str) and os.path.isdir(folder_path):
#                 self.folder_path = folder_path
#                 self.identifying = True
#             else:
#                 self.error_message.append(f'当前文件夹 {self.folder_path} 报错信息为：请输入正确的文件地址')
#         except Exception as e:
#             self.error_message.append(f'当前文件夹 {self.folder_path} 报错信息为：{e}')
#
#     def def_folder_search_content(self):
#         """搜索文件夹下文件包含搜索内容的文件"""
#         if self.identifying:
#             from src.config import file_path_name
#             while True:
#                 print(
#                     f"目前识别文件格式为: {' '.join(i for i in file_path_name['file_search_for'])} 其他文件等待上线，"
#                     f"输入条件（条件之间用一个空格隔开），按回车退出程序。", end='')
#                 search_content = input('')
#                 if search_content == '':
#                     break
#                 # search_content = search_content.split()
#                 search_content = search_content.split(' ')
#                 set_path = set()
#                 for root, _, files in os.walk(self.folder_path):
#                     if files:
#                         for file_name in files:
#                             file_manipulate = FileOperations(os.path.join(root, file_name))
#                             self.identifying = True
#                             if file_manipulate.def_file_size > 3 * 1024 * 1024:
#                                 decide = input(
#                                     f"判断搜索文件:【{file_manipulate.file_path}】"
#                                     f", 大小为【{file_manipulate.def_file_output_size}】"
#                                     f", 请检查文件是否正常，直接回车跳过此文件搜索，输入任意按键并回车继续搜索"
#                                     f">>> ")
#                                 if decide == '':
#                                     self.identifying = False
#                             if self.identifying and not file_manipulate.def_file_filter_junk:
#                                 if file_manipulate.file_path.lower()[-5:] == ".docx":
#                                     if file_manipulate.def_docx_search_for_manipulate(search_content):
#                                         set_path.add(file_manipulate.file_path)
#                                 elif file_manipulate.file_path.lower()[-5:] == ".xlsx" \
#                                         or file_manipulate.file_path.lower()[-4:] == '.xls':
#                                     if file_manipulate.def_file_xlsx_xls_search_for_manipulate(search_content):
#                                         set_path.add(file_manipulate.file_path)
#                                 elif file_manipulate.file_path[-4:].lower() == ".txt":
#                                     if file_manipulate.def_txt_search_for_manipulate(search_content):
#                                         set_path.add(file_manipulate.file_path)
#                                 elif file_manipulate.file_path[-4:].lower() == ".csv":
#                                     if file_manipulate.def_csv_search_for_manipulate(search_content):
#                                         set_path.add(file_manipulate.file_path)
#
#                 if len(set_path):
#                     print(f'\n>>> 一共{len(set_path)}文件')
#                     for file_name in set_path:
#                         print(f'【{file_name}】')
#                 else:
#                     print(f"\n在路径【{self.folder_path}】中未找到含有【{' '.join(search_content)}】内容的文件")
#
#     @property
#     def def_folder_obtain_full_path(self):
#         """获取此文件夹目录的所有文件和文件夹"""
#         for root, dirs, files in os.walk(self.folder_path):
#             for file_name in files:
#                 file_manipulate = FileOperations(os.path.join(root, file_name))
#                 if file_manipulate.def_file_filter_junk:
#                     self.file_output_data.append(
#                         [file_manipulate.file_path, '文件', '无效', file_name])
#                 self.file_output_data.append(
#                     [file_manipulate.file_path, '文件', '有效', file_name])
#
#             for dir_name in dirs:
#                 dir_root_path = os.path.join(root, dir_name)
#                 if '.' == dir_name[:1]:
#                     self.file_output_data.append(
#                         [dir_root_path, '文件夹', '无效', dir_name])
#                 self.file_output_data.append(
#                     [dir_root_path, '文件夹', '有效', dir_name])
#             self.identifying = True
#         return self.identifying
#
#     def def_folder_obtain_full_path_print(self, path=None, depth=0, site=None):
#         """递归获取目录层级"""
#         if site is None and path is None:
#             site = []
#             path = self.folder_path
#
#         void_num = 0
#         filenames_list = os.listdir(path)
#
#         for item in filenames_list:
#             if '._' == item[:2]:
#                 continue
#             string_list = ["│   " for _ in range(depth - void_num - len(site))]
#             for s in site:
#                 string_list.insert(s, "    ")
#
#             if item != filenames_list[-1]:
#                 string_list.append("├── ")
#             else:
#                 # 本级目录最后一个文件：转折处
#                 string_list.append("└── ")
#                 void_num += 1
#                 # 添加当前已出现转折的层级数
#                 site.append(depth)
#             print("".join(string_list) + item)
#
#             new_item = path + '/' + item
#             if os.path.isdir(new_item):
#                 self.def_folder_obtain_full_path_print(new_item, depth + 1, site)
#             if item == filenames_list[-1]:
#                 void_num -= 1
#                 # 移除当前已出现转折的层级数
#                 site.pop()
#
#     def def_folder_obtain_full_path_save_xlsx(self, xlsx_path):
#         """获取文件夹下所有的文件、目录并输出到 xlsx 文件 """
#         if self.def_folder_obtain_full_path:
#             new_pd_file = pd.DataFrame(self.file_output_data)
#             new_pd_file.to_excel(xlsx_path, index=False, header=['路径', '类型', '是否有效', '名称'])
#             self.file_output_data = []
#             self.identifying = True
#         return self.identifying
#
#     def def_folder_remove_file_junk(self):
#         """删除垃圾文件"""
#         for root, _, files in os.walk(self.folder_path):
#             if files:
#                 for file_name in files:
#                     file_m = FileOperations(os.path.join(root, file_name))
#                     if file_m.identifying:
#                         if file_m.def_file_filter_junk_remove:
#                             print(f'删除 {file_m.file_path} 文件成功！')
