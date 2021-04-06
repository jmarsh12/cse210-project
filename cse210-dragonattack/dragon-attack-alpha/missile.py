import arcade
import constants


class Missile(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(constants.MISSILE_IMAGE)
        self.center_y = y
        self.center_x = x
        self.change_x = -5
        self.change_y = 10
