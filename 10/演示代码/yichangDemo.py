# 索引越界
# list01 = [1,2,3,4,5,6]
# print(list01[1])
# print(list01[6])

# 除数不能为0异常
# print(1/0)

# KeyboardInterrupt
# while True:
#     print("hello world !!")

# a  = None
# AttributeError: 'NoneType' object has no attribute 'add'
# print(a.add())

# ModuleNotFoundError: No module named 'test04'
# import test04

# 预测下面的代码会出现索引越界的问题
from logging import exception


try:  #对try代码块中的语法进行监测
    list01 = [1,2,3,4,5,6]
    print(list01[1])
    print(list01[6])
    # print(1/0)
    # except是抓取异常信息
    # 有抛出错误，我们自己解决了
# except IndexError as e:
#     print("此处出现了索引越界的异常了，请检查上面的代码，我先往后运行了！！")
#     print(e)
# except ZeroDivisionError as z:
#     print(z)
# 不确定到底会抛出哪一个异常
# Exception能够抓到除数为0的异常

except Exception as e:
    print(e)
finally:
    print("不管你走的是try，还是except，最终都要运行这一句！")

print("我是后续的代码")