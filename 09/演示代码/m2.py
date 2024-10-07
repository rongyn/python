# 导入m1的代码
# 1、直接使用import导入
# import m1
# 可以使用导入的模块名.方法名()，来调用执行方法
# m1.palyGame()

# 创建student对象
# stu1 = m1.student()
# stu1.study()

# 2、精确导入：也要先打开m1查看playGame才能导入过来，但是只要一查看，顺序代码就执行了
# from m1 import playGame,student
# 就直接使用方法名就可以了
# 因为没有import m1，所以不能使用m1
# m1.playGame()
# playGame()
# # 现在没有导入student类
# s = student()
# s.study()


# 3、直接导包，能不能运行m1中调用的playGame方法
# 你希望在此处调用模块的时候执行m1中调试代码吗？不应该
# 在m2中再次执行导入：m1是__name__的值
# 导包的时候是把if __name__=="__main__"也导过来了
# __name__在m1执行的时候是等于__main__
# __name__但是在m2执行的时候是等于m1的，所以就不再执行m1中的调试代码了
from m1 import playGame,student