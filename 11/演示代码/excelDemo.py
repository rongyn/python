# 打开allen.xlsx
# 导入读取excel文件的模块（xlrd=2.0.1，支持的是xls文件）
from os import set_inheritable
import xlrd
# 1、定义一个文件对象，打开excel工作簿
# xlrd.biffh.XLRDError: Excel xlsx file; not supported
# f = xlrd.open_workbook(r"e:\allen.xlsx")
# <xlrd.book.Book object at 0x000001F240EF5D90>
f = xlrd.open_workbook(r"e:\allen.xls")
# 2、选择工作簿中的一个sheet页，获取其中的表格数据
# sheet_by_index:按照sheet页的索引获取，从0开始
# Sheet  0:<Sheet1>
# sheet1 = f.sheet_by_index(0)
# Sheet  0:<allen>
sheet1 = f.sheet_by_name("allen")
# sheet1  =  f.sheets()[1]

# 3、获取sheet1中单元格数据(第二行第二列)
# [1.0, 'allen1', 123456.0]
# rowData = sheet1.row_values(1)
# 获取单元格数据
# print("第二行第二列数据为:%s"%rowData[1])
# cell_value(行索引号,列索引号)，索引号都是从0开始的
# cellData = sheet1.cell_value(1,1)
# print("第二行第二列数据为:%s"%cellData)

# 4、遍历获取所有的数据（所有行和所有单元格）
# 前提是知道sheet1中表有多少行多少列
# sheet1.nrows：返回sheet1的行数的字段
# sheet1.ncols：返回sheet1的列数的字段
rows = sheet1.nrows
cols = sheet1.ncols
# i就是行号的索引（第一行的索引就是0）
# for i in range(0,rows):
#     data = sheet1.row_values(i)
#     print(data[1])

# 所有单元格
for n in range(0,rows):
    for m in range(0,cols):
        data = sheet1.cell_value(n,m)
        print(data)