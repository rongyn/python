list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 创建list1的时候查看一次地址
print(id(list1))
list2 = ["a", "b", "c", "d"]
list3 = [1, 2, 3, "a", "b", 'c', [1, 2, 3], 1, "a"]
# 1、列表是有序的
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ['a', 'b', 'c', 'd']
# 2、列表中的元素是可以重复的
# # [1, 2, 3, 'a', 'b', 'c', [1, 2, 3], 1, 'a']
# print(list1)
# print(list2)
# print(list3)
# 3、列表是可变的
# 4、列表是可以索引的:每一个元素都有2个编号，一个正向、反向
# 想更改一个元素的值
list1[1] = 20
# 在更改完值之后，查看list1地址是否发生了变化
print(id(list1))
print(list1[1])
# [1, 20, 3, 4, 5, 6, 7, 8, 9]
print(list1)
# 判断list1是可变的：地址没有发生了变化，但数据发生变化
# python中提供了id方法来监测变量的地址（变量指向的地址）
# id(变量名)

# 5、列表是可以切片的
list4 = [1, 2, 3, "a", "b", 'c', [1, 2, 3], 1, "a"]
# 想获取第三个元素到最后所有的元素
print(list4[2:])
# 获取第三个到第五个元素
print(list4[2:5])
