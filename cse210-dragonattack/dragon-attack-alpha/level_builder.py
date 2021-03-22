from ground import Ground
from game import constants
import arcade


class LevelBuilder(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.GROUND_IMAGE)
        # self.ground = Ground()
        # self.center_x = constants.TERRAIN_RADIUS
        # self.center_y = constants.TERRAIN_HEIGHT
        self.platform_list = []

    def build_level_1(self):

        for i in range(60, 75, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 600
            self.platform_list.append(self.ground)

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
        #     TODO: put gold on top of this ledge

        for i in range(150, 160, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 950
            self.platform_list.append(self.ground)
        #     TODO: put gold on top of this ledge

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
        #     TODO: put gold on top of this ledge

        for i in range(220, 235, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 0
            self.platform_list.append(self.ground)
        # TODO: put gold on top of this ledge

        for i in range(245, 260, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 250
            self.platform_list.append(self.ground)

        for i in range(300, 320, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)
        #     TODO: put gold on top of this ledge

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
        #     TODO: put gold on top of this ledge

        for i in range(415, 425, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 650
            self.platform_list.append(self.ground)
        #     TODO: put gold on top of this ledge

        for i in range(400, 410, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.platform_list.append(self.ground)
        #     TODO: put gold on top of this ledge

        for i in range(450, 475, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 330
            self.platform_list.append(self.ground)
        #     TODO: put gold on top of this ledge

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
        #     TODO: put gold on top of this ledge

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
        #     TODO: put gold on top of this ledge

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
        #     TODO: put gold on top of this ledge

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

        for i in range(980, 985, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1250
            self.platform_list.append(self.ground)

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

        for i in range(1060, 1065, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1700
            self.platform_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 150
            self.platform_list.append(self.ground)

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
        #     TODO: put coin on top of wall

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

        for i in range(1410, 1425, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 750
            self.platform_list.append(self.ground)

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
    #         TODO: add ending flag at range(1610, 1615, 6)
