import arcade
import constants
from missile import Missile


class Village(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.VILLAGE_IMAGE)
        self.bottom = 80
