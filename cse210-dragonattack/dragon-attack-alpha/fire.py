import arcade
import constants
# from dragon import Dragon


class Fire(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(constants.FIRE_IMAGE)
        # self.dragon = Dragon()
        self.center_y = y
        self.center_x = x + constants.DRAGON_RADIUS + constants.FIRE_RADIUS
        self.change_x = constants.FIRE_SPEED
        self.change_y = -constants.FIRE_SPEED

    # def move_fire(self):
    #     if len(self.dragon.fire_list) > 0:
    #         for i in range(len(self.dragon.fire_list)):
    #             self.dragon.fire_list[i].center_x += self.change_x
    #             self.dragon.fire_list[i].center_y += self.change_y
    #             self.dragon.fire_list[i].change_y = -constants.FIRE_SPEED
    #             self.dragon.fire_list[i].change_x = constants.FIRE_SPEED

    @staticmethod
    def blow_fire(self):
        arcade.play_sound(constants.FIRE_SOUND)
