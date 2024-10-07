# 读取allen.txt文件中的数据
# 1、打开文件，并指定打开的方式
# f = open(r"e:\allen.txt","r",encoding="utf-8")
# 2、对文件进行读取
# f.read(size): 指定size，就按照size个数读取，不指定就是全部读取
# f.readline(size)：不指定size，读取一行，指定size，则读取指定size字节长度的数据
# f.readlines():一次性把所有的行数据读取出，将其每行数据作为元素存储在一个列表中
# print(f.read())
# print(f.read(3))

# print(f.readline()) #这句运行，f指向了第二行的开始
# print(f.readline(3))

# ['1abcdefg\n', '2sdfasdfa\n', '3abcdefg\n', '4abcdefg\n', '5asdfasfas\n', '6abcdefg']
# print(f.readlines())
# f.close()

import  time
# 使用文件读取的方法，实现一个控制台版本的小说阅读器
f = open(r"e:\allen.txt","r",encoding="utf-8")
# 把内容一次性读出每行，保存到列表
# 列表遍历，延时输出
for i in f.readlines():
    print(i)
    # 每隔开一秒，刷新一行
    time.sleep(1)
# 关闭文件对象
f.close()