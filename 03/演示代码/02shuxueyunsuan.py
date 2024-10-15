# 导入math模块
import math
import random
# 取绝对值
a = 100
b = -100
print(abs(b))

# math模块，提供数学运算的方法
# ceil:取比浮点数大的最近的整数功能
c = 1.23
print(math.ceil(c))

# floor:取比浮点数小的最近的整数功能
print(math.floor(c))

# pi:圆周率的常量
print(math.pi)

# 生成一个随机整数
# randint: (a: int, b: int)
# 生成的数据在100到999之间，是可以包括100和999的。
randNum = random.randint(100,999)
print(randNum)
