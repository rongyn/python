# 在python的使用中，存在需要将一些数据转换为其他类型的场景。
# 只需要使用该数据类型作为方法名使用即可转化。
# 方法名有：int(str)、str(其他类型)、list(其他类型)、tuple(其他类型)等
# input():是可以将键盘录入的数据转为python字符串格式
# 1、需求：希望将键盘录入的数据转换数据类型为整性数据（int）
# 处理方式：直接使用int作为方法名转换即可，int(str字符串)
# str字符串:必须是数字类型的字符串，"1233",'222'
# ValueError: invalid literal for int() with base 10: 'ab'
# age = int(input("请输入你的年龄："))
# # <class 'str'>
# print(type(age))
# # TypeError: %d format: a number is required, not str
# print("我的年龄是：%d"%age)

# 2、str(其他类型)：将其他数据类型转为字符串
# 将整数转为字符串
student_id = str(12345)
print(type(student_id))

# 将列表转为字符串
student_name = str(["allen","lucy","李雷","韩梅梅"])
print(type(student_name))
print(student_name)

# 将元组转为字符串？（课后练习）

# 3、eval():将一个字符串表达式转为对象
# "print('hello world')"  ---> print('hello world')
str1 = "print('hello world')"
eval(str1)

# 4、list():将其他类型序列转为列表
str2 = "abcdefg"
list1 = list(str2)
print(type(list1))
print(list1)

tuple1 = (1,2,3,4,5)
list2 = list(tuple1)
print(type(list2))
print(list2)

# 5、字符串和列表转元组的方法（tuple()）--课下练习
# 6、dict():将一个元组转为字典
# {'name': 'allen', 'name1': 'allen1'}
dict1 = dict([("name","allen"),("name1","allen1")])
print(type(dict1))
print(dict1)