class persion():
    # 国籍的属性：定义为实例变量好还是类变量好
    guoji = "中国"

# 对于类变量是可以通过类名直接访问的
# print(persion.guoji)
persion.guoji = "美国"
# 创建一个小王对象
xiaowang = persion()
# 已经不再是类变量的guoji了，而是给xiaowang对象创建了一个和类变量同名的成员变量
# xiaowang.guoji = "美国"
# 输出的成员变量的guoji
print(xiaowang.guoji)
print(persion.guoji)

# 创建一个小李对象
xiaoli = persion()
# 小李拿到的是类变量中的guoji
print(xiaoli.guoji)