# 在控制台输出10-1
# for i in [10,9,8,7,6,5,4,3,2,1]:
#     print(i)

# range和列表的区别
# range生成数据序列的时候是用到哪一个生成哪一个
# 而列表是需要提前创建好，保存在内存才能使用
# for i  in range(10,0,-1):
#     print(i)

# for i  in range(1,11,1):
#     print(i)

# 求1~10之间的偶数的和
# sum = 0
# for i in range(0,11,2):
#     sum += i

# for i in range(1,11):
#     if(i%2==0):
#         sum += i
# print(sum)

# 单层for循环
# 双层for循环
for i in range(1,10):
    for j in range(1,10):
        print("请输入数据%2d:%2d"%(i,j))

# 实现99乘法表
'''
1*1=1
1*2=2   2*2=4
1*3=3   2*3=6   3*3=9
....
分析：
1、总共是9行9列
2、第几行的打印几次乘法字符串就是print()
3、第一行有1列、第二行有1列2列、第三行有1列2列3列.....-->列号<=行号
4、使用双层for循环来实现，外层for控制行（打印一行里面的所有列）--nrow
5、内层for循环来控制列的输出--ncol
6、ncol<=nrow
'''
# 外层for循环来控制行
# for nrow in range(1,10):
#     # 内层for循环控制列的输出：内层循环了9
#     for ncol in range(1,10):
#         if(ncol <= nrow):
#             print("%d*%d=%2d"%(ncol,nrow,ncol*nrow),end="\t")
    
#     # 内层for循环结束后，需要回车换行
#     print()


# for nrow in range(1,10):
#     # 内层for循环控制列的输出，内层循环次数就节省了很多
#     for ncol in range(1,nrow+1):
#         print("%d*%d=%2d"%(ncol,nrow,ncol*nrow),end="\t")
    
#     # 内层for循环结束后，需要回车换行
#     print()

# 有一个列表list1 = [6,2,1,7,9,2]
# 通过for循环实现列表元素的排序（从小到大排序），不能用sort方法。
# 冒泡排序方法：比较相邻的两个数据，较大者往后移动
list1 = [6,2,1,7,9,2]
# 外层控制排序的次数n是列表长度-1
for n in range(0,len(list1)-1):
    # 内层for循环来做比较的次数,相邻的两个数据的比较，较大值往后排
    # -n的效果
    for m in range(0,len(list1)-1-n):
        if(list1[m] >= list1[m+1]):
            # 交换两个位置的数据
            # 1、定义临时遍历
            # temp = list1[m]
            # list1[m]=list1[m+1]
            # list1[m+1]=temp

            # 2、多变量赋值
            # list1[m],list1[m+1] = list1[m+1],list1[m]

            # 3、算术运算
            # list1[m] = list1[m] + list1[m+1]
            # list1[m+1] = list1[m] - list1[m+1]
            # list1[m] = list1[m] - list1[m+1]

            # 4、使用异或运算
            list1[m] = list1[m] ^ list1[m+1]
            list1[m+1] = list1[m] ^ list1[m+1]
            list1[m] = list1[m] ^ list1[m+1]           
print(list1)

list2 = [6,2,1,7,9,2]
# 快速排序方法
# list2.sort()
# print(list2)