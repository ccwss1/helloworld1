# 数据和变量分开保存，变量中保存的是数据的地址
# a = 1
# print(id(a))
# print(id(1))
# b = a
# print(id(b))
# c = 1
# print(id(c))
# a = 2
# print(id(a), id(b))
# print(a, b, c)


def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))
    result = "hello"
    print("函数要返回数据的内存地址是 %d" % id(result))
    # 函数返回的也是数据的引用
    return result


a = 10
print("a 变量保存数据的内存地址是 %d" % id(a))
receive = test(a)  # 调用test 函数，本质上传递的是实参保存的是数据的引用，而不是实参保存的数据的值
print("%s 的内存地址是 %d" % (receive, id(receive)))

# 不可变类型：数字型，字符串，元组， 可变类型：字典，列表
a_num = 1
a_str = "hello"
a_list = [1, 2, 3]
b_list = a_list
print(id(a_list), id(b_list))
a_list.append(4)
print(id(a_list), id(b_list))
# 字典的key只能使用不可变类型的数据
a_dict = {"name": "xm"}
print(id(a_dict))
a_dict["age"] = 18
a_dict[1] = "整数"
a_dict[(1,)] = "元组"
print(a_dict, id(a_dict))
# hash函数,把不可变类型数据变成整数
print(hash("hello"))
print(hash(1))
print(hash((1,)))

# 局部变量-定义在函数内部，只有某个函数可以使用 和 全局变量-定义在函数外部，所有函数均可使用
# 在其他的语言中，不推荐使用全局变量
global_var = 90  # 全局变量，定义在所有函数的上方，定义在函数调用前
g_num = 99  #  定义全局变量前一般加g_ 或 gl_前缀
num2 = 9


def demo1():
    num = 10  # 局部变量
    print("在demo1函数内部的变量是%d" % num)
    num = 20
    print(num)
    print(global_var)


def demo2():
    global gnum  # global 全局变量声明
    gnum = 0
    print(gnum)
    num2 = 100  # 在python中不允许直接修改全局变量的值，如果使用赋值语句，会在函数内部定义一个局部变量
    print("demo2函数内部的变量值是%d" % num2)


demo1()
demo2()
print(gnum)
