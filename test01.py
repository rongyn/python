# L = ['apple', 'pear', 'banana', 'orange', 'grape']
# L.append('peach')
# print(L)
#
# L1 = [1, 2, "A", "B"]
# L.append(L1)
# print(L)
#
# L.insert(0, 'fruit:')
# print(L)
#
# print(len(L))
import random


# L.pop()
# print(L)
# del L[-1]
# print(L)
#
# del L[4]
# print(L)
#
# L[6].remove("A")
# print(L)
#
# L2 = [2, 1, 4, 5, 4]
# L2.sort()
# print(L2)
# print(max(L2))
# print(min(L2))
# # print(L2[::-1])
# L2.reverse()
# print(L2)
#
# dt = {"name": "zhangsan", "password": "123456"}
# dt["iphone"] = "123123123"
# print(dt)
#
# print(dt.keys())
#
# print(dt.values())
#
# print(dt.items())
#
# dt.pop("iphone")
# print(dt)


# score = int(input("请输入成绩:"))
# if score >= 90:
#     print("A")
# elif score >= 80 and score <= 89:
#     print("B")
# elif score >= 70 and score <= 79:
#     print("C")
# elif score >= 60 and score <= 69:
#     print("D")
# else:
#     print("E")
#
# a = int(input("请输入数字a:"))
# b = int(input("请输入数字b:"))
# c = int(input("请输入数字c:"))
# if a > b:
#     if a > c:
#         print("a最大:%d" % a)
#     else:
#         print("c最大:%d" % c)
# else:
#     if b > c:
#         print("b最大:%d" % b)
#     else:
#         print("c最大：%d" % c)


# for i in range(1,11):
#     print(i)

# 错误：for i in range(10, 1):
#     print(i)
# 正确：for i in range(10, 0, -1):
#     print(i)

# sum1 = 0
# for i in range(1, 11):
#     sum1 += i
# print(sum1)

# sum1 = 0
# for i in range(0, 11, 2):
#     sum1 += i
# print(sum1)
#
# # 99：
# for h in range(1, 10):
#     for l in range(1, 10):
#         if (l < h):
#             print("%d*%d=%d" % (l, h, l * h), end="\t")
#     print()


# # 冒泡
# list1 = [2, 1, 6, 7, 2, 9]
# for i in range(0, len(list1) - 1):
#     for j in range(0, len(list1) - 1):
#         if (list1[j] >= list1[j + 1]):
#             temp = list1[j]
#             list1[j] = list1[j + 1]
#             list1[j + 1] = temp
# print(list1)


# randomnum = random.randint(1, 101)
# count = 0
# while True:
#     guessnum = int(input("请输入一个1-100的数字："))
#     count += 1
#     if guessnum > randomnum:
#         print("大了")
#     elif guessnum < randomnum:
#         print("小了")
#     else:
#         print("你猜对了，猜了%d次" % count)

# 公鸡5文钱一只,母鸡3文钱一只,小鸡3只一文钱，用100文钱买一百只鸡，其中公鸡,母鸡,小鸡都必须要有，问公鸡,母鸡，小鸡要买多少只刚好凑足100文钱。
# numg = 0
# numm = 0
# nums = 0
#
# while numg <= 20:
#     while numm <= 33:
#         nums = 100 - numg - numm
#         if nums % 3 == 0:
#             total = 5 * numg + 3 * numm + nums // 3
#             if total == 100:
#                 print(f"g:{numg},m:{numm},s:{nums}")
#         numm += 1
#     numm = 0
#     numg += 1
#
# # 初始化变量
# cock = 0  # 公鸡数量
# hen = 0  # 母鸡数量
# chick = 0  # 小鸡数量

# # 开始穷举
# while cock <= 20:  # 公鸡最多可以买20只（5文钱一只，最多100文钱）
#     while hen <= 33:  # 母鸡最多可以买33只（3文钱一只，最多99文钱）
#         chick = 100 - cock - hen  # 小鸡数量 = 100 - 公鸡数量 - 母鸡数量
#
#         # 检查小鸡数量是否为正整数，并且每只小鸡3只一文钱，即小鸡数量必须是3的倍数
#         if chick % 3 == 0:
#             # 计算总花费
#             total_money = 5 * cock + 3 * hen + chick // 3
#
#             # 检查总花费是否为100文钱
#             if total_money == 100:
#                 print(f"公鸡: {cock}只, 母鸡: {hen}只, 小鸡: {chick}只")
#
#                 # 增加母鸡数量
#         hen += 1
#
#         # 重置母鸡数量，增加公鸡数量
#     hen = 0
#     cock += 1


# 使用python中的下面技术实现功能
# 1.使用列表存储学员信息(姓名)
# 2.对列表进行增、删、改、查
# 3.通过input方法输入信息
# 4.通过if语句判断选项菜单(比如1表示增加新学员功能)
# 5.每次增删改后都要求实现一次查询显示
# 6.将代码封装一个死循环中(如果选择了5菜单，则终止死循环)
# ==============学员管理菜单:================
# 1-增加新学员 2-更新 3-删除学员 4-查询 5-退出
# ==============学员管理菜单:================
# NameList = ["小王"]
# while True:
#     print("==============学员管理菜单:================")
#     print("1-增加新学员 2-更新 3-删除学员 4-查询 5-退出")
#     print("==============学员管理菜单:================")
#     choicenum = int(input("please choice this number（1-5）:"))
#
#     if choicenum == 1:
#         print("----------------增加新学员----------------------")
#         name = input("请输入新增学员的姓名：")
#         NameList.append(name)
#         print("增加后的学员名单：%s" % NameList)
#         print("-----------------------------------------------")
#     elif choicenum == 2:
#         print("----------------更新名字----------------------")
#         oldname = input("请输入已有的名字：")
#         newname = input("请输入新名字：")
#         NameList[NameList.index(oldname)] = newname
#         print("更新结果：%s" % NameList)
#     elif choicenum == 3:
#         print("----------------删除名字----------------------")
#         delname = input("请输入要删除的名字：")
#         NameList.remove(delname)
#         print("最新学员：%s，已删除：%s" % (NameList, delname))
#     elif choicenum == 4:
#         print("----------------查询名字----------------------")
#         print("查询结果：%s" % NameList)
#     elif choicenum == 5:
#         print("已退出")
#         break
#     else:
#         print("请输入正确序列：1-增加新学员 2-更新 3-删除学员 4-查询 5-退出")

# 阶乘5*4*3*2*1
# jiecheng = 1
# i = [5, 4, 3, 2, 1]
# for j in i:
#     jiecheng *= j
#     print(jiecheng)
# print(jiecheng)


def display_message():
    print("我学到了定义函数和调用")


display_message()


def favorite_book(title):
    print("one of my favorite books is %s" % title)


favorite_book("Alice in Wonderland")


