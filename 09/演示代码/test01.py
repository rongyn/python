# 1.定义一个员工类,自己分析出几个实例变量（属性）、方法（行为），以及一个显示所有成员信息的方法，并测试。
# 2.定义一个手机类,自己分析出几个实例变量（属性）、方法（行为），以及一个显示所有成员信息的方法，并测试。
# 分析众多手机的共同的属性和行为：
# 属性：型号、尺寸、品牌、颜色、价格、处理器类型等，智能手机（类别）
# 行为：打电话、发短信、上网、玩游戏、买东西、自拍等
# 实现这个类
class phone():
    # 定义类变量
    type = "智能手机"

    # 定义实例变量，并通过构造方法来初始化
    def __init__(self,brand,color,price,size,memory,process):
        # 实例变量初始化
        self.brand = brand
        self.color = color
        self.size = size
        self.price = price
        self.memory = memory
        self.process = process
    # 定义手机打电话的功能
    def call(self,telephoneId):
        print("打电话给"+telephoneId)

    def photo(self):
        print("手机价格为"+str(self.price)+",可以用来自拍！！")
    # 用来输出所有的成员变量
    def info(self):
        print("手机的品牌为:%s,价格为：%s,颜色为:%s,尺寸为：%s"%(self.brand,self.price,self.color,self.size))

# 创建对象调用方法
# 先来创建一个小米11手机
xiaomi11 = phone("小米","black",2999,6,16,"高通骁龙860")
# 访问小米11的属性和行为
print(xiaomi11.brand)
print(xiaomi11.memory)
print(xiaomi11.price)
# 访问方法
xiaomi11.call("18621984010")
xiaomi11.photo()
xiaomi11.info()