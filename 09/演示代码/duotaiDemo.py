# 到java语言的时候，重点再给大家讲讲多态。
# 正常的多态有个前提：继承
# python中的多态：不管你有没有继承，只要具备某个功能，就可以运行
# 定义父类
class animal():
    def run(self):
        print("animal Running")

class cat(animal):
    def run(self):
        print("cat Running")


class dog():
    def run(self):
        print("dog Running")

# 这里写animal只是迷惑大家的，写a\b\c都没问题
def runLiangCi(animal):
    animal.run()

# 定义两个对象
a=animal()
c = cat()
d =dog()
runLiangCi(c)
runLiangCi(a)
# 传的一个狗的对象，cat参数能不能接收的了
# dog Running
runLiangCi(d)