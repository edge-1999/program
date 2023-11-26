from tool.file_manager.file_operations.file_utils import validate_file_path, verify_individual_file_paths


@verify_individual_file_paths
def your_function(*args, **kwargs):
    # 函数内容
    print('执行函数')
