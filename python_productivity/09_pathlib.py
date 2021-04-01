import pathlib
import configparser

# base_dir = 'E:/Projects/PythonPractice/python_productivity/'
# #base_dir = '/Users/miraclewong/'
# keywords = '**/*BBC*'
#
# path = pathlib.Path(base_dir)
#
# files = path.glob(keywords)
# print(list(files))
#
# files2 = path.rglob('*.xlsx')
# print(list(files2))
#
# # 遍历子目录和所有文件
# files3 = path.glob('**/*')
# print(list(files3))

def read_dirs(ini_filename, section, arg):
    """
    通过ini文件，节和参数的取得要操作多个目录
    """
    current_path = pathlib.PurePath(__file__).parent
    inifile = current_path.joinpath(ini_filename)

    # 创建实例
    cf = configparser.ConfigParser()

    # 读取.ini文件
    cf.read(inifile)

    return cf.get(section, arg).split(",")


def locate_file(base_dir, keywords):
    p = pathlib.Path(base_dir)
    files = p.glob(keywords)
    return list(files)

if __name__ == '__main__':
    dirs = read_dirs('search.ini', 'work', 'searchpath')
    keywords = '**/*BBC*'

    result = []
    for dir in dirs:
        files = locate_file(dir, keywords)
        result += files

    print([str(r) for r in result])
