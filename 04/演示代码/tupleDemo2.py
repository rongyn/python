# tuple1 = (1,2,3,4,5,["a","c"],6,7)
# 把1改为10: 'tuple' object does not support item assignment
# tuple1[0]=10

# 把["a","c"]中的"a"改为d。
# tuple1[5][0] = "d"
# (1, 2, 3, 4, 5, ['d', 'c'], 6, 7)
# 能不能换掉["a","c"]
# tuple1[5] = ["1",2]


tuple1 = (1,2,3,4,5,["a","c"],6,7)
tuple2 = (1,2,3,4,5)
print(tuple1+tuple2)
print(tuple2*2)
print(1 in tuple1)
print(tuple1)

# 第一个元组的长度(元素的个数)
print(len(tuple1))
print(max(tuple2))
print(min(tuple2))
print(tuple1.index(2))
print(tuple1.index(["a","c"]))
print(tuple1.count(1))
