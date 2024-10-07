# 列表处理的增删改查的方法
# list1 =  [1, 2, 3, 'a', 'b', 'c', [1, 2, 3], 1, 'a', 12, 23, 34]
# 1、列表元素的查看
# 使用索引方式查看列表的元素(分别取第一个和最后一个)
# print(list1[0])
# print(list1[-1])
# print(list1[:])
# 列表逆序
# print(list1[::-1])
# list2 = list1[::-1]
# print(list2)
# list1.reverse()
# print(list1)

# 2、给列表增加运算
# 第一种：append方法--追加，给列表的末尾追加元素
# None
# print(list1.append("allen"))
# 列表是有序的
# list1.append("allen")
# list1.append("lucy")
# list1.append("lily")
# # [1, 2, 3, 'a', 'b', 'c', [1, 2, 3], 1, 'a', 12, 23, 34, 'allen']
# print(list1)

# 第二种：insert方法--插入，就会出现按照指定位置插入元素
# insert(插入位置的索引号，插入的元素)，原索引号位置及其后的元素都要右移动一个索引
# list1.insert(1,"allen")
# [1, 'allen', 2, 3, 'a', 'b', 'c', [1, 2, 3], 1, 'a', 12, 23, 34]
# print(list1)

# 第三种：extend方法--扩展列表，把一个列表中(list2)的元素分别追加到另外一个列表中(list1)
list2= ["allen","小王","小李"]
# [1, 2, 3, 'a', 'b', 'c', [1, 2, 3], 1, 'a', 12, 23, 34, ['allen', '小王', '小李']]
# list1.append(list2)
# [1, 2, 3, 'a', 'b', 'c', [1, 2, 3], 1, 'a', 12, 23, ['allen', '小王', '小李'], 34]
# list1.insert(-1,list2)
# [1, 2, 3, 'a', 'b', 'c', [1, 2, 3], 1, 'a', 12, 23, 34, 'allen', '小王', '小李']
# list1.extend(list2)
# print(list1)

list3 =  [1, 2, 3, 'a', 'b', 'c', [1, 2, 3], 1, 'a', 12, 23, 34]
# 列表的元素删除
# 1、pop():弹出，每执行一次pop，默认的总是把列表中的最后一个元素弹出并返回
# print(list3.pop())
# print(list3)
# pop(index):按照指定的索引号index删除数据并返回该数据
# print(list3.pop(1))
# print(list3)

# 2、del list3[2]:删除列表中指定的元素
# del list3[2]
# print(list3)

# 3、通过切片的方式删除
# list3[3:6] = []
# print(list3)

# 4、remove(删除的值)：按照指定的值（列表第一次出现的）删除
# list3.remove("a")
# # [1, 2, 3, 'b', 'c', [1, 2, 3], 1, 'a', 12, 23, 34]
# print(list3)

# 列表元素的修改
# list3[0] = 10
# list3[0:2] = ["allen","小王","小张"]
list3[0] =  ["allen","小王","小张"]
print(list3)