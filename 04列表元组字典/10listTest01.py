# 已知列表 L = ['apple','pear','banana','oranger','grape']
L = ['apple','pear','banana','oranger','grape']
# (1) 往列表L中追加“peach”
# L.append("peach")
L.insert(5,"peach")
print(L)
# (2) 定义另外一个列表L1 = [1,2,"A","B"],将该列表追加至L中
L1 = [1,2,"A","B"]
# 将列表追加
L.append(L1)
print(L)
# 将列表元素追加
L.extend(L1)
print(L)
# (3) 向列表L开头添加“fruit:”
L.insert(0,"Fruit:")
print(L)
# (4) 获取列表L的总长度(列表元素个数)
print(len(L))
# (5) 删除列表L的最后一个元素（使用两种方法）
# 不带参数，默认弹出最后一个
# L.pop()
# L.pop(-1)
# del L[-1]
del L[len(L)-1]
print(L)
# (6) 删除列表的第5个元素
# L.pop(4)
del L[4]
# ['Fruit:', 'apple', 'pear', 'banana', 'grape', 'peach', [1, 2, 'A', 'B'], 1, 2, 'A']
print(L)
# (7) 删除元素“A”(删除两处的A)
L.remove("A")
print(L)
L[6].remove("A")
print(L)


# 已知列表 L2 = [2,1,4,5,4]
L2 = [2,1,4,5,4]
# (1)对列表L2进行排序--sort()
# [1, 2, 4, 4, 5]
# L2.sort()
# [5, 4, 4, 2, 1]
# L2.sort(reverse=True)
print(L2)
# (2)获取列表中的最大值和最小值
# print(L2[0])
# print(L2[-1])
print(max(L2))
print(min(L2))
# (3)对排序好的列表进行逆序排列（使用两种方法）
# L2.sort(reverse=True)
L2.sort()
print(L2[::-1])