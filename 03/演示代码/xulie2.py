str1 = "ABCDEFGGG"
str2 = "12ABCDE23F44GGG"
# 获取序列的长度（元素的个数），个数：len(序列名)
print(len(str1))

# 获取最大、最小元素：max(序列名)、min(序列名)
print(max(str2))
print(min(str2))

# 获取元素索引:序列名.index(元素值,start,end)
print(str2.index("E"))
print(str2.index("E", 4, 10))
# substring not found
# print(str2.index("E",7,10))

# 获取序列中某个元素出现的次数-count()
print(str2.count("2"))
