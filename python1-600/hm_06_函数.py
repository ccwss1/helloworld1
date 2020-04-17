# 九九乘法表
def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            result = col * row
            print("%d * %d = %d " % (col, row, result), end='\t')
            col = col + 1
        print('')
        row = row + 1


def say_hello():
    """ 函数的注释用三个引号写在函数内部，函数定义的代码应与其他代码隔两个空行"""
    print("hello friend")
    print("hello sister")


def sum_2_num(num1, num2):
    """ 对两个数字求和 , num1 和 num2 是形参，5，6是实参
    形参：参数数量和在函数内部当成变量使用
    实参：传递数据
    """
    # num1 = 10
    # num2 = 20
    result = num1 + num2
    # print("%d + %d = %d" % (num1, num2, result))
    # 可以使用返回值告诉调用一方函数计算的结果
    return result


sum2 = sum_2_num(5, 6)
print(sum2)


def test1():
    print("*")
    print("test1")
    print("*")


def test2():
    """ 函数嵌套"""
    print("--")
    print("test2")
    test1()
    print("--")


# 分隔线演练
def print_line(char: object, times: object) -> object:
    print(char * times)


""" 遇到需求变化，不要轻易更改已经改好的函数，需要冷静思考"""


def print_lines(char, times, nums):
    """打印多行分隔线

    :param char: 分隔线使用的字符
    :param times: 分隔符的次数
    :param nums: 打印的行数
    """
    num = 0
    while num < nums:
        print_line(char, times)
        num = num+1


print_lines("*", 5, 10)
