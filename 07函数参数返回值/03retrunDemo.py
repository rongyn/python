# return语句
# 用于结束函数，有选择地给调用者返回一个表达式（值）
# 一个方法中可以有return、也可以不带
# 如果有的话，这个返回的值一定是经果分析确定
# 第一种写法
# def sum(a,b):
#     return a+b
# # 第二种写法
# def sum(a,b):
#     c = a+b

# 第三种写法
def sum(a, b):
    return a, b, a + b
    # 下面的这个print()永远不会执行到
    print("aaa")


# 这个地方就是调用者的位置,把方法的返回值赋值给了变量result
# 如果没写return，返回None
# return不仅仅能返回一个值，还可以返回多个值，多个值是呗封装在了一个元组中返回
# (2, 3, 5)
result = sum(2, 3)
print(result)
