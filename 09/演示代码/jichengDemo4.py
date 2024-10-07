# 多层继承：sun->fu->yeye

class yeye():
    def shuohua(self):
        print("在家说话声音最大！！")
    

class fu(yeye):
    def zhuanqian(self):
        print("赚钱养家")

class sun(fu):
    def zhuanqian(self):
        print("孙子负责花钱")

s = sun()
s.shuohua()
s.zhuanqian()