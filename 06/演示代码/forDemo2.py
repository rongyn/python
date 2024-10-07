# 迭代数据类型：字符串、列表、元组、字典、集合和range()
# 实现遍历（把元素一个个地取出来）数据类型的元素
# 对于i遍历的理解：1-控制循环次数、2-获取元素值
# 1、遍历字符串
# for i in "allen":
#     print(i)

# 2、遍历列表（熟练掌握）
list1 = ["a","b","c","d"]
# for i in list1:
#     print(i)
#     a=12
#     b=23
#     c=a+b
#     print(c)

# for j in [1,2,3,4,5,6]:
#     print(j)

# 3、遍历元组（自己完成练习）、集合
# for i in {1,2,3,4,5}:
#     print(i)

# 4、遍历字典（熟练掌握）
userInfo = {"username":"allen","password":"123456"}
# 直接遍历字典名，默认获取的是键
# 有了键能不能拿到值
# for ui in userInfo:
#     print(ui)
#     print(userInfo[ui])


# for key in userInfo.keys():
#     print(key)

# for value in userInfo.values():
#     print(value)

# for item in userInfo.items():
#     # ('username', 'allen')
#     print(item[0])
#     print(item[1])


# range遍历（熟练掌握）
# 专门的方式控制循环的次数或者顺序的数据--range(start,end,step=1) 左闭右开
# range(0,100),按照指定的范围生成一个序列数据
# range(0,9):表示0，1，2，3，4，5，6，7，8所组成的数据类型
# range(0,9,2):表示0，2，4, 6，8所组成的数据类型
# for i in range(0,9,2):
#     print(i)

# 采range()实现循环100次，怎么写？
# 控制台输出100次hello world
for i in range(1,101):
    print("hello world !!!!!"+str(i))