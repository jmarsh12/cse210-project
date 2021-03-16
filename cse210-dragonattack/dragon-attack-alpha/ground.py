import arcade
import constants

class Ground(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.GROUND_IMAGE)

        self.bottom = 0
        self.center_x = constants.TERRAIN_RADIUS
        self.center_y = constants.TERRAIN_HEIGHT
