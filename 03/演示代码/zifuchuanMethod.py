str1 = 'A''B''C''D'
str2 = "ABCDEFGFFDD"

print(str2[1])


# 获取str2中B字符的索引号-index()
print(str2.index("B"))
# 有重复，从左往右取出现第一次的索引
print(str2.index("F"))
# 多个字符的索引
print(str2.index("FG"))
# substring not found
# print(str2.index("F1G"))

str3 = "    asdf     allen        dd  "
# lstrip():裁剪str3左侧的空格，并返回裁剪后的字符串副本
# rstrip():裁剪str3右侧的空格，并返回裁剪后的字符串副本
# strip():裁剪str3两侧的空格，并返回裁剪后的字符串副本
print(str3.lstrip())
print(str3)
print(str3.rstrip())
print(str3.strip())

# 将字符串首字母大写的方法-title()
str4 = "abcdefg"
print(str4.title())
print(str4)

# 按照指定的分隔符，将一个字符串分隔成多个-split()
# 186-2198-4010
str5 = "186-2198-4010"
print(str5.split("-"))