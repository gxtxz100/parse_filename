import os
import re

def parse_filename(filename):
    """解析文件名，提取主编号和副编号"""
    # 使用正则表达式提取主编号（数字部分）
    main_match = re.search(r'^(\d+)', filename)
    main_number = int(main_match.group(1)) if main_match else 0

    # 使用正则表达式提取副编号（文件名中的第二部分数字）
    sub_match = re.search(r'\.(\d+)', filename)
    sub_number = int(sub_match.group(1)) if sub_match else 0

    return (main_number, sub_number)

def list_and_sort_files_in_directory(directory_path):
    # 检查目录是否存在
    if not os.path.exists(directory_path):
        print("提供的目录不存在，请检查路径。")
        return

    # 确保提供的路径是一个目录
    if not os.path.isdir(directory_path):
        print("提供的路径不是一个目录。")
        return

    # 获取目录中的所有文件名
    file_names = os.listdir(directory_path)

    # 过滤掉子目录，只保留文件
    file_names = [file for file in file_names if os.path.isfile(os.path.join(directory_path, file))]

    # 根据文件名中的数字进行排序
    sorted_file_names = sorted(file_names, key=parse_filename)

    # 将排序后的文件名写入到txt文件中
    with open('sorted_file_names.txt', 'w', encoding='utf-8') as file:
        for name in sorted_file_names:
            file.write(name + '\n')

    print(f"排序后的文件名已保存到 'sorted_file_names.txt'。")

# 用户输入文件夹地址
directory_path = input("请输入文件夹地址：")
list_and_sort_files_in_directory(directory_path)