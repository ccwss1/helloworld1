#  类就是具有一类属性或者方法的更大的封装，对象是类的实体化
#  类命名大驼峰命名法 属性-特征（name,age,height）
#  方法-行为(动词，run,eat) 类命名-名词提炼法

#  dir函数可以查看对象内的所有属性和方法


def demo():
    """这是一个测试函数"""
    print("hello")


#  __doc__ 查看函数的文档 ，__xx__ python内置的方法和属性
print(dir(demo()))
print(demo.__doc__)


#  方法几乎和函数一样，区别是必须用对象调用，第一个参数是self，封装在类class里
#  定义猫类
class Cat:
    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")




#  创建猫对象
tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()
print(tom)
print("%x" % id(tom))  # %x 16进制  %d 十进制

#  创建第二个猫对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
#  可以在类的外部给对象增加属性，虽然简单，但是不推荐使用
#  .属性名 赋值即可

lazy_cat.name = "大懒猫"
lazy_cat2 = lazy_cat
print(lazy_cat2)


