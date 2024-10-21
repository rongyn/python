# 列表中使用通用的运算符和方法
list1 = [1, 2, 3, "a", "b", 'c', [1, 2, 3], 1, "a"]
list2 = [12, 23, 34]
# 1、+拼接:将两个列表中的元素拼接到一起
# [1, 2, 3, 'a', 'b', 'c', [1, 2, 3], 1, 'a', 12, 23, 34]
print(list1 + list2)
# 拼接完，list1和list2变了没(只有给list1的元素重新赋值才会变)
print(list1)

# 2、*复制
# [12, 23, 34, 12, 23, 34, 12, 23, 34]
print(list2 * 3)

# 3、in：成员（元素）运算
# "a"是list1中的一个元素嘛？
print("a" in list1)
print("a" not in list1)

# 4、index方法,在列表中不支持find方法
print(list1.index("a"))
print(list1.index([1, 2, 3]))

# 5、max()和min()
print(max(list2))
print(min(list2))

# 6、count()
print(list1.count("a"))

# 7、len():统计列表中元素的个数
print(len(list2))
