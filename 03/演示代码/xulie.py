str1 = "hello"
str2 = " world!!"
# +是拼接功能，拼接两个序列（字符串序列）
print(str1+str2)

# in、not in：成员运算符
str3 = "ABCDEFG"
print("A" in str3)
print("AA" in str3)
print("A" not in str3)
print("AA" not in str3)

# *：复制运算，格式：序列 * 数字
print(str3*7)

# 索引：序列名[索引号]
print(str3[0])
print(str3[-7])
# string index out of range
# print(str3[7])
# string index out of range
print(str3[-8])

# 切片：从大的序列中切出一个小序列
# 格式：序列名[start:end:step]
# start:开始的索引号
# end：结束的索引号
# step：步调，默认值是1，如果设置为2则隔一个取一个值；如果是-1，则倒着挨个取
# 左闭右开（可以取到start索引对应的值，但是取不到end对应的值）
print(str3[1:4])
print(str3[1:4:2])
print(str3[::])
print(str3[::-1])
print(str3[-1:-7:-1])
print(str3[-1:-8:-1])