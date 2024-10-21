tuple1 = (1, 2, 3, 4, 5, 2)
# 元组是有序的,元组中的数据是可以重复的
# print(tuple1)
print(tuple1[1])
print(tuple1[:])
print(tuple1[::-1])
# 元组不能被修改: 'tuple' object does not support item assignment
# tuple1[0] = 10
# 元组定义的小括号中至少有一个逗号
tuple2 = (12,)
# <class 'tuple'>
print(type(tuple1))
# <class 'int'>
print(type(tuple2))

tuple3 = (1, 2, 3, [4, 5], 6)
tuple3[3][0] = 9
print(tuple3)
tuple3[3] = [8, 8]
print(tuple3)
