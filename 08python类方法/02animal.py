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
    def info(self,xingming,xingbie):
        self.name = xingming
        self.sex = xingbie

    # 定义要给睡觉的方法
    def sleep(self):
        print("动物都要睡觉")

# 类不创建对象，就是不执行的
# 创建了小猫的对象
cat =  animal()
# 查看小猫的类型,type是类变量
print(cat.type)
# 通过info方法就给小猫确定了名字和性别
cat.info("花花","male")
# name和sex是实例（就是对象，就是cat）变量
print(cat.name)
print(cat.sex)

# cat对象能不能eat()
cat.eat("鱼")
print(cat.shixing)

# cat对象睡觉行为sleep（）
cat.sleep()

# 类的文档字符串查看
print(animal.__doc__)

print("===============================")
# 类变量是给所有对象使用的
# 实例变量是给固定某一个变量使用的

# 创建了小狗的对象
dog =  animal()
# 查看小狗的类型,type是类变量
print(dog.type)
# print(dog.name)
# print(dog.sex)