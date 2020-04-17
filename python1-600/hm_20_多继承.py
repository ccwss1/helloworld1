# 多继承
# 如果父类之间存在同名的属性或方法，则应该尽量避免使用多继承


# class A:
#
#     def test(self):
#         print("test method")
#
#
# class B:
#
#     def demo(self):
#         print("demo method")
#
#
# class C(A, B):
#     pass
#
#
# c = C()
# c.test()
# c.demo()

# 如果父类之间存在同名的属性或方法，则应该尽量避免使用多继承
class A(object):

    def test(self):
        print("test--1 method")

    def demo(self):
        print("demo--1 method")


class B:

    def demo(self):
        print("demo--2 method")


class C(B, A):
    pass


c = C()
c.test()
c.demo()
print(C.__mro__)
print(dir(A))
# method resolution order 多继承时按照mro的输出顺序从左到右查找

# object是所有类的基类，python3中会默认，python2中如果不指定基类，则不默认
# 为了保证代码同时在python2和python3运行，需要指定object


# 多态，继承，封装 面向对象的三大特性
# 多态：不同的子类对象调用相同的父类方法，产生不同的执行结果
# 以继承和重写父类方法为前提
class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍" % self.name)


class Xiaotianquan(Dog):
    def game(self):
        super(Xiaotianquan, self).game()
        print("%s飞到天上去玩" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s play with %s" % (self.name, dog.name))
        dog.game()


erha = Xiaotianquan("wangcai")
xiaoming = Person("xiaoming")
xiaoming.game_with_dog(erha)

