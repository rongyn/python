# 在此模块中导入test01.py
# __name__ != "__main__",现在等于test01这个模块名

# 1、导包的文件在当前目录下（都在day09这个目录下），是可以直接进行导包的
# import test01
# from test01 import playGame,student


# 2、test01.py文件是在test02.py的上一级目录
# ModuleNotFoundError: No module named 'test01'？？？
# import test01

# 导入sys模块
from importlib.resources import path
import os
import sys
# ['e:\\3-Learning\\17-BJ2201\\pythonDemo\\day09', 'D:\\Python\\python38.zip', 
# 'D:\\Python\\DLLs',
# 'D:\\Python\\lib', 'D:\\Python', 'D:\\Python\\lib\\site-packages']
# 需要将你要导包的模块所在的目录加入到sys.path这个列表中,python就能找到该模块并导入
# sys.path.append(r"E:\3-Learning\17-BJ2201\pythonDemo")
# ./在vscode中指的是E:\3-Learning\17-BJ2201\pythonDemo
# ./day09
# sys.path.append(r"./")
# 希望既可以在cmd下、也可以在vscode中运行，还不想用绝对路径，怎么办
# 在os模块中提供了一些出来路径的方法

# 当前文件test02.py所在的目录,os.path.dirname()就是获取指定文件或者目录所在的目录
# __file__指的是当前文件test02.py的名字
# e:/3-Learning/17-BJ2201/pythonDemo/day09
# e:\3-Learning\17-BJ2201\pythonDemo\day09
# 现在已经能够动态获取当前文件所在的目录的绝对值
path1 = os.path.abspath(os.path.dirname(__file__))
# 下面要获取当前目录上一级目录的绝对值
path2 = os.path.abspath(os.path.dirname(path1))
# 将path2追加到sys.path中
sys.path.append(path2)

# 开始导包
import test01