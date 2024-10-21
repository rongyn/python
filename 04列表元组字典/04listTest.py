# 1.如何获取list中最大整形元素的索引？list1=[12,23,4,6,8,13,34,1,23,5]
list1 = [12, 23, 4, 6, 8, 13, 34, 1, 23, 5]
# 分析：先找出最大元素（max），根据该元素确定索引（index）
print(list1.index(max(list1)))
print(max(list1))


# 2、使用序列显示班级5名同学名单，并实现名单的增删改
student_name = ["小张", "小王", "小李", "小崔", "小刘"]
# 给列表增加一个新的学员
student_name.append("小马")
print(student_name)
student_name[student_name.index("小马")] = "小马哥"
print(student_name)
# 要删除小马哥
# student_name.remove("小马哥")
# 通过小马哥的索引号删除
del student_name[student_name.index("小马哥")]
print(student_name)
