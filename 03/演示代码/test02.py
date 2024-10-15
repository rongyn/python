# 使用一个print方法，结合input和print多行数据。
# print()的使用
# input()的使用
# 占位符格式化输出
# \n换行的使用
# 多行字符串显示
# print("=================================\n\
# 姓名：%s\n\
# 职位：%s\n\
# 公司地址：%s\n\
# ====================================="%(input("输入姓名："),input("输入岗位："),input("输入公司地址：")))



# 补充：字符串特有find方法，功能上和index相似
str1 = "ABCDEFG"
# index是序列的通用方法，再列表和元组中也能用
# find方法只能在字符串中用
# print(str1.index("C"))
# # ValueError: substring not found,导致代码终止运行了
# print(str1.index("m"))
# print(str1.index("A"))

# S.find(sub[, start[, end]]) 
print(str1.find("C"))
# "m"不在大串中,不报错，返回-1值
print(str1.find("m"))
print(str1.find("A"))


