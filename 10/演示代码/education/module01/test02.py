# 同一目录下的导模块
from module01.test01 import student

def  func():
    print("这是一个func方法！！")

stu = student()
print(stu.add(12,23))