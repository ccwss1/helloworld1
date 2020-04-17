# 参数可以传递数据，返回值返回函数执行的结果
def measure():
    print("测量开始。。。")
    temp = 39
    wetness = 50
    print("测量结束。。。")
    return temp, wetness


result = measure()
print(result)  # 返回多个变量时，返回元组
print(result[0])
#  可以使用多个变量，一次接收函数返回结果
#  变量个数与元组数量一致
gl_temp, gl_wetness = measure()
print(gl_temp)

# 交换两个数字-面试题
a = 8
b = 99
# 解法1
c = a
a = b
b = c
#  解法2
a = a + b
b = a - b
a = a - b
#  解法3-python专有
a, b = (b, a)
print(a, b)


# 参数,函数内部的赋值语句，不会影响函数外部的实参
def demo(num, num_list):
    num = 100
    num_list = [6, 7, 8]
    print("num = %d" % num)
    print(num_list)


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num, gl_list)


#  参数,函数内部使用方法（append等）更改可变类型数据时，会更改外部实参的值
def demo1(num_list1):
    num_list1.append(9)
    print(num_list1)


gl_list1 = [1, 2, 3]
demo1(gl_list1)
print(gl_list1)


#  列表的+=不是相加再赋值，本质上是调用列表的extend方法
def demo2(num2, num_list2, num_list22):
    num2 += num2
    num_list22 = num_list22 + num_list22
    print(num_list22)
    num_list2 += num_list2
    print(num2, num_list2)


gl_num2 = 9
gl_list2 = [1, 3, 5]
gl_list22 = [2, 4, 8]
demo2(gl_num2, gl_list2, gl_list22)
print(gl_num2, gl_list2, gl_list22)

#  缺省参数，设置默认值的参数(一般是常见的值)，如果调用时不赋值，则使用默认值，
#  简化函数的调用,缺省参数应该在参数列表的末尾,调用时需要指定缺省参数的参数名
gl_list3 = [9, 8, 6]
gl_list3.sort()
print(gl_list3)
gl_list3.sort(reverse=True)
print(gl_list3)


def print_info(name, title, gender=True):
    """

    :param title:
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "boy"
    if not gender:
        gender_text = "girl"

    print("[%s]%s is %s" % (title, name, gender_text))


print_info("xiaoming", "wendang")
print_info("xm", "hhh", gender=False)


#  多值参数，*args 存放元组参数，**kwargs 存放字典参数
def demo4(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


#  demo4(1)
#  demo4(1, 2, 3, 4, 5)
demo4(1, 2, 3, 4, name="xm", age=18)


# 计算任意多个数字的和
def sum_numbers(*args):
    num = 0
    print(args)
    for i in args:
        num = num + i
    return num


result = sum_numbers(1, 2, 3)
print(result)

#  拆包
def demo6(*args, **kwargs):
    print(args)
    print(kwargs)


gl_dict = {"name": "xming"}
gl_tup = (1, 2, 3)
demo6(*gl_tup, **gl_dict)