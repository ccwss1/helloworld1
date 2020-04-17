class Cat:
    def __init__(self, name):
        print("这是一个初始化方法")
        #  self.属性名 = 属性的初始值
        self.name = name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    #  __str__方法，必须返回字符串,打印对象时希望打印一些自定义的内容
    def __str__(self):
        return "%s 调用str方法" % self.name

    #  对象被销毁前，自动调用__del__方法
    def __del__(self):
        print("要被销毁了")


tom = Cat("tom")  # __init__ 专门用来定义类的属性，在创建对象时会自动调用
tom.eat()
print(tom)
del tom
print("-"*50)


