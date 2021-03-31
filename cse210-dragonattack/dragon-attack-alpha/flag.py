from game import constants
import arcade


class Flag(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.FLAG_IMAGE)

        self.bottom = 0
        self.center_x = constants.FLAG_RADIUS
        self.center_y = constants.FLAG_HEIGHT
