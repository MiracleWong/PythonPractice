import xlwt
import xlrd

file = '/Users/miraclewong/github/PythonPractice/python_productivity/result/结果.xlsx'
dst_file = '/Users/miraclewong/github/PythonPractice/python_productivity/result/结果1.xlsx'

data = xlrd.open_workbook(file)
table = data.sheets()[0]
value = table.cell_value(rowx=0, colx=0)

workbook = xlwt.Workbook(encoding="utf-8")
xlsheet = workbook.add_sheet("统计结果")

xlsheet.write(0,0, value)
workbook.save(dst_file)
