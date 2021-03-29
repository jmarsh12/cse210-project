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
        self.texture_list_left = []
        self.texture_list_left.append(arcade.load_texture(constants.FLYING_LEFT_0))
        self.texture_list_left.append(arcade.load_texture(constants.FLYING_LEFT_1))
        self.texture_list_left.append(arcade.load_texture(constants.FLYING_LEFT_2))
        self.texture_list_left.append(arcade.load_texture(constants.FLYING_LEFT_3))
        self.texture_list_left.append(arcade.load_texture(constants.FLYING_LEFT_4))
        self.texture_list_left.append(arcade.load_texture(constants.FLYING_LEFT_5))
        self.texture_list_left.append(arcade.load_texture(constants.FLYING_LEFT_6))
        self.texture_list_left.append(arcade.load_texture(constants.FLYING_LEFT_7))
        self.texture_list_left.append(arcade.load_texture(constants.FLYING_LEFT_8))
        self.texture_list_right = []
        self.texture_list_right.append(arcade.load_texture(constants.FLYING_RIGHT_0))
        self.texture_list_right.append(arcade.load_texture(constants.FLYING_RIGHT_1))
        self.texture_list_right.append(arcade.load_texture(constants.FLYING_RIGHT_2))
        self.texture_list_right.append(arcade.load_texture(constants.FLYING_RIGHT_3))
        self.texture_list_right.append(arcade.load_texture(constants.FLYING_RIGHT_4))
        self.texture_list_right.append(arcade.load_texture(constants.FLYING_RIGHT_5))
        self.texture_list_right.append(arcade.load_texture(constants.FLYING_RIGHT_6))
        self.texture_list_right.append(arcade.load_texture(constants.FLYING_RIGHT_7))
        self.texture_list_right.append(arcade.load_texture(constants.FLYING_RIGHT_8))
        self._facing_left = True
        self._move_up = True

        self._frame = 0

    def move_up(self):
        self.change_y = constants.PLAYER_JUMP_SPEED
        self.center_y += self.change_y
        self._move_up = True
        self._frame = (self._frame + 1) % 9

    def move_down(self):
        self.change_y = -(constants.PLAYER_JUMP_SPEED / 2)
        self._move_up = False
        self._frame = (self._frame + 1) % 9

    def move_left(self):
        self.change_x = -constants.PLAYER_MOVEMENT_SPEED
        self._facing_left = True
        self._frame = (self._frame + 1) % 9

    def move_right(self):
        self.change_x = constants.PLAYER_MOVEMENT_SPEED
        self._facing_left = False
        self._frame = (self._frame + 1) % 9

    def lose_health(self):
        if self.health <= 0:
            self.health = 0
        else:
            self.health -= 100

    def draw(self):

        if self._facing_left:
            self.texture_list_left[self._frame].draw_scaled(self.center_x, self.center_y)
        else:
            self.texture_list_right[self._frame].draw_scaled(self.center_x, self.center_y)

        if self._move_up and self._facing_left:
            self.texture_list_left[self._frame].draw_scaled(self.center_x, self.center_y)
        elif self._move_up == False and self._facing_left == False:
            self.texture_list_right[self._frame].draw_scaled(self.center_x, self.center_y)

    def get_center_x(self):
        return self.center_x

    def get_center_y(self):
        return self.center_y

    def get_health_remaining(self):
        return self.health

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
