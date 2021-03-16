import arcade
import constants
from ground import Ground
from dragon import Dragon
from fire import Fire


class Game(arcade.Window):

    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, "Dragon Attack")
        arcade.set_background_color(arcade.color.ALICE_BLUE)

        self.dragon = Dragon()
        self.fire = None
        self.ground = None
        self.ground_list = []
        self.fire_list = []
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.space_pressed = False
        self.change_x = 0
        self.change_y = 0

    def on_draw(self):
        arcade.start_render()

        for i in self.ground_list:
            i.draw()
            # print(len(self.ground_list))
        self.dragon.draw()
        if len(self.fire_list) > 0:
            for fire in self.fire_list:
                fire.draw()
        # if self.space_pressed:
        #     self.fire = Fire(self.dragon.center_x, self.dragon.center_y)
        #     self.fire.draw()

    def setup(self):
        for i in range(200):
            self.ground = Ground()
            self.ground.center_x = constants.TERRAIN_RADIUS * (i * 2)
            self.ground_list.append(self.ground)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.SPACE:
            self.space_pressed = True

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
        elif key == arcade.key.SPACE:
            self.space_pressed = False

    def on_update(self, delta_time):
        self.dragon.center_x += self.dragon.change_x
        self.dragon.center_y += self.dragon.change_y
        if len(self.fire_list) > 0:
            for i in range(len(self.fire_list)):
                self.fire_list[i].center_x += self.fire.change_x
                self.fire_list[i].center_y += self.fire.change_y
                self.fire_list[i].change_y = -constants.FIRE_SPEED
                self.fire_list[i].change_x = constants.FIRE_SPEED
        self.dragon.change_x = 0
        self.dragon.change_y = 0
        # If continuous movement is desired, erase 2 previous lines
        for fire in self.fire_list:
            for ground in self.ground_list:
                if fire.collides_with_sprite(ground):
                    self.fire_list.remove(fire)
                    break
        for ground in self.ground_list:
            if self.dragon.collides_with_sprite(ground):
                self.dragon.center_y = (2 * constants.TERRAIN_HEIGHT) + constants.DRAGON_HEIGHT

        if self.up_pressed and not self.down_pressed:
            self.dragon.change_y = constants.PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.dragon.change_y = -constants.PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.dragon.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.dragon.change_x = constants.PLAYER_MOVEMENT_SPEED
        if self.space_pressed:
            self.fire = Fire(self.dragon.center_x, self.dragon.center_y)
            self.fire_list.append(self.fire)
