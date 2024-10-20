# 已知字典dt = {"name":"zhangsan","password":"123456"}
# 键的特点：不能重复、无序，列表能作为键嘛,
# 字典的元素组成：key：value（键值对）
# unhashable type: 'list'
# dict1 = {[1,2,3]:"allen"}
# dict1 = {(1,2,3):"allen"}
dt = {"name":"zhangsan","password":"123456"}
# (1)增加key值"iphone",并赋值"13109877890"
# dt["iphone"]="13109877890"
dt1 = {"iphone":"13109877890"}
# dt.update(dt1)
dt.update({"iphone":"13109877890"})
print(dt)
# (2)获取字典中所有的key值
print(dt.keys())
# (3)获取字典中所有的value值
print(dt.values())
# (4)获取字典中所有的键值对
print(dt.items())
# (5)删除key为"iphone"的值
# 根据指定的键删除元素（键值对）
dt.pop("iphone")
print(dt)