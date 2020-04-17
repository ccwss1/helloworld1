# 异常
# 简单的捕获异常的方法
# try:
#     # 不能确定正确执行的代码
#     num = int(input("请输入一个整数"))
# except:
#     # 错误的代码处理
#     print("需要输入一个整数")

# 捕获错误类型
try:
    num1 = int(input("请输入一个整数"))
    result = 8 / num1
    print(result)
# 解释器抛出异常时，最后一行错误信息的第一个单词就是错误类型
# except ZeroDivisionError:
#     print("除0错误")
except ValueError:
    print("输入类型错误")
# 捕获未知错误,希望程序无论出现任何错误都不会因为异常而终止
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("没有异常才会执行的代码")
finally:
    print("无论是否出现异常，都会执行的代码")
print("-" * 50)


# 异常的传递
def demo1():
    return int(input("please input an integer"))


def demo2():
    return demo1()


# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())
except Exception as result:
    print("未知错误%s " % result)


# 主动抛出异常
def input_password():
    password = input("请输入密码：")
    if len(password) >= 8:
        return password
    print("主动抛出异常")
    # 创建异常对象，主动抛出异常
    ex = Exception("密码长度不够")
    raise ex


try:
    print(input_password())

    # 捕获异常
except Exception as result:
    print(result)
