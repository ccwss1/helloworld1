# 每一个.py结尾的文件都是一个模块，全局变量，类，函数都是模块提供给外界的工具
# 要想使用工具包中的工具，需要先导入这个模块
# import as 指定别名
# from import 局部导入,如果两个模块导入同名的函数，后导入的会覆盖新导入的，所以此种方法不推荐
# 文件起名时，不要和系统模块重名


# from hm_24_testmodule1 import say_hello
# from hm_24_testmodule1 import Dog
# import random
# # 查看模块路径
# print(random.__file__)
# wangcai = Dog()
# wangcai.run()
# say_hello()


# 文件被导入时，所有没有缩进的代码都将被执行一遍
import hm_24_testmodule1