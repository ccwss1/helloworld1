def say_hello():
    print("hello")


print("test module")


class Dog(object):
    def run(self):
        print("I can run")


if __name__ =="__main__":
    # __name__在源文件是__main__,在被导入时是模块名
    print(__name__)
    # 模块测试代码，在文件被导入时，不需要执行
    say_hello()
