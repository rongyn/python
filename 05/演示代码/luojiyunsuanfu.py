# 逻辑运算符
# 主要是处理布尔类型数据（True和False），也可以有其他数据类型参与运算
# and 、or 、not
# 1、处理数据是布尔值的情况(掌握)
# and：逻辑与运算，参与与运算的两个运算数都为True则结果位True；否则位False
print(True  and  True)
print(True  and  False)
print(False  and  True)
print(False  and  False)

# or：逻辑或运算，参与或运算的两个运算数有一个位True则结果位True;否则位False（都为False）
print(True  or  True)
print(True  or  False)
print(False  or  True)
print(False  or  False)

# not: 逻辑非运算，非True即False，非False即True
print(not True)
print(not False)

# 结合关系运算和逻辑运算来使用
a = 12
b = 23
print((a<b) and  (a==12))

# 2、处理数据不是布尔值的情况(理解)
# and：如果and左侧的运算数是False,则结果是False；如果左侧不是False，则返回and右侧的值
print(True and 2)  #2
print(False and 4) #False
print(4 and 2) #2

# or:or左侧的运算数是True，则结果是True；左侧是False，则结果是右侧的值；如果左侧是非布尔值，则返回左侧的值
print(True or 2)  #True
print(False or 4) #4
print(4 or 2) #4

# not: 运算数是非布尔类型的话，非0当作True处理；0当作False处理
print(not 2)
print(not 0)
print(not {})