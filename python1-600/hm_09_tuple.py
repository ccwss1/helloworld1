info_tuple = ("zhangsan", 18, 1.75)
print(type(info_tuple))
empty_tuple = ()
print(type(empty_tuple))
single_tuple = (1,)
print(info_tuple[0])
print(info_tuple.index(1.75))
print(info_tuple.count("zhangsan"))
print(len(info_tuple))
# tuple很少遍历，因为数据类型不一致
for my_info in info_tuple:
    print(my_info)

print(" %s 的年龄是 %d ,身高是 %.2f" % info_tuple)

# 元组和列表转换
number_list = [1, 2, 3, 4]
number_tuple = tuple(number_list)
number2_tuple = (1, 2, 3, 4)
number2_list = list(number2_tuple)