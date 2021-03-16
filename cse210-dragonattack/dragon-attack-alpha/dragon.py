import arcade
import constants


class Dragon(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.DRAGON_IMAGE)
        self.center_x = (constants.DRAGON_RADIUS * 2) + 10
        self.center_y = (2 * constants.TERRAIN_HEIGHT) + constants.DRAGON_HEIGHT
