# 设计模式是针对某一特定问题的成熟的解决方案
# 单例设计模式，让类创建的对象，在系统中只有唯一的一个实例
# 每一次用类创建的对象，没存地址是相同的，比如播放器，回收站
class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.创建对象时，new方法会被自动调用
        print("创建对象，分配空间")
        # 2.为对象分配空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        # 返回对象的引用
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag is False:
            print("播放器初始化")
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)