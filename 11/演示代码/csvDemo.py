# 注意：我们自己定义的py模块的名字不要叫做：csv.py
import csv

# 1、首先要打开文件
# as理解为重命名或者赋值
# with open(r"e:\allen.csv","r+",encoding="utf-8") as f:
#     # 读取数据：reader(csv文件对象)
#     data = csv.reader(f)
#     # <_csv.reader object at 0x00000239ABAA6880>
#     # 通过遍历从改地址中把数据提取出来
#     for d in data:
#         print(d[1])


# 2、写入文件
# newline=''，在输入完一行数据之后不再添加一个空行了
with open(r"e:\allen.csv","a+",encoding="utf-8",newline="") as f:
    # 写入的时候也是按照列表写入的，分隔符默认也是使用逗号
    data = ['1', 'allen1', '123456']
    # 创建一个写入对象
    writerCSV = csv.writer(f,dialect="excel")
    # writerow():写入一行数据
    # writerCSV.writerow(data)
    # writerCSV.writerows([data,data,data,data])
    data1 = [
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6]
    ]

    writerCSV.writerows(data1)