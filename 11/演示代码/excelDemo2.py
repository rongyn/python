# 实现往excel中写入数据
# 使用xlwt的模块：pip install xlwt

# 1、导包
import xlwt

# 2、打开excel工作簿文件
f = xlwt.Workbook(encoding = "utf-8")

# 3、指定写入数据的sheet页
sheet = f.add_sheet("allen")

# 4、写入第二行第二列中
# sheet.write(行索引，列索引，值)
# sheet.write(1,1,"你好")
# 如何写入一行数据呢
# rowData = ["name","password","id","address"]
# 遍历一行中列的索引号col
# for col in range(0,len(rowData)):
#     sheet.write(0,col,rowData[col])

# 写入多行数据
rowData = [
    ["name","password","id","address"],
    ["name1","password1","id1","address1"],
    ["name2","password2","id","address2"],
    ["name3","password3","id","address3"]
]

row = len(rowData)
for r in range(0,row):
    for c in range(0,len(rowData[r])):
        sheet.write(r,c,rowData[r][c])

# 5、写完之后别忘了保存文件(将内存中的数据写入到文件中)
f.save(r"e:\allen.xls")