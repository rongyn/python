# 定义动物类
class animal():
    """
       作者：allen
       功能描述：实现动物类
       版本：v1.0  
    """
    # 创建类变量：在类中方法外定义，是所有的对象共享的变量
    type = "动物"

    # 实例变量：在类的方法中的变量，self开头的
    # 局部变量：定义在方法的参数列表中或者方法内的变量
    # 先写一个方法,要求方法的第一个参数必须是self：eat(self)
    def eat(self,shiwu):
        self.shixing = shiwu
        print("动物要吃%s"%self.shixing)
    
    # 定义info方法，来初始化动物的属性名称和性别
    # 咱们自己写了一个方法进行初始化
    # def info(self,xingming,xingbie):
    #     self.name = xingming
    #     self.sex = xingbie
    # 定义构造方法，用来初始化动物的名称和性别
    # 1、无参数的构造方法，方法名是固定的
    def __init__(self):
        # pass是空语句，如果一条语句没有是有语法错误的，加上空语句就没问题了
        # pass
        self.name = "花花"
        self.sex = "male"

    # 2、带参数的构造方法
    def __init__(self,xingming,xingbie):
        self.name = xingming
        self.sex = xingbie



    # 定义要给睡觉的方法
    def sleep(self):
        print("动物都要睡觉")

# 类不创建对象，就是不执行的
# 创建了小猫的对象
# 在创建cat对象的时候是默认自动调用了__init__()构造方法
cat =  animal("xiaohua","female")
print(cat.name)
print(cat.sex)
print("=====================")
# dog = animal()
# print(dog.name)
# print(dog.sex)
