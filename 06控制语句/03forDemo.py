# print("hello world !!!")
# print("hello world !!!")
# print("hello world !!!")
# print("hello world !!!")
# print("hello world !!!")
# print("hello world !!!")
# print("hello world !!!")
# print("hello world !!!")
# print("hello world !!!")
# print("hello world !!!")

# 循环结构解决重复代码执行的现象（场景）-for循环
# for循环：比较确定循环次数的用法，把helloworld输出10遍
# 迭代数据类型：字符串、列表、元组、字典、结合和range()
# for循环的次数取决于迭代数据类型的长度(元素个数)
# for 变量 in 迭代数据类型：
#      for循环代码块    

# 代码的执行逻辑：
# 第一次循环：i取字符串中的第一个元素0，并赋值给i，执行代码块，执行代码块之后，再回到for i位置
# 第二次循环：i取字符串中的第二个元素1，并赋值给i，执行代码块，执行代码块之后，再回到for i位置
# 第三次循环：i取字符串中的第三个元素2，并赋值给i，执行代码块，执行代码块之后，再回到for i位置
# 。。。。
# 第十次循环：i取字符串中的第十个元素9，并赋值给i，执行代码块，执行代码块之后，再回到for i位置
# 第十一次循环：i又想取字符串中取值，发现没了 ，就不再进入代码块执行了，直接结束了for循环。
# 1、for的第一种语法结构（掌握）
for i in "0123456789":
    # print("hello world")
    print(i)

# 2、for的第二种结构
# for i in "0123456789":
#     # print("hello world")
#     print(i)
# else:
#     print(i)
