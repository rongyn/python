# 多继承


class fu():
    # 父亲的外貌属性
    waimao = "帅"
    # 父亲的行为
    def zhuanqian(self):
        print("父亲负责赚钱养家！！")

class mu():
    # 母亲的长相
    zhangxiang = "漂亮"
    # 母亲的行为
    def chijia(self):
        print("母亲负责漂亮！！")

# 他俩的儿子、女儿
class zi(fu,mu):
    pass


# 创建儿子的对象
z = zi()
print(z.waimao)
print(z.zhangxiang)
z.zhuanqian()
z.chijia()