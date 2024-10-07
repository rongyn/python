# 这就是一个模块
# 1、先写一个顺序执行的代码
name = "allen"
print(name)

# 2、定义了一个方法，不调用不执行
def playGame():
    print("玩游戏！！")


# 3、定义一个类，不调用不执行
class student():
    def study(self):
        print("学生要学习")


# 在m1中调用了一次方法
# 可能是要调试这个方法的功能，一定是在当前代码中调试通过、正确
# 才会给其他模块调用使用

# 添加一个if条件语句
# __name__是一个内置变量，固定写法
# __main__是一个常量
# 在当前文件（模块）中运行代码，__name__是等于常量__main__的
if __name__=="__main__":
    # 把调试代码放到if语句中
    print(__name__)
    playGame()
# 用于验证的else语句，一般不加
else:
    print(__name__)