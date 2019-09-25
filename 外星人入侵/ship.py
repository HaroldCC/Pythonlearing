import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """飞船类"""
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(
            r'C:\Users\19211\Desktop\python\.vscode\外星人入侵\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值，
        # rect 的centerx 等属性只能存储整数值
        # 因此要做如下操作
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            """self.rect.right 返回飞船外接矩形的右边缘的 x 坐标，
            如果这个值小于self.screen_rect.right 的值，
            就说明飞船未触及屏幕右边缘
            """
            # 更新飞船的center值，而不是rect
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            """如果rect 的左边缘的 x 坐标大于零，就说明飞船未触及屏幕左边缘"""
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        """注释：在方法update() 中，
        我们添加了一个if 代码块而不是elif 代码块，
        这样如果玩家同时按下了左右箭头键，
        将先增大飞船的rect.centerx 值，再降低这个值，
        即飞船的位置保持不变。
        如果使用一个elif 代码块来处理向左移动的情况，
        右箭头键将始终处于优先地位。从向左移 动切换到向右移动时，
        玩家可能同时按住左右箭头键，
        在这种情况下，前面的做法让移动更准确。
        """
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
