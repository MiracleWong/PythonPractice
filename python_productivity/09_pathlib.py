import pathlib
import configparser

base_dir = 'E:/Projects/PythonPractice/python_productivity/'
#base_dir = '/Users/miraclewong/'
keywords = '**/*BBC*'

path = pathlib.Path(base_dir)

files = path.glob(keywords)
print(list(files))

files2 = path.rglob('*.xlsx')
print(list(files2))

# 遍历子目录和所有文件
files3 = path.glob('**/*')
print(list(files3))
