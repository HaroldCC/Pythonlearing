class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        # self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        # self.bullet_speed_factor = 3
        self.bullet_width = 300  # 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed =  10 # 3

        # 外星人设置
        # self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        # self.fleet_direction = 1

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1

        # 外星人点数的提高速度
        self.score_scale = 1.5
        '''
        我们添加了设置speedup_scale ，
        用于控制游戏节奏的加快速度：2表示玩家每提高一个等级，
        游戏的节奏就翻倍；1 表示游戏节奏始终不变。
        将其设置为1.1能够将游戏节奏提高到够快，让游戏既有难度，
        又并非不可完成。最后，我们调用initialize_dynamic_settings() ，
        以初始化随 游戏进行而变化的属性
        '''
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
