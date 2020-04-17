import pygame
import random

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1
FRAME_PRE_SEC = 60


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法, 如果父类不是object
        super(GameSprite, self).__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景"""

    def __init__(self, is_alt=False):
        super().__init__("./images/images/background.png")
        if is_alt is True:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        super().__init__("./images/images/ymz1.jpg", )
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除")
            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        super().__init__("./images/images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.x < 0:
            self.rect.x = 0

    def fire(self):
        # print("发射子弹。。。")
        bullet1 = Bullet()
        bullet2 = Bullet()
        bullet3 = Bullet()
        bullet1.rect.bottom = self.rect.y
        bullet1.rect.centerx = self.rect.centerx
        bullet2.rect.bottom = self.rect.y - 20
        bullet2.rect.centerx = self.rect.centerx
        bullet3.rect.bottom = self.rect.y - 40
        bullet3.rect.centerx = self.rect.centerx
        self.bullets.add(bullet1, bullet2, bullet3)

class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/images/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹被销毁")
        pass
