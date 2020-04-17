import random

is_continue = 1
while is_continue :

    player = int(input("请输入您要出的拳：石头1/剪刀2/布3"))
    computer = random.randint(1,3)
    print("玩家要出的拳是：%d , 电脑要出的拳是 %d" % (player,computer))

    if ((player == 1 and computer == 2)
            or (player == 2 and computer == 3)
            or (player == 3 and computer == 1)):

        print("欧耶，电脑弱爆了！")

    elif player == computer:

        print("真是心有灵犀呢，平局了")

    else :

        print("不要走，决战到天亮")

    is_continue = int(input("您想继续吗，继续1/不继续0"))
