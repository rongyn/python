# 字典的定义和值的获取
dict1 = {"邓超":"孙俪","郑凯":"苗苗","黄晓明":"baby","文章":"马伊利","文章":"姚笛"}
# 通过键来获取值
# print(dict1["邓超"])
# 修改文章的值
# dict1["文章"] = "姚笛"
# print(dict1)
# 直接打印这个字典
# {'邓超': '孙俪', '郑凯': '苗苗', '黄晓明': 'baby', '文章': '姚笛'}

# 定义字典的时候：键是不能重复的（set集合）、还是无序的
# 值没有其他的要求
print(dict1)


# 字典中常用的方法
# 1、keys():获取字典中所有的键组成是列表
# dict_keys(['邓超', '郑凯', '黄晓明', '文章'])
print(dict1.keys())

# values():获取字典中所有的值组成是列表
# dict_values(['孙俪', '苗苗', 'baby', '姚笛'])
print(dict1.values())

# 3、items()：返回的是键值对
# dict_items([('邓超', '孙俪'), ('郑凯', '苗苗'), ('黄晓明', 'baby'), ('文章', '姚笛')])
print(dict1.items())

# 4、clear()：清空字典
# dict1.clear()
# print(dict1)

# 5、get()：通过键获取值(熟练使用)
print(dict1.get("文章"))
print(dict1["文章"])

# 6、给字典增加元素
# {'邓超': '孙俪', '郑凯': '苗苗', '黄晓明': 'baby', '文章': '姚笛', '杜江': '霍思燕'}
dict1["杜江"] = "霍思燕"
print(dict1)

dict2 = {"陈小春":"应采儿"}
# 采用update的方法
# {'邓超': '孙俪', '郑凯': '苗苗', '黄晓明': 'baby', '文章': '姚笛', '杜江': '霍思燕', '陈小春': '应采儿'}
dict1.update(dict2)
print(dict1)


dict4 = {}.fromkeys({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'},'a')
print(dict4)