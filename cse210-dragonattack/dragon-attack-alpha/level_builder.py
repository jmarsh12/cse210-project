from ground import Ground
from village import Village
from gem import Gem
from missile import Missile
from flag import Flag
from game import constants
import arcade
from sheep import Sheep


class LevelBuilder:

    def __init__(self):
        self.village1 = Village()
        self.village2 = Village()
        self.village3 = Village()
        self.village4 = Village()
        self.village5 = Village()
        self.village6 = Village()
        self.village7 = Village()
        self.village8 = Village()
        self.village9 = Village()
        self.village10 = Village()

        self.platform_list = arcade.SpriteList()
        self.village_list = arcade.SpriteList()
        self.impenetrable_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.missile_list = []
        self.flag_list = arcade.SpriteList()
        self.sheep = Sheep()
        self.flag = Flag()

    def build_level_1(self):
        arcade.play_sound(constants.GAME_SONG_2)
        self._create_villages()
        self._create_ground_and_platforms()
        self._create_missiles()

    def _create_ground_and_platforms(self):

        for i in range(0, 30, 1):
            self.ground = Ground()
            self.ground.center_x = constants.TERRAIN_RADIUS * (i * 2)
            self.platform_list.append(self.ground)

        for i in range(40, 100, 1):
            self.ground = Ground()
            self.ground.center_x = constants.TERRAIN_RADIUS * (i * 2)
            self.platform_list.append(self.ground)

        for i in range(125, 250, 1):
            self.ground = Ground()
            self.ground.center_x = constants.TERRAIN_RADIUS * (i * 2)
            self.platform_list.append(self.ground)

        for i in range(60, 75, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 600
            self.platform_list.append(self.ground)
        self._place_gem(1125, 650)

        for i in range(100, 125, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 350
            self.platform_list.append(self.ground)

        for i in range(130, 140, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 700
            self.platform_list.append(self.ground)

        for i in range(85, 100, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 815
            self.platform_list.append(self.ground)

        for i in range(95, 120, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1050
            self.platform_list.append(self.ground)
        self._place_gem(1632, 1100)

        for i in range(150, 160, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 950
            self.platform_list.append(self.ground)
        self._place_gem(2567, 1000)

        for i in range(200, 220, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)

        for i in range(230, 240, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 550
            self.platform_list.append(self.ground)
        self._place_gem(4063, 600)

        for i in range(220, 235, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 0
            self.platform_list.append(self.ground)
        self._place_gem(3927, 50)

        for i in range(245, 260, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 250
            self.platform_list.append(self.ground)
        #     10th platform

        for i in range(300, 320, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)
        self._place_gem(5321, 450)

        for i in range(345, 355, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 600
            self.platform_list.append(self.ground)

        for i in range(390, 400, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 800
            self.platform_list.append(self.ground)
        self._place_gem(6698, 850)

        for i in range(415, 425, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 650
            self.platform_list.append(self.ground)
        self._place_gem(7140, 700)

        for i in range(400, 410, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)
        self._place_gem(6953, 450)

        for i in range(450, 475, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 330
            self.platform_list.append(self.ground)
        self._place_gem(8007, 380)

        for i in range(650, 660, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)

        for i in range(675, 680, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)
        self._place_gem(11543, 450)

        for i in range(695, 700, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)

        for i in range(685, 695, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 650
            self.platform_list.append(self.ground)
        self._place_gem(11798, 700)
        #     20th platform

        for i in range(715, 720, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)

        for i in range(735, 740, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)
        self._place_gem(12563, 450)

        for i in range(755, 760, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)

        for i in range(775, 780, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)

        for i in range(795, 800, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)

        for i in range(875, 900, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 350
            self.platform_list.append(self.ground)

        for i in range(915, 930, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 500
            self.platform_list.append(self.ground)
        self._place_gem(15708, 550)

        for i in range(940, 960, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 700
            self.platform_list.append(self.ground)

        for i in range(920, 935, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 900
            self.platform_list.append(self.ground)

        for i in range(950, 960, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1100
            self.platform_list.append(self.ground)
        #     30th platform

        for i in range(980, 985, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1250
            self.platform_list.append(self.ground)
        self._place_gem(16677, 1300)

        for i in range(1000, 1005, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1350
            self.platform_list.append(self.ground)

        for i in range(1020, 1025, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1450
            self.platform_list.append(self.ground)

        for i in range(1040, 1045, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1550
            self.platform_list.append(self.ground)
        self._place_gem(17697, 1600)

        for i in range(1060, 1065, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1700
            self.platform_list.append(self.ground)
        #     36th platform

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 150
            self.platform_list.append(self.ground)
        #     beginning of wall

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 250
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 350
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 450
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 550
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 650
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 750
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 850
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 950
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1050
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1150
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1250
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1350
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1450
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1550
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1650
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1750
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1850
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1950
            self.platform_list.append(self.ground)
        self._place_gem(18547, 2000)
        # end of wall

        for i in range(1125, 1130, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 850
            self.platform_list.append(self.ground)

        for i in range(1150, 1175, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 850
            self.platform_list.append(self.ground)
        self._place_gem(19788, 900)

        for i in range(1350, 1360, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 450
            self.platform_list.append(self.ground)

        for i in range(1375, 1390, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 650
            self.platform_list.append(self.ground)
        # 40th platform

        for i in range(1410, 1425, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 750
            self.platform_list.append(self.ground)
            self._place_gem(24072, 800)

        for i in range(1445, 1460, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 750
            self.platform_list.append(self.ground)

        for i in range(1480, 1495, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 750
            self.platform_list.append(self.ground)
            #     43rd platform

        for i in range(1610, 1615, 6):
            self.flag = Flag()
            self.flag.center_x = i * 17
            self.flag.center_y = 180
            self.flag_list.append(self.flag)

    def _create_villages(self):
        self.village1.center_x = 400
        self.village1.center_y = 152
        self.village_list.append(self.village1)

        self.village2.center_x = 2500
        self.village2.center_y = 152
        self.village_list.append(self.village2)

        self.village3.center_x = 5000
        self.village3.center_y = 152
        self.village_list.append(self.village3)

        self.village4.center_x = 7775
        self.village4.center_y = 420
        self.village_list.append(self.village4)

        self.village5.center_x = 15000
        self.village5.center_y = 440
        self.village_list.append(self.village5)

        self.village6.center_x = 19750
        self.village6.center_y = 940
        self.village_list.append(self.village6)

        self.village7.center_x = 25000
        self.village7.center_y = 152
        self.village_list.append(self.village7)

    def _create_missiles(self):
        for village in self.village_list:
            self.missile = Missile(village.center_x, village.center_y)
            self.missile_list.append(self.missile)

    def _place_gem(self, x, y):
        self.gem = Gem()
        self.gem.center_x = x
        self.gem.center_y = y
        self.gem_list.append(self.gem)

    def get_impenetrable_list(self):
        for village in self.village_list:
            self.impenetrable_list.append(village)
        for ground in self.platform_list:
            self.impenetrable_list.append(ground)
        return self.impenetrable_list

    def get_platforms(self):
        return self.platform_list

    def get_villages(self):
        return self.village_list

    def get_gems(self):
        return self.gem_list

    def get_missiles(self):
        return self.missile_list
