import arcade
import constants


class Fire(arcade.Sprite):
    def __init__(self, x, y, identifier):
        if identifier == 0:
            super().__init__(constants.FIRE_IMAGE)
            self._identifier = 0
            self.change_x = constants.FIRE_SPEED
            self.change_y = -constants.FIRE_SPEED
            self.center_y = y
            self.center_x = x + constants.DRAGON_RADIUS + constants.FIRE_RADIUS
        elif identifier == 1:
            super().__init__(constants.FIRE_MIRROR_IMAGE)
            self._identifier = 1
            self.change_x = -constants.FIRE_SPEED
            self.change_y = -constants.FIRE_SPEED
            self.center_y = y
            self.center_x = x - constants.DRAGON_RADIUS - constants.FIRE_RADIUS
        # self.dragon = Dragon()

    def move_fire(self):
        if self._identifier == 0:
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.change_y = -constants.FIRE_SPEED
            self.change_x = constants.FIRE_SPEED
        elif self._identifier == 1:
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.change_y = -constants.FIRE_SPEED
            self.change_x = -constants.FIRE_SPEED

    @staticmethod
    def blow_fire(self):
        arcade.play_sound(constants.FIRE_SOUND)
