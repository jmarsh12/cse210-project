import arcade
import constants
from dragon import Dragon


class Fire(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(constants.FIRE_IMAGE)
        dragon = Dragon()
        self.center_y = y
        self.center_x = x + constants.DRAGON_RADIUS + constants.FIRE_RADIUS
        self.change_x = constants.FIRE_SPEED
        self.change_y = -constants.FIRE_SPEED

