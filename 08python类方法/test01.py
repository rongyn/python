class animal():
    '''
    alter:ryn
    '''
    # 创建类变量：在类中方法外定义，是所用的对象共享的变量
    type = '动物'

    # 实例变量：在类的方法中的变量，self开头的
    # 局部变量：定义在方法的参数列表中或者方法内的变量
    # 先写一个方法：eat
    def eat(self, food):
        self.shixing = food
        aa = 12

    # 定义info方法，来初始化动物的属性名称喝性别
    def info(self, xingming, xingbie):
        self.name = xingming
        self.sex = xingbie

    # 定义要睡觉的方法
    def sleep(self):
        print("animals must sleep")


# 类不创建对象是不执行的
cat = animal()
# 查看小猫的类型，type是类变量
print(cat.type)
# 通过info方法给小猫确定名字和性别
cat.info("花花", "male")
# name和sex是实例（就是对象，就是cat）变量
print(cat.name)
print(cat.sex)


#类变量是给所有对象使用
#实例变量是给固定某一个变量使用
dog = animal()
# 查看小猫的类型，type是类变量
print(dog.type)
print(dog.name)
print(dog.sex)