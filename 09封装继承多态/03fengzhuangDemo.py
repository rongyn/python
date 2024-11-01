# python中面向对象的三大特性：封装、继承（会用）和多态。
# 封装：在你的类中，有一些属性不希望别人能直接访问到，就需要将该属性私有化
# 在特定的情况下还是要对外提供私有属性的访问的，类中添加对外公共访问的方法，在其中提供私有属性
# 特点：提高属性的安全性
# 封装的过程：私有化属性，提供私有化属性的公共访问方法，在方法进行数据有效性验证
# 1、私有化：在变量或者方法前添加两个下划线__,在类中的各方法之间是可以相互调用的
# self.__age
# __study()
class student():
    def __init__(self,name,age,sex):
        self.name=name
        # 私有化age变量
        self.__age = age
        self.sex = sex
    
    # 2、提供功能的访问方式(私有属性的查看、修改getXxx()和setXxx())：getAge()和setAge()
    def getAge(self):
        return self.__age
    
    # 3、修改年龄，增加对年龄的处理
    def setAge(self,age):
        if(age>0 and age<=120):
            self.__age=age
        else:
            print("输入的数据不符合实际情况！！")

    def study(self):
        print("学生的本职工作就是学习")


xiaoli = student("小李","28","女")
# 'student' object has no attribute 'age'
# print(xiaoli.age)
# 'student' object has no attribute '__age'
# print(xiaoli.__age)
# 到目前，属性已经被私有化了，虽然看不到age和__age
# 所谓的私有化，只是把名称改了：_类名__age
# print(xiaoli._student__age)

# 通过功能的访问方法来查看年龄
print(xiaoli.getAge())
xiaoli.setAge(180)
print(xiaoli.getAge())

# xiaoli.age = 180
# print(xiaoli.age)  #合理吗？不合理，那怎么防范被修改为不合理的数据呢？封装可以