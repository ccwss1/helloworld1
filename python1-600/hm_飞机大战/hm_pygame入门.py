import pygame
from plane_sprites import *

pygame.init()
# 编写游戏的代码
# print("游戏的代码。。。")
# hero_dict = pygame.Rect(2, 3, 4, 5)
# print("英雄的坐标 %d %d" % (hero_dict.x, hero_dict.y))
# print("英雄的宽度和高度 %d %d" % (hero_dict.width, hero_dict.height))
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
bg = pygame.image.load("./images/images/background.png")
screen.blit(bg, (0, 0))
# 绘制英雄的飞机
hero = pygame.image.load("./images/images/me1.png")
screen.blit(hero, (200, 500))
# 更新图像
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()
# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)
bg_rect = pygame.Rect(0, 0, 480, 700)

# 创建敌机的精灵
enemy = GameSprite("./images/images/enemy1.png")
enemy1 = GameSprite("./images/images/ymz.jpg", 2)
# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)
screen.blit(bg, (0, 0))
# 游戏循环 -> 意味着游戏的正式开始
while True:
    # 可以指定循环体内部代码执行的频率
    clock.tick(60)
    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
    # 监听事件
    for euent in event_list:
        if euent.type == pygame.QUIT:
            print("退出游戏。。。")
            # 卸载所有模块
            pygame.quit()
            # 直接终止当前的程序
            exit()
    # 2.修改飞机的位置
    hero_rect.y -= 1
    bg_rect.y += 1
    if hero_rect.y <= -126:
        hero_rect.y = 700
    # 3.调用blit绘制图像位置
    screen.blit(bg, bg_rect)
    screen.blit(hero, hero_rect)

    # 让组中所有精灵更新位置
    enemy_group.update()
    # 在screen上绘制所有的精灵
    enemy_group.draw(screen)
    # 4.更新显示
    pygame.display.update()

pygame.quit()
