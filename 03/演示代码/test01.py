# 已知字符串s = "I’m learning Python,my name is xiaobai!"
# 字符串是用单引号或者双引号圈起来的一组字符
# 变量：只有完成赋值初始化之后才有对应数据的数据类型
s = "I’m learning Python,my name is xiaobai!"
# (1)截取字符串（切片、索引功能）
# 	截取第一位到第三位的字符（索引号要比这个位数少1）；
# 切片的格式：str1[start:end:step],左闭右开的特点
print(s[0:3])
# 	截取字符串的全部字符；
print(s[:])
print(s[0:50])
print(s[0:len(s)])
# 	截取第七个字符到结尾；
print(s[6:len(s)])
# 	截取从头开始到倒数第三个字符之前；
print(s[0:len(s) - 3])
# 第一个元素有两个索引号：0或者-len(s)
print(s[-len(s):-3])
print(s[0:-3])
print(s[:-3])
# 	截取第三个字符；
print(s[2])
print(s[2:3])

# 	截取倒数第一个字符；
# 索引取值的话，下标不能越界： string index out of range
print(s[len(s) - 1])
print(s[-1])
# 	创造一个与原字符串顺序相反的字符串；
#   能不能把原字符串直接反转？字符串是常量，是不可变的
str1 = s[::-1]
print(str1)
print(s)

# 	截取倒数第三位到结尾；
print(s[len(s) - 3:])
print(s[-3:])

# (2)字符串函数
s1 = "I’m learning Python,my name is xiaobai!"
# 	获取“l”的索引；
#  str.index(subStr,start,end)
print(s1.index("l"))
print(s1.index("l", 0, len(s1)))
# 	查找“Python”在字符串中的位置；
print(s1.index("Python"))

# 	获取“n”出现的次数；
print(s1.count("n"))

# 	获取字符串“xiaobai”；
# 先获取x的索引号：查xiaobai的索引即可
# 然后获取i的索引号，x的索引号+xiaobai的长度
print(s1[s1.index("xiaobai"):s1.index("xiaobai") + len("xiaobai")])
print(s1.index("xiaobai"))
# 如果把空格看作是分隔符
# ['I’m', 'learning', 'Python,my', 'name', 'is', 'xiaobai!']
print(s1.split(" ")[-1].split("!")[-2])

# 	把“xiaobai”替换成自己的名字；(超纲)
print(s1.replace("xiaobai", "allen"))
# 	把字母转换成大写；
print(s1.upper())
print(s1.lower())

# 一个网页的HTML源码。其中有一段：
# 	<html><body><h1>hello world</h1></body></html>
# 	想要把这个hello world提取出来，用python 的字符串处理，如何处理？

str2 = "<html><body><h1>hello world</h1></body></html>"
print(str2[str2.index("hello world"):str2.index("hello world") + len("hello world")])
print(str2.split("<h1>")[-1].split("</h1>")[0])
