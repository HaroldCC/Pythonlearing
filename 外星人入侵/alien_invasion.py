# 重构之后，该程序内不再需要该模块
# import sys

import pygame

# 包含函数模块
import game_functions as gf

from pygame.sprite import Group
"""创建一个编组（group），用于存储所有有效的子弹，
以便能够管理发射出去的所有子弹。
这个编组将是pygame.sprite.Group 类的一个实例；
pygame.sprite.Group 类类似于列表，
但提供了有助于开发游戏的额外功能。
在主循环中，我们将使用这个编组在屏幕上绘制子弹，
以及更新每颗子弹的位置
"""

# 包含游戏设置类模块
from settings import Settings
# 包含飞船类模块
from ship import Ship
# 包含统计信息模块
from game_stats import GameStats
# 包含按钮模块
from button import Button
# 包含记分牌模块
from score_board import Scoreboard
'''为创建一行外星人，
首先在alien_invasion.py中创建一个名为aliens 的空编组，
用于存储全部外星人，再调用game_functions.py中创建外星人群的函数,
由于我们不再在alien_invasion.py中直接创建外星人，
因此无需在这个文件中导入Alien 类
##############################################3
#包含外星人类模块
from alien import Alien
'''


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    # 将设置赋给ai_settings
    ai_settings = Settings()
    # (没有settings版本)screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    # 创建Play按钮实例
    play_button = Button(ai_settings, screen, "Play")

    # 设置背景色
    # (没有settings版本)bg_color = (230,230,230)

    # 创建飞船实例
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    score_board = Scoreboard(ai_settings, screen, stats)
    '''不再创建
    # 创建外星人实例
    alien = Alien(ai_settings,screen)
    '''

    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()

    # 创建外星人群
    gf.creat_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        """
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        """
        # 上面可简化为 ↓
        gf.check_events(ai_settings, screen, stats, score_board, play_button,
                        ship, aliens, bullets)

        if stats.game_active:
            # 在每次循环时都调用飞船移动标志的判断
            ship.update()

            # 子弹
            # bullets.update()

            # 删除已消失的子弹
            '''
            ######重构至game_functions中的update_bullets()######
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            #下面这个语句是检验当子弹到达顶部后是否将子弹从bullets中删除
            #print(len(bullets))
            '''
            gf.update_bullets(ai_settings, screen, stats, score_board, ship,
                              aliens, bullets)

            # 外星人位置
            gf.update_aliens(ai_settings, stats, score_board, screen, ship,
                             aliens, bullets)
        """
        #每次循环都重绘屏幕
        #(没有settings版本)screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        #显示飞船
        ship.blitme()

        #让最近绘制的屏幕可见
        pygame.display.flip()
        """
        # 上面代码可简化为 ↓
        gf.update_screen(ai_settings, screen, stats, score_board, ship, aliens,
                         bullets, play_button)


run_game()
