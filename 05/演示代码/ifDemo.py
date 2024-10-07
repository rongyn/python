# 1、通过键盘输入一个成绩，判断有没有及格
# score变是成绩的变量
# score = int(input("请输入你的考试成绩："))
# if(score>=60):
#     # if代码块
#     print("及格了！！！")
#     print("及格了！！！")
#     print("及格了！！！")
#     print("及格了！！！")

# # 此处的代码就和if语句没有任何关系了
# print("关我啥事！！！")

# 2、键盘输入一个成绩，判断是及格还是不及格呢？
# score = int(input("请输入你的考试成绩："))
# if(score>=60):
#     print("我及格了！！！！")
# else:
#     print("坏菜了，没考及格！！！")

# # 此处的代码就和if语句没有任何关系了
# print("关我啥事！！！")

# 3、还是输入一个成绩，判断你的成绩等级是：优（>=90,<=100）良(>=80)中(>=60)差(<60,>0)
# score大于等于90、小于等于100的两种写法
# 90<=score<=100
# score>=90 and score<=100
# 给成绩95，45
# 使用if-elif-..-else的效率要大于等于多个if语句的组成
# score = int(input("请输入你的考试成绩："))
# if(90<=score<=100):
#     print("成绩位优秀")
# elif(score>=80 and score<90):
#     print("成绩为良好")
# elif(score>=60 and score<80):
#     print("成绩为中等")
# elif(score>=0 and score<60):
#     print("成绩为不及格")
# else:
#     print("你输入的数据不再成绩范围内！！")

# if(90<=score<=100):
#     print("成绩位优秀")
# if(80<=score<90):
#     print("成绩位优秀")
# if(60<=score<80):
#     print("成绩位优秀")
# if(0<=score<60):
#     print("成绩位优秀")


# 输入一个数字，判断是否被2、3整除的效果
# 采用if嵌套语句
data = int(input("请输入一个整数"))
if(data%2==0):
    if(data%3==0):
        print("data是可以被2和3同时整除！")
    else:
        print("data是可以被2整除，但是不能被3整除！")
else:
    if(data%3==0):
        print("data是可以被3整除，但是不能被2整除")
    else:
        print("data既不能被2整除，也不能被3整除！")