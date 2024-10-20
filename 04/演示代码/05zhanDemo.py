list1 = []
list1.append("A")  # 相当于压栈A
list1.append("B")  # 相当于压栈B
list1.append("C")  # 相当于压栈C
list1.append("D")  # 相当于压栈D
print(list1)
print(list1.pop())  # 相当于弹栈D
print(list1.pop())  # 相当于弹栈C
print(list1)
print(list1.pop())  # 相当于弹栈B
print(list1.pop())  # 相当于弹栈A
print(list1)
