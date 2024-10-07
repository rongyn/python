# 成员运算符：看某个元素是否是序列类型数据的成员
str1 = "ABCDEFG"
list1 = list(str1)
tuple1 = tuple(str1)
print(list1)
print(tuple1)
# in:判断元素是序列类型的成员吗？是就返回True，否则False
# not in:判断元素不是序列类型的成员吗？不是就返回True，否则False
print("A" in str1)
print("A" in list1)
print("A" in tuple1)

print("A" not in str1)
print("A" not in list1)
print("A" not in tuple1)