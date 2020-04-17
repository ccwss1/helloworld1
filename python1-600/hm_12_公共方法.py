t_list = [1, 2, 3]
del t_list[1]
print(t_list)
t_str = "gdsfac"
t_dict = {"a": "z", "b": "u"}
t_tuple = (1, 2, 3, 4)
print(len(t_tuple))
# max，min统计字典时只比较key值
print(max(t_str), min(t_list), max(t_dict), min(t_tuple))
print("ab" > "cd")  # dictionary不能比较大小
print([1, 2] > [5, 6])

# tuple,list,str可以切片,dict不能
print([1, 2, 3][:2])
print((0, 9, 8)[:1])
print("bhgj"[:3])

# 运算符，+ * > < >= <= == str,tuple,list可以，in，not in均可
print([7] * 6)
print([9] + [0])  # 返回新的list
t_list.extend([8, 9])  # 在原始的list上修改,合并
t_list.append([6, 7])  # 参数list被当成一个元素插入到列表末尾
print(t_list)
print((6,) * 8)
print((1, 2) + (3, 4))
print("v" * 8)
print("o" + "p")
print("a" in "abc")
print("n" in {"n": "p"})  # 只判断key

# for循环
for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    # if 遍历结束执行else后面的，如果for里用break退出循环，else不会被执行
    print("会执行吗")
print("循环结束")

students = [
    {"name": "xiaoming"},
    {"name": "zhangsan"}
]
find_name = "xiaoming"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了，%s" % find_name)
        break
else:
    print("你找的人不存在")
print("循环结束")
