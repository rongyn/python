# 定义动物类
class animal():

    # 创建类变量：在类中方法外定义，是所有的对象共享的变量
    type = "动物"
    # 2、带参数的构造方法
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    # 定义要给睡觉的方法
    def sleep(self):
        print("动物都要睡觉")

# 类不创建对象，就是不执行的
# 创建了小猫的对象
# 在创建cat对象的时候是默认自动调用了__init__()构造方法
cat =  animal("xiaohua","female")
print(cat.name)
print(cat.sex)
cat.sleep()
print("=====================")
dog = animal("小黑","male")
print(dog.name)  #self.name相当于dog.name
print(dog.sex)
