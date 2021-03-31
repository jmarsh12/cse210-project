import arcade
import time
import constants


class Sheep(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.SHEEP_IMAGE)
        self.center_x = (constants.SHEEP_RADIUS * 2) + 10
        self.center_y = (2 * constants.TERRAIN_HEIGHT) + constants.SHEEP_HEIGHT
        self.alive = True
        self.sheep_list = []
        self.boundary_right = 3

    def move_sheep(self):
        self.change_x = constants.SHEEP_SPEED 
        self.center_x += self.change_x
        if self.center_x >= 5000:
            self.alive = False
        if self.center_x == self.boundary_right:
            self.change_x *= -1
