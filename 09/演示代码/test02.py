# 3.编写Python程序，模拟简单的计算器。(一定要用面向对象，以创建类的方式实现)
# 定义名为Number的类，其中有两个整型数据实例变量n1和n2，编写__init__方法，外部接收n1和n2；
# 再为该类定义加（addition）、减（subtration）、乘（multiplication）、除（division）等方法，分别对两个成员变量执行加、减、乘、除的运算。
# 创建Number类的对象，调用各个方法，并显示计算结果。
# 分析：已经确定了2个实例变量和4个方法
class Number():
    # 定义构造方法实现两个实例变量的初始化
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    # 实现加法运算
    def additon(self):
        return self.n1 + self.n2

    # 实现减法运算
    def substation(self):
        return self.n1 - self.n2

    # 实现乘法运算
    def multiplication(self):
        return self.n1 * self.n2

    # 实现除法运算
    def division(self):
        return self.n1 / self.n2


# 创建一个实际计算器对象
iphoneCalc = Number(24,2)
# 赋值调用
he = iphoneCalc.additon()
print(he)
# 直接调用
print(iphoneCalc.substation())
print(iphoneCalc.multiplication())
print(iphoneCalc.division())