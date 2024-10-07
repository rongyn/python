class anmial():
    type = "动物"
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age =age 
    #定义人类的行为
    def eat(self):
        print("动物要吃饭！！")
    
    def playGame(self):
        print("动物要玩耍！！")
    
    def sleep(self):
        print("动物要睡觉！！")   

# 定义人类:继承父类的方法
class person(anmial):
    # 类变量
    type = "人类"
    # 通过构造方法实现实例变量
    def __init__(self,name,sex,age,shehuixing):
        # 调用父类构造方法实现参数的初始化
        # 父子共有的实例变量，调用父类构造方法初始化
        anmial(name,sex,age)
        # 儿子自己的实例变量，需要自己初始化
        self.shehuixing=shehuixing
    #定义人类的行为,重写了父类的方法（子类的名字和父类一样）
    def eat(self):
        print("人吃肉")
    
    def playGame(self):
        print("人玩王者荣耀")
    
    def sleep(self):
        print("动物要睡觉！！")

    # 子类特有的方法
    def study(self):
        print("人类会学习进步！！")
# 定义猫类
class cat():
    # 类变量
    type = "猫类"
    # 通过构造方法实现实例变量
    def __init__(self,name,sex,age,mao):
        self.name=name
        self.sex=sex
        self.age =age
        self.mao=mao
    #定义人类的行为
    def eat(self):
        print("猫吃鱼")
    
    def playGame(self):
        print("猫玩毛线球")
    
    def sleep(self):
        print("动物要睡觉！！")

# 创建一个人类
xiaozhang = person("小张","男",28,True)
xiaozhang.eat()
xiaozhang.study()
print("小张是具备%s"%xiaozhang.shehuixing)