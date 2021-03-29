import constants
import arcade
from dragon import Dragon


class HealthBar():

    def __init__(self):
        self.dragon = Dragon()
        self.heath_remaining = self.dragon.health
        self.center_x = self.dragon.get_center_x()
        self.center_y = y = self.dragon.get_center_y()
        self.height = constants.HEALTH_BAR_HEIGHT
        self.width = constants.HEALTH_BAR_LENGTH
        self.color = arcade.color.GO_GREEN
        self.change_x = 0
        self.change_y = constants.GRAVITY

    def draw_health_bar(self):
        if self.dragon.health == constants.DRAGON_MAX_HEALTH:
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def move_up(self):
        self.change_y = constants.PLAYER_JUMP_SPEED
        self.center_y += self.change_y

    def move_down(self):
        self.change_y = -(constants.PLAYER_JUMP_SPEED / 2)
        self.center_y += self.change_y

    def move_left(self):
        self.change_x = -constants.PLAYER_MOVEMENT_SPEED
        self.center_x += self.change_x

    def move_right(self):
        self.change_x = constants.PLAYER_MOVEMENT_SPEED
        self.center_x += self.change_x
