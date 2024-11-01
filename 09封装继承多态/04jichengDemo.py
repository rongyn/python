# 实现继承的案例
# 人类、猫类共同的属性：姓名、性别、年龄、type（哺乳类、鸟类？）
# 人类特有的属性：社会性
# 小猫特有的属性：有毛
# 人类、猫类共同的行为：吃、睡、玩
# 人类特有的行为：说话，玩王者，人喜欢吃肉
# 猫特有的行为：玩毛线球、猫喜欢吃鱼

# 1、实现人类、猫类、....,存在很多的重复代码
# 2、我们这些重复的代码提取出来，定义在一个动物类中
# 3、建立子类和父类之间的继承关系：class 子类(父类名)
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

# 定义小狗类
class dog(anmial):
    type = "狗类"
    # 小狗不局限于吃饭，而且喜欢吃骨头
    # 方法重写：子类中将父类中的方法再重新设计一遍，方法名相同
    def eat(self,shiwu):
        print("狗喜欢吃%s"%shiwu)

    # 子类特有的方法
    def huaqian(self):
        print("孩子负责花钱")

# 定义人类
class person():
    # 类变量
    type = "人类"
    # 通过构造方法实现实例变量
    def __init__(self,name,sex,age,shehuixing):
        self.name=name
        self.sex=sex
        self.age =age
        self.shehuixing=shehuixing
    #定义人类的行为
    def eat(self):
        print("人吃肉")
    
    def playGame(self):
        print("人玩王者荣耀")
    
    def sleep(self):
        print("动物要睡觉！！")
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


# 创建小狗的对象
d = dog("警犬大黑","male",3)
print(d.age)
print(d.type)
# 直接继承父类的方法，因为子类已经重写了该方法，子类重写了父类的方法，子类对象就只能调用子类重写的方法
d.eat("骨头")
d.sleep()
d.huaqian()