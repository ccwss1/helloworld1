# 类是一个特殊的对象，类属性用来记录与这个类相关的特征
# 类方法针对类对象定义的方法，可以访问类属性或者调用其他的类方法
class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    def __init__(self, name):
        self.name = name
        Tool.count += 1

    # 类方法，调用类属性或者类方法,类名.()
    @classmethod
    def show_tool_count(cls):
        print("这是类方法，调用的类属性是%d" % cls.count)

    # 实例方法，调用实例属性或实例方法,类对象.()
    def show_name(self):
        print("实例方法---工具的名字是%s" % self.name)

    # 静态方法，既不需要调用实例属性，也不需要调用类属性,类名.()
    @staticmethod
    def run():
        print("静态方法--工具好使")


tool1 = Tool("斧头")
tool2 = Tool("榔头")
print(Tool.count)
Tool.run()
tool1.show_name()
# 属性的向上查找机制，先查找对象属性，如果没有找到，则向上查找类属性
# 此种方法不推荐
# print(tool1.count)
Tool.show_tool_count()


# 案例
class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        print("%s game begin" % self.player_name)


Game.show_help()
Game.show_top_score()
xiaoming = Game("xiaoming")
xiaoming.start_game()
