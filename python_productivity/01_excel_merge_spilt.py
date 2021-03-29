from pathlib import Path, PurePath
import xlrd
import xlwt

src_path = '/Users/miraclewong/github/PythonPractice/python_productivity/调查问卷'
dst_file = '/Users/miraclewong/github/PythonPractice/python_productivity/result/结果.xlsx'
p = Path(src_path)
files = [x for x in p.iterdir() if PurePath(x).match("*.xlsx")]

content = []

for file in files:
    username = file.stem
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    answer1 = table.cell_value(rowx=4, colx=4)
    answer2 = table.cell_value(rowx=10, colx=4)
    temp = f'{username},{answer1},{answer2}'
    content.append(temp.split(","))
    print(temp)

table_header = ['员工姓名', '第一题', '第二题']
workbook = xlwt.Workbook(encoding='utf-8')
xlsheet = workbook.add_sheet("统计结果")

row = 0
col = 0

for cell_header in table_header:
    xlsheet.write(row, col, cell_header)
    col += 1

row += 1

for line in content:
    col = 0
    for cell in line:
        xlsheet.write(row, col, cell)
        col += 1

    row += 1

workbook.save(dst_file)
