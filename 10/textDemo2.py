# 2、往txt文件中写入数据
# 打开文件的模式就是w或者a
# f = open(r"e:\allen.txt","w",encoding="utf-8")
# f = open(r"e:\allen.txt","a",encoding="utf-8")

# 写入：allen老师，你好，大家好！！！
# write(str):将指定的字符串str写入到文件中,是覆盖写入
# writelines():参数是一个列表，把列表的元素作为行写入，如果需要换行，每个元素结尾要带\n字符
# f.write("allen老师，你好，大家好！！！")
lists = ["allen\n","老师\n","你好\n","大家好\n","全国人民好！！\n"]
# f.writelines(lists)

# 读写完成之后，需要关闭文件对象
# f.close()


# 3、with语句实现文件的打开并读写（这个必须掌握）
# 更安全，可以帮我自动关闭文件对象
# with open(r"e:\allen.txt","r",encoding="utf-8") as f:
#     print(f.readlines())

with open(r"e:\data\1234.jpg","rb") as f:
    print(f.read())