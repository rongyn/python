# 现在就创建完成了一个模块
# 模块（包）的导入，常用关键字有两个：import（导入） 、 from（从xxx）
# 导入random模块，把random模块中代码，做一个副本拿到当前模块中
import random
# 从random模块中导入其中的一个方法randint(),导入更精确了
from random import randint
# 导入selenium
import selenium
from selenium import webdriver
# 带包导入
from selenium.webdriver.common.by import By

# 导模块（包）的格式
# import 模块名/包名
# from 模块名/包名  import 类名/方法名/变量名
