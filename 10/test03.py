# 希望在当前文件中导入day08目录下test01.py
from importlib.resources import path
import os
import sys

# 1、直接将day08获取并追加到sys.path
# __file__: 当前文件
# os.path.dirname(__file__)：获取当前文件所在的目录（相对值）（vscode中可以，但是在cmd不识别）
# os.path.abspath(os.path.dirname(__file__))：将获取的目录转化为绝对值的形式（vscode、cmd运行都正常）
path1 = os.path.abspath(os.path.dirname(__file__))
# 获取上一级目录
# path2 = os.path.abspath(os.path.dirname(path1)) + r"/day08"
path2 =  os.path.abspath(os.path.dirname(path1)) 
# 2、将day08定义成包：__init__.py
# 把path2追加到sys.path
sys.path.append(path2)

# 如果day08是包的话，是可以直接带包导入的
# 因为python能够定位到pythonDemo目录，就能检索其下的模块和包
import day08.test01
from  day08.test01 import playGame