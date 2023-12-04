import yaml, os

# 获取当前文件路径：
# current_path = os.getcwd()
# current_pat =os.path.dirname(os.path.abspath(__file__))
# print(current_path)
# # 获取当前脚本所在的项目根目录
# root_path = os.path.dirname(current_path)
# print("项目根目录路径：", root_path)

def read_data(file_name):
    file_path = os.path.dirname(os.getcwd()) + os.sep + 'Data' + os.sep + file_name + '.yaml'
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

# read_data('data')

