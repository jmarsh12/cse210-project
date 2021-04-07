import arcade
import constants


class Village(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.VILLAGE_IMAGE)
        self.bottom = 80
