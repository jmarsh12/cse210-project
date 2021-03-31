import arcade
from game import constants


class Gem(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.GEM_IMAGE)

        self.bottom = 0
        self.center_x = constants.GEM_RADIUS
        self.center_y = constants.GEM_HEIGHT
