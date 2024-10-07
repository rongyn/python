# 导入module01中的test01这个模块
import sys
import os

# 获取education目录的绝对值
path = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)

# print(sys.path)
# education目录已经加导sys.path,python就能检索这个目录了
# 下面就能够导入该目录下的模块或者包（有__init__.py文件的文件夹）
# 要带包导入模块
from module01.test01 import student
from  module01.test02 import func
stu = student()
print(stu.add(12,23))
func()