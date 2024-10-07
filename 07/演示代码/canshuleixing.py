# python调用函数时使用的参数方式
# 位置参数:定义函数时候的参数列表要和调用时候传递实际参数列表一致(个数和位置要一致)
# 1  传入的实际参数的个数和形参不一致,则报错,多了\少了都不行
# 2  如果传入的数据的顺序不一致,python无法监测,需要在代码中添加判断语句


# 需求:实现一个方法,参数待人用户名和性别,打印出这个用户名和性别
def printInfo(name,sex):
    # 需要传入1\2分别表示男女
    dict1 = {1:"先生",2:"女生"}
    # 对第二个参数sex的校验,校验他必须是一个整数
    # isinstance(sex,int):如果sex是int类型,则为True,否则False
    if isinstance(sex,int):
        print("hello %s %s,欢迎来到千锋软件测试课程!"%(name,dict1[sex]))
    else:
        print("请输入1和2的整数!!")
# 调用方法
# hello allen , 男,欢迎来到千锋软件测试课程!
# printInfo("allen","男")
# hello 男 , allen,欢迎来到千锋软件测试课程!
# printInfo("男","allen")
# printInfo() missing 1 required positional argument: 'sex'
# printInfo("allen")
# printInfo() takes 2 positional arguments but 3 were given
# printInfo("allen",1,2)
# hello allen 先生,欢迎来到千锋软件测试课程!
# printInfo("allen",1)
# KeyError: 'allen'
# 请输入1和2的整数!!
# printInfo(1,"allen")
# printInfo("allen",2)


# 关键字参数:就是把形式参数的参数名作为一种标识,传递实际参数的时候绑定这个表示
# 可以不用管实际参数的顺序问题了
# 都是用关键字传参是可以的
# 前面是位置参数,后面跟一些关键字参数是可以的
# 前面是关键字,后面是位置则不允许
# 同一个参数位置,不允许给多个值



# hello allen 先生,欢迎来到千锋软件测试课程!
# printInfo(name="allen",sex=1)
# hello allen 先生,欢迎来到千锋软件测试课程!
# printInfo(sex=1,name="allen")
# hello allen 先生,欢迎来到千锋软件测试课程!
# printInfo("allen",sex=1)
# positional argument follows keyword argument
# 位置参数不允许放在关键字参数的后面
# printInfo(name="allen",1)
# 位置参数不允许放在关键字参数的后面
# printInfo(sex=1,"allen")
# printInfo() got multiple values for argument 'name'
# name这形式参数拿到两个数据
# printInfo(1,name="allen")



# 默认值参数:在定义函数的时候，给某些参数直接指定值，调用的是是可以不给该参数传数据的。
# 在定义的时候要传一次值
# 默认值参数的值定义为不可变的数据类型

# 需求：维护学生信息表，给学生追加信息：姓名、年龄、校区
listS = []
def studentInfo(name,age,school="北京"):
    listS.append(name)
    listS.append(age)
    listS.append(school)
# ['allen', 28, '北京']
# studentInfo("allen",28,"北京")
# studentInfo("Lucy",23,"北京")
# studentInfo("lily",24,"北京")
# ['allen', 28, '北京', 'Lucy', 23, '北京', 'lily', 24, '北京']
# ['allen', 28, '北京', 'Lucy', 23, '西安', 'lily', 24, '深圳']
studentInfo("allen",28)
studentInfo("Lucy",23,"西安")
studentInfo("lily",24,"深圳")
print(listS)
# end='\n':是不是一种默认值参数的使用？
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# print("aaaa",end="\t")

# 不定长参数
# 实现求和运算的方法：2个数的求和、3个数的求和........
# 实现的方法的参数个数是不固定，借助*args、**kwargs
# def sum1(a,b):
#     return a+b

# def sum2(a,b,c):
#     return a+b+c

# def sum3(a,b,c,d):
#     return a+b+c+d

# *args会接受多个实际的参数值，把接受的数据放在一个元组中，可用读取这个元组的数据进行处理即可
# 实现大于2个数据的求何运算

def sum(a,b,*args):
    # result = 0
    # print(args)
    result = a+b
    for i in args:
        result += i
    return result
#  ()
# sum(1,2)
# (3, 4, 5, 6, 7, 8)
# 36
# print(sum(1,2,3,4,5,6,7,8))
# print(sum(4,5,6,7,8))
# print(sum(2,3))


# **kwargs:也是用于接受多组实际参数值的变量，必须使用关键字进行传递实际参数
# 实现大于2个数据的求何运算
def sum1(a,b,**kwargs):
    # print(kwargs)
    result = a+b
    for i in kwargs:
        result += kwargs[i]
    return result
# takes 2 positional arguments but 3 were given
# {'c': 3}
# sum1(a=1,b=2,c=3)
# sum1(1,2,c=3)
print(sum1(1,2,c=3,d=4,e=5))