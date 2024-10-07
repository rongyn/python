str1 ="hello"
str1 = r"world\n你好中国"
str2=r'D:\Node\node_modules'

# print("asdfasdfasdf")
print(str2)


str3 = "A"
# Return the Unicode code point for a one-character string.
# 将一个字符组成的字符串转化为unicode整数编码
print(ord(str3))  #65
print(chr(97))
# print(0x10ffff)

str4 = "好"
print(ord(str4))  #22909
print(chr(22909))

# 字符串在python都是unicode编码的
# 将一个unicode编码的字符串转为ascii编码
# encode()方法实现中文字符串的编码
print("A".encode("ascii"))  #b'A'
# 在ascii码中没有对应的这个字符
# print("好".encode("ascii"))

# 将"好"转为gb2312编码
print("好".encode("gb2312"))  #b'\xba\xc3'
print("好".encode("utf-8"))   #b'\xe5\xa5\xbd'

# 用什么字符集进行的编码就要使用什么字符集进行解码
# 使用decode()进行解码
# aa = b'\xba\xc3'
# print(aa.decode("gb2312"))
# print(aa.decode("utf-8"))

print("小".encode("gb2312"))
bb = b'\xd0\xa1'
print(bb.decode("gb2312"))
print(bb.decode("utf-8"))

cc = b'\xe5\xa5\xbd'
print(cc.decode("utf8"))