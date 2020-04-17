# 递归,自己调用自己，需要设置中止条件,类似于数学归纳法
def sum_number(num):
    print(num)
    if num == 1:
        return 1
    temp = sum_number(num-1)
    print("finish %d" % num)
    return num + temp


result = sum_number(6)
print(result)