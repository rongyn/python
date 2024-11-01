# 6.求5的阶乘
# 阶乘：jiecheng = 5*4*3*2*1
# str1 = "54321"
# jiecheng = 1
# for i in str1:
#     jiecheng *= int(i)
# print(jiecheng)
# 做乘法的话，乘积变量初始化1，不能是0
# 做加法的话，和变量的初始化0，不能是1
# list1 = [5,4,3,2,1]
# jiecheng = 1
# for i in list1:
#     jiecheng *= i
# print(jiecheng)

# 上面的两种写法不是很方便，而且效率低一些，range()
# jiecheng = 1
# for i in range(5, 0, -1):
#     jiecheng *= i
# print(jiecheng)

# 对于一个四位的整数，倒序输出其每一位上的数字。例如，一个整数3421，分别显示和输出：1,2,4,3。
zhengshu = int(input("输入四位整数："))
# 最好将该整数转为字符串
str1 = str(zhengshu)
# str1[::-1]
for i in str1[::-1]:
    print(i)
# list1 = list(str1)
# reverse:反转列表
# list1.reverse()
# for i in list1:
#     print(i)

# 9、百钱买百鸡(掌握)
# 公鸡5钱一只，母鸡3钱一只，小鸡1钱3只。问100钱买100只鸡，分别怎么购买。
# 买公鸡x只、母鸡y只、小鸡z只，x+y+z==100 and 5*x + 3*y+ z/3 == 100
# 第一层循环来控制公鸡数量
# for x in range(0,21):
#     # 第二层控制买母鸡的数量
#     for y in range(0,34):
#         # 第三层控制买小鸡的数量
#         for z in range(0,101):
#             if(x+y+z==100 and 5*x + 3*y+ z/3 == 100):
#                 print("买%2d只公鸡、%2d只母鸡、%2d只小鸡，可以满足要求。"%(x,y,z))

# 在控制台输出所有的”水仙花数”(掌握)
# 指一个三位数，其各位数字的立方和等于该数本身。
# 先搞出一个三位数：100，999--234
# a  = 234
# bai = a//100
# shi = a//10%10
# ge = a%10
# bai**3 + shi ** 3 + ge ** 3==a
# count = 0
# for a in range(100,1000):
#     bai = a//100
#     shi = a//10%10
#     ge = a%10 
#     if(bai**3 + shi ** 3 + ge ** 3==a):
#         print("水仙花数为:"+str(a))
#         count += 1
# print("水仙花数总共有：%d个 。"%count)


# 1、获取100~999的整数
# 2、将整数转为字符串
# 3、循环遍历字符串，得出个十百位上的数字
# count = 0
# for a in range(100,1000):
#     # 获得个十百位数字的立方和的变量
#     he = 0
#     for i  in str(a):
#         he += int(i)**3
#     if(he==a):
#         print("水仙花数为:"+str(a))
#         count += 1
# print("水仙花数总共有：%d个 。"%count)
