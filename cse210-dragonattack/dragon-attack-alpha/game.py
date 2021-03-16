import arcade
import constants
from ground import Ground
from dragon import Dragon


class Game(arcade.Window):

    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, "Dragon Attack")
        arcade.set_background_color(arcade.color.ALICE_BLUE)

        self.dragon = Dragon()
        self.ground = None
        self.ground_list = []
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.change_x = 0
        self.change_y = 0

    def on_draw(self):
        arcade.start_render()

        for i in self.ground_list:
            i.draw()
            # print(len(self.ground_list))
        self.dragon.draw()

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

    def on_update(self, delta_time):
        self.dragon.center_x += self.dragon.change_x
        self.dragon.center_y += self.dragon.change_y
        self.dragon.change_x = 0
        self.dragon.change_y = 0
        # If continuous movement is desired, erase lines 66 and 67.

        if self.up_pressed and not self.down_pressed:
            self.dragon.change_y = constants.PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.dragon.change_y = -constants.PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.dragon.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.dragon.change_x = constants.PLAYER_MOVEMENT_SPEED
