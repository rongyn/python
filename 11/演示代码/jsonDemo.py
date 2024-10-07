# 把allen.json数据读取进来
import json

# 打开文件
# with open(r"e:\allen.json","r",encoding="utf-8") as f:
#     # 使用load方法读取数据
#     data = json.load(f)
#     # [{'name': 'allen', 'age': 28, 'sex': '男', 'id': '18621984010', 'address': ['山东省', '济宁市', '高新区']}, 
#     # {'name': 'lucy', 'age': 25, 'sex': '女', 'id': '14521984010', 'address': ['河北省', '廊坊市', '高新区']},
#     # {'name': 'lily', 'age': 28, 'sex': '男', 'id': '1333984010', 'address': ['陕西省', '西安市', '高新区']}]
#     # print(data)
#     for d in  data:
#         # 读取三个字典元素
#         print(d["address"][0])

# json这个模块还能处理字符串
str1 = "abdc"
# 定义一个python中的字符串，字符串的数据的特点是什么
str2 = '{"name":"lily","age":28,"sex":"男","id":"1333984010","address":["陕西省","西安市","高新区"]}'
# JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
str3 = "{'name':'lily','age':28,'sex':'男','id':'1333984010','address':['陕西省','西安市','高新区']}"
# SONDecodeError: Expecting value: line 1 column 1 (char 0)
# "abc" --> int
data1 = json.loads(str3)
print(data1)
print(type(data1))