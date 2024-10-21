# L = ['apple', 'pear', 'banana', 'orange', 'grape']
# L.append('peach')
# print(L)
#
# L1 = [1, 2, "A", "B"]
# L.append(L1)
# print(L)
#
# L.insert(0, 'fruit:')
# print(L)
#
# print(len(L))

# L.pop()
# print(L)
# del L[-1]
# print(L)
#
# del L[4]
# print(L)
#
# L[6].remove("A")
# print(L)
#
# L2 = [2, 1, 4, 5, 4]
# L2.sort()
# print(L2)
# print(max(L2))
# print(min(L2))
# # print(L2[::-1])
# L2.reverse()
# print(L2)
#
# dt = {"name": "zhangsan", "password": "123456"}
# dt["iphone"] = "123123123"
# print(dt)
#
# print(dt.keys())
#
# print(dt.values())
#
# print(dt.items())
#
# dt.pop("iphone")
# print(dt)


# score = int(input("请输入成绩:"))
# if score >= 90:
#     print("A")
# elif score >= 80 and score <= 89:
#     print("B")
# elif score >= 70 and score <= 79:
#     print("C")
# elif score >= 60 and score <= 69:
#     print("D")
# else:
#     print("E")
#
# a = int(input("请输入数字a:"))
# b = int(input("请输入数字b:"))
# c = int(input("请输入数字c:"))
# if a > b:
#     if a > c:
#         print("a最大:%d" % a)
#     else:
#         print("c最大:%d" % c)
# else:
#     if b > c:
#         print("b最大:%d" % b)
#     else:
#         print("c最大：%d" % c)


# for i in range(1,11):
#     print(i)

# 错误：for i in range(10, 1):
#     print(i)
# 正确：for i in range(10, 0, -1):
#     print(i)

# sum1 = 0
# for i in range(1, 11):
#     sum1 += i
# print(sum1)

sum1 = 0
for i in range(0, 11, 2):
    sum1 += i
print(sum1)

# 99：
for h in range(1, 10):
    for l in range(1, 10):
        if (l < h):
            print("%d*%d=%d" % (l, h, l * h), end="\t")
    print()
# 冒泡
list1 = [2, 1, 6, 7, 2, 9]
for i in range(0, len(list1) - 1):
    for j in range(0, len(list1) - 1):
        if (list1[j] >= list1[j + 1]):
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp
print(list1)
