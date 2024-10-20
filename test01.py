L = ['apple', 'pear', 'banana', 'orange', 'grape']
L.append('peach')
print(L)

L1 = [1, 2, "A", "B"]
L.append(L1)
print(L)

L.insert(0, 'fruit:')
print(L)

print(len(L))

# L.pop()
# print(L)
# del L[-1]
# print(L)

del L[4]
print(L)

L[6].remove("A")
print(L)

L2 = [2, 1, 4, 5, 4]
L2.sort()
print(L2)
print(max(L2))
print(min(L2))
# print(L2[::-1])
L2.reverse()
print(L2)

dt = {"name": "zhangsan", "password": "123456"}
dt["iphone"] = "123123123"
print(dt)

print(dt.keys())

print(dt.values())

print(dt.items())

dt.pop("iphone")
print(dt)
