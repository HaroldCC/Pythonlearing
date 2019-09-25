import sys

import pygame

import json

from bullet import Bullet

from alien import Alien

from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        '''
        ######此处重构为fire_bullet()######
        #创建一颗子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullets_allowed:
            #检查未消失的子弹是否小于设置中允许的子弹数
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
        '''
        fire_bullet(ai_settings, screen, ship, bullets)
    # 当按下'q'键将关闭程序
    elif event.key == pygame.K_q:
        # 在游戏推出前保存最高分
        # with open('highest_score.json') as f_obj:
            # highest_score = json.load(f_obj)
            # if high_score > highest_score:
                # json.dump(high_score,f_obj)

        sys.exit(0)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, score_board, play_button, ship,
                 aliens, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 检测是否为退出事件
        if event.type == pygame.QUIT:
            # 添加默认参数0，将不会显示异常
            sys.exit(0)

        # 检测是否为按键事件
        elif event.type == pygame.KEYDOWN:
            '''
            ######此处重构为check_keydown_events()######
            #判断右移按键，向右移动飞船
            if event.key == pygame.K_RIGHT:
                #添加飞船移动标志后，将不再需要下一行
                #ship.rect.centerx += 1
                #当按下按键，直接将飞船移动标志改为True
                ship.moving_right = True
                #左移
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            '''
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        # 检测松开按键事件
        elif event.type == pygame.KEYUP:
            '''
            ######此处重构为check_keyup_events()######
            #当松开按键后，飞船将不再移动，移动标志改为False
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            '''
            check_keyup_events(event, ship)

        # 检测是否是鼠标点击事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, score_board,
                              play_button, ship, aliens, bullets,
                              mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, score_board, play_button,
                      ship, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    '''
    ###此处将更改游戏开始后如果点击按钮区域仍回重新开始的错误###
    if play_button.rect.collidepoint(mouse_x,mouse_y):
    '''
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        score_board.prep_score()
        score_board.prep_high_score()
        score_board.prep_level()

        # 显示剩余的飞船
        score_board.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, score_board, ship, aliens,
                  bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""

    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示飞船
    ship.blitme()
    '''不再需要
    #显示外星人
    alien.blitme()
    '''
    aliens.draw(screen)

    # 显示得分
    score_board.show_score()

    # 若果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, score_board, ship, aliens,
                   bullets):
    """更新子弹的位置，并消除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    '''
    ######重构为check_bullet_alien_collisions()######
    #检查是否有子弹击中了外星人
    #如果击中，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    '''
    check_bullet_alien_collisions(ai_settings, screen, stats, score_board,
                                  ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, score_board,
                                  ship, aliens, bullets):
    """相应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 计分
    if collisions:
        '''
        当前，我们的代码可能遗漏了一些被消灭的外星人。
        例如，如果在一次循环中有两颗子弹射中了外星人，
        或者因子弹更宽而同时击中了多个外星人，
        玩家将只能得到一个被消灭的外星人的点数。
        为修复这种问题，我们来调整检测子弹和外星人碰撞的方式。
        在check_bullet_alien_collisions() 中，
        与外星人碰撞的子弹都是字典collisions 中的一个键；
        而与每颗子弹相关的值都是一个列表，其中包含该子弹撞到的外星人。
        我们遍历字典collisions ，
        确保将消灭的每个外星人的点数都记入得分
        stats.score += ai_settings.alien_points
        score_board.prep_score()
        ####代码替换为下面代码
        '''
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            score_board.prep_score()

        # 检查最高得分
        check_high_score(stats, score_board)

    if len(aliens) == 0:
        # 删除现有的所有子弹
        bullets.empty()
        # 外星人全部被消灭，提高一个等级
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        score_board.prep_level()
        # 创建一个新的外星人群
        creat_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_hight, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) -
                         ship_hight)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def creat_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    '''
    ######重构为get_number_aliens_x()######
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    '''
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)
    """
    #####替换为创建外星人群######
    #创建第一行外星人
    for alien_number in range(number_aliens_x):
        '''
        ######此处重构为creat_alien()######
        #创建一个外星人并将其加入当前行
        alien = Alien(ai_settings,screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
        '''
        creat_alien(ai_settings,screen,aliens,alien_number)
    """

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, score_board, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1

        # 更新记分牌
        score_board.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕低端中央
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False

        # 游戏结束后显示光标
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, score_board, screen,
                        ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 如果任一飞船触碰到屏幕底部，像飞船被撞一样处理
            ship_hit(ai_settings, stats, score_board, screen, ship, aliens,
                     bullets)
            break


def update_aliens(ai_settings, stats, score_board, screen, ship, aliens,
                  bullets):
    """检查是否有外星人位于屏幕边缘，并更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, score_board, screen, ship, aliens,
                 bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, score_board, screen, ship, aliens,
                        bullets)


def check_high_score(stats, score_board):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()
