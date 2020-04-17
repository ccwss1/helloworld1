#  不使用继承时
# class Animal:
#     def eat(self):
#         print("eat")
#
#     def drink(self):
#         print("drink")
#
#     def run(self):
#         print("run")
#
#     def sleep(self):
#         print("sleep")
#
#
# class Dog:
#     def eat(self):
#         print("eat")
#
#     def drink(self):
#         print("drink")
#
#     def run(self):
#         print("run")
#
#     def sleep(self):
#         print("sleep")
#
#     def bark(self):
#         print("bark")
#
# wangcai = Dog()
# wangcai.eat()
# wangcai.drink()
# wangcai.bark()


# 使用继承时,继承实现代码的重用，相同的代码不需要重复编写
# 子类拥有父类的属性和方法，子类需要封装子类特有的属性和方法
# 继承具有传递性
class Animal1:
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog1(Animal1):
    def bark(self):
        print("bark")

    def eat(self):
        print("eat_new")  # 覆盖父类的方法，与父类方法完全不同时


class XiaoTianQuan(Dog1):
    def fly(self):
        print("I can fly")

    # 对父类的方法进行拓展
    def bark(self):
        # 1.针对子类特有的需求编写代码
        print("wangwangwang")
        # 使用super调用父类的方法，
        super().bark()
        print("emmmmm")
        #  Dog1.bark(self),也可以继承，但是不推荐使用


class Cat(Animal1):
    def catch(self):
        print("catch")


erha = XiaoTianQuan()
erha.drink()
erha.bark()
erha.eat()
erha.fly()

# 子类不能在自己的方法内部，直接访问父类的私有属性或私有方法
class A:
    def __init__(self):
        self.num1 = 1
        self.__num2 = 2

    def __test(self):
        print("私有方法%d %d" % (self.num1, self.__num2))

    def test(self):
        print("公有方法%d %d" % (self.num1, self.__num2))


class B(A):

    def demo(self):
        print(self.num1)
        # print(self.__num2)
        self.test()  # 可以通过父类的公有方法间接访问私有属性


b = B()
print(b.num1)
b.demo()
print(b)