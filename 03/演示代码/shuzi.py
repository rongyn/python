# 定义一个整数变量
age = 288888888888888888888888888888888888888888888888888888888
print(age)


# 定义一个浮点数变量
a = 1.23
pi = 3.14159261234567891234
b = 2e3   # 科学表示法，相当于2*10^3
c = 2e-3   # 科学表示法，相当于2*10^-3
# print("a的值为：%f"%a)
# print("pi的值为：%f"%pi)
# print("b的值为：%f"%b)

# 默认精确度，保留17位有效数字
print(a)
print(pi)
print(b)

# 定义一个复数
fushu = 1+2j
print(fushu)

# <class 'int'>
print(type(age))
# <class 'float'>
# python中数据类型也是类，一切皆是对象
print(type(pi))
# <class 'complex'>
print(type(fushu))
