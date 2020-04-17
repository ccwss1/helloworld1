# while 语句基础用法
# sum = 0
# i = 0
# while i < 101:
#     if i % 2 != 0:
#         sum += i
#     i=i+1
# print("0到100的求和为 %d"% sum)


# break语句
# i = 0
# while i < 10:
#     if i == 3:
#         break
#     print(i)
#     i = i+1

# continue语句
# i = 0
# while i < 10:
#     if i == 7:
#         i = i+1
#         continue
#     print(i)
#     i = i+1

# 用嵌套打印小星星
# i = 1
# while i <= 5:
#     print("*" * i)
#     i = i+1
# row = 1
#
# while row <= 5:
#     col = 1
#     while col <= row:
#         print("*",end='')
#         col = col+1
#     print("")
#     row = row+1


# #print函数默认换行
# print(0)
# print(1)
# print(2,end='')
# print(3,end="==")
# print(4)
# print(5)

# 九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        result=col * row
        print("%d * %d = %d " % (col,row,result),end='\t')
        col = col + 1
    print('')
    row = row + 1
# 转义字符
print("hello \n hello")
print("hello \' hello")
print("hello \" hello")
print("hello \\ hello")
print("hello \r hello")