import arcade
import constants
from random import randint


class Missile(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(constants.MISSILE_IMAGE)
        self.center_y = y
        self.center_x = x
        self.change_x = self._set_x_velocity()
        self.change_y = self._set_y_velocity()

    @staticmethod
    def _set_x_velocity():
        velocity = randint(-10, 10)
        if velocity == 0:
            velocity = -5
        return velocity

    @staticmethod
    def _set_y_velocity():
        velocity = randint(5, 15)
        return velocity