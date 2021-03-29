import arcade
import constants
from fire import Fire


class Dragon(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.DRAGON_IMAGE)
        self.fire = None
        self.health = constants.DRAGON_MAX_HEALTH
        self.center_x = (constants.DRAGON_RADIUS * 2) + 10
        self.center_y = (2 * constants.TERRAIN_HEIGHT) + constants.DRAGON_HEIGHT
        self.change_x = 0
        self.change_y = 0
        self.fire_regen = 100
        self.fire_list = []

    def move_up(self):
        self.change_y = constants.PLAYER_JUMP_SPEED
        self.center_y += self.change_y

    def move_down(self):
        self.change_y = -(constants.PLAYER_JUMP_SPEED / 2)

    def move_left(self):
        self.change_x = -constants.PLAYER_MOVEMENT_SPEED

    def move_right(self):
        self.change_x = constants.PLAYER_MOVEMENT_SPEED

    def get_center_x(self):
        return self.center_x

    def get_center_y(self):
        return self.center_y

    def move_fire(self):
        if len(self.fire_list) > 0:
            for i in range(len(self.fire_list)):
                self.fire_list[i].center_x += self.fire.change_x
                self.fire_list[i].center_y += self.fire.change_y
                self.fire_list[i].change_y = -constants.FIRE_SPEED
                self.fire_list[i].change_x = constants.FIRE_SPEED
        else:
            pass

    def shoot_fire(self):
        if self.fire_regen > 0:
            arcade.play_sound(constants.FIRE_SOUND)
            self.fire = Fire(self.center_x, self.center_y)
            self.fire_list.append(self.fire)
        self.fire_regen -= constants.FIRE_REGEN_SPEED

    def regenerate_fire(self):
        if self.fire_regen < constants.MAX_FIRE:
            self.fire_regen += constants.FIRE_REGEN_SPEED
        else:
            self.fire_regen = constants.MAX_FIRE
