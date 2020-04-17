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


name = "小明"