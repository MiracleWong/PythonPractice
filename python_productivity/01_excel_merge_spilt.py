from pathlib import Path, PurePath
import xlrd
import xlwt

src_path = '/Users/miraclewong/github/PythonPractice/python_productivity/调查问卷'
# dst_file = '/Users/miraclewong/github/PythonPractice/python_productivity/result/结果.xlsx'
dst_path = '/Users/miraclewong/github/PythonPractice/python_productivity/工资单/工资单.xlsx'

p = Path(src_path)
files = [x for x in p.iterdir() if PurePath(x).match("*.xlsx")]


# for file in files:
#     username = file.stem
#     data = xlrd.open_workbook(file)
#     table = data.sheets()[0]
#     answer1 = table.cell_value(rowx=4, colx=4)
#     answer2 = table.cell_value(rowx=10, colx=4)
#     temp = f'{username},{answer1},{answer2}'
#     content.append(temp.split(","))
#     print(temp)
#
# table_header = ['员工姓名', '第一题', '第二题']
# workbook = xlwt.Workbook(encoding='utf-8')
# xlsheet = workbook.add_sheet("统计结果")
#
# row = 0
# col = 0
#
# for cell_header in table_header:
#     xlsheet.write(row, col, cell_header)
#     col += 1
#
# row += 1

# for line in content:
#     col = 0
#     for cell in line:
#         xlsheet.write(row, col, cell)
#         col += 1
#
#     row += 1


def get_excel(src_file):
    data = xlrd.open_workbook(src_file)
    table = data.sheets()[0]
    return table


# 定义写入文件的函数
def write_to_file(filename, cnt):
    """
    filename : 写入的文件名
    cnt      : 写入的内容
    """
    workbook = xlwt.Workbook(encoding='utf-8')
    xlsheet = workbook.add_sheet("本月工资")

    row = 0
    for line in cnt:
        col = 0
        for cell in line:
            xlsheet.write(row, col, cell)
            col += 1
        row += 1
    paths = ["python_productivity", "工资单"]
    workbook.save(Path.cwd().parent.with_name(filename).with_suffix('.xlsx'))
    # workbook.save(PurePath(dst_path).with_name(filename).with_suffix('.xlsx'))


def split_excel(src_file):
    table = get_excel(src_file)
    employee_numbers = table.nrows
    salary_header = table.row_values(rowx=0, start_colx=0, end_colx=None)
    for line in range(1, employee_numbers):
        content = table.row_values(rowx=line, start_colx=0, end_colx=None)
        new_content: list = [salary_header, content]
        write_to_file(filename=content[1], cnt=new_content)


if __name__ == '__main__':
    split_excel("工资单/工资单.xlsx")