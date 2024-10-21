# set集合创建：使用{}来定义集合
# 不是序列类型了（有序、可重复、可索引、可切片，有的能修改、有的不能改变）
# set1 = {8,2,6,3,5,4,3,2}
# 特点：有序吗？无序；能重复嘛？自动去重复
# {2, 3, 4, 5, 6, 8}
# print(set1)

# 不能直接使用{}来定义set集合
# <class 'dict'>
set2 = {}
# set2 = {"allen"}
print(type(set2))
set1 = {8, 2, 6, 3, 5, 4, 3, 2}
set2 = {2, 3, 9, 4}

# {8, 5, 6}
print(set1 - set2)
print(set1 | set2)
print(set1 & set2)
