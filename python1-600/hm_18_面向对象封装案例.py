#  把属性和方法封装到一个类中
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字是%s 体重是%.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1.0


xiaoming = Person("xiaoming", 75.0)
xiaoming.eat()
print(xiaoming)
xiaomei = Person("xiaomei", 45.0)  # 多个对象之间，属性互不干扰
xiaomei.run()
print(xiaomei)


# 摆放家具
class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "家具是%s,占地面积%.2f平米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s \n 总面积：%.2f \n 剩余面积：%.2f \n 家具列表: %s" \
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加%s" % item)
        if self.free_area >= item.area:
            self.item_list.append(item.name)
            self.free_area = self.free_area - item.area
            print("添加成功")
        else:
            print("%s剩余空间不足，无法添加" % item.name)


# 1.创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)

# 2.创建房子对象
house = House("两室一厅", 60)
print(house)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)


#  士兵突击
#  一个对象的属性可以是另一个类创建的对象
class Gun:

    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count = self.bullet_count + count

    def shoot(self):
        if self.bullet_count <= 0:
            print("%s 没有子弹了" % self.model)
            return
        else:
            self.bullet_count = self.bullet_count - 1
            print("%s发射成功,剩余%d子弹" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None  # 如果不知道初始值是什么，可以用None

    def fire(self):
        # is is not 是身份运算符，可以判断两个变量的
        # 引用对象/内存地址是否一致， ==用来判断变量的值是否相等
        # 针对None时，建议用is
        if self.gun is None:
            print("%s 没有枪" % self.name)
            return
        print("冲鸭")
        self.gun.add_bullet(4)
        self.gun.shoot()




#  创建枪对象
ak47 = Gun("ak47")


#  创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()

print(xusanduo.gun)


#  私有属性和私有方法
#  对象的某些属性和方法，希望只在对象的内部使用，不希望在外部访问到
#  在属性或方法前加__
class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("xiaofang")
#  print(xiaofang.__age) 私有属性
#  xiaofang.__secret() 私有方法
#  伪私有属性，实际上是对私有属性进行了处理，在日常开发中不要使用
print(xiaofang._Women__age)
xiaofang._Women__secret()
