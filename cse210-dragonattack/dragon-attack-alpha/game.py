import arcade

import constants
import random
from dragon import Dragon
from health_bar import HealthBar
from village import Village
from sheep import Sheep
import time
from flag import Flag
from gem import Gem
from game_over import GameOverView
from level_builder import LevelBuilder
from missile import Missile


class Game(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.ALICE_BLUE)

        self.level_1 = LevelBuilder()
        self.flag = Flag()
        self.gem = Gem()
        self.gem_list = arcade.SpriteList()
        self.fire_impact_sound = constants.FIRE_IMPACT_SOUND
        self.fire_sound = constants.FIRE_SOUND
        self.dragon = Dragon()
        self.health = HealthBar()
        self.fire = None
        self.sheep = Sheep()
        self.ground = None
        self.ground_list = arcade.SpriteList()
        self.impenetrable_list = arcade.SpriteList()
        self.fire_list = []
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.space_pressed = False
        self.change_x = 0
        self.change_y = 0
        self.view_bottom = 0
        self.view_left = 0
        self.physics_engine = None
        self.song = constants.GAME_SONG_2
        self.missile = None

        self.missile_list = []
        self.village_list = arcade.SpriteList()
        self.physics_engine_missile = None

        self.win = False
        self.game_over = False

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(-1500, -500, 32000, 5000, constants.BACKGROUND_IMAGE)

        arcade.draw_text("Burn the flag to win!", 27300, 400, color=(255, 191, 0))

        for flag in self.level_1.flag_list:
            flag.draw()

        for i in self.ground_list:
            i.draw()

        for gem in self.gem_list:
            gem.draw()

        self.health.draw_health_bar()
        self.dragon.draw()

        if len(self.dragon.fire_list) > 0:
            for fire in self.dragon.fire_list:
                fire.draw()
        if self.space_pressed:
            self.dragon.shoot_fire()

        for i in self.village_list:
            i.draw()

        for missile in self.missile_list:
            missile.draw()

        if len(self.sheep.sheep_list) < 5:
            self.sheep.center_x = random.randint(200, 5000)
            self.sheep.sheep_list.append(self.sheep)

        for i in self.sheep.sheep_list:
            if self.sheep.alive:
                self.sheep.draw()
                self.sheep.move_sheep()
        for fire in self.dragon.fire_list:
            for sheep in self.sheep.sheep_list:
                if fire.collides_with_sprite(sheep):
                    arcade.play_sound(constants.FIRE_IMPACT_SOUND)
                    self.dragon.fire_list.remove(fire)
                    self.sheep.sheep_list.remove(sheep)
                    break
            self.alive = False

    def setup(self):
        self.level_1.build_level_1()
        self.ground_list = self.level_1.get_platforms()
        self.village_list = self.level_1.get_villages()
        self.missile_list = self.level_1.get_missiles()
        self.impenetrable_list = self.level_1.get_impenetrable_list()
        self.gem_list = self.level_1.get_gems()
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.dragon, self.impenetrable_list, constants.GRAVITY)

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
        if time.time() % 1.5 < 0.15:
            for village in self.village_list:
                self.missile = Missile(village.center_x + (random.randint(-50, 100)), village.center_y)
                self.missile_list.append(self.missile)

        self.dragon.regenerate_fire()
        self.health.update(self.dragon.get_center_x(), self.dragon.get_center_y(), self.dragon.health)
        self.dragon.move_fire()

        self.dragon.change_x = 0
        self.dragon.change_y = 0

        for sheep in self.sheep.sheep_list:
            if self.dragon.collides_with_sprite(sheep):
                self.dragon.gain_sheep_health_bonus()
                self.sheep.sheep_list.remove(sheep)
                break

        if len(self.dragon.fire_list) > 0:
            for fire in self.dragon.fire_list:
                for ground in self.ground_list:
                    if fire.collides_with_sprite(ground):
                        arcade.play_sound(constants.FIRE_IMPACT_SOUND)
                        self.dragon.fire_list.remove(fire)
                        break
                    elif fire.center_y < -100:
                        self.dragon.fire_list.remove(fire)
                        break

        for i in self.missile_list:
            self.physics_engine_missile = \
                arcade.PhysicsEnginePlatformer(i, self.village_list, gravity_constant=0.2)
            self.physics_engine_missile.update()

        for i in self.missile_list:
            if self.dragon.collides_with_sprite(i):
                arcade.play_sound(constants.DAMAGE_SOUND)
                self.dragon.lose_health()
                self.missile_list.remove(i)
                if self.dragon.health == 0:
                    self.game_over = True
                    self.dragon.reset_health()
            elif i.collides_with_list(self.ground_list):
                self.missile_list.remove(i)
            if i.left < 0 or i.top > 3000:
                self.missile_list.remove(i)

        for fire in self.dragon.fire_list:
            for missile in self.missile_list:
                if fire.collides_with_sprite(missile):
                    arcade.play_sound(constants.FIRE_IMPACT_SOUND)
                    self.missile_list.remove(missile)

        for fire in self.dragon.fire_list:
            for village in self.village_list:
                self.village = Village()
                if fire.collides_with_sprite(village):
                    arcade.play_sound(constants.FIRE_IMPACT_SOUND)
                    self.village_list.remove(village)
                    self.impenetrable_list.remove(village)
                    break

        for fire in self.dragon.fire_list:
            if fire.collides_with_sprite(self.flag):
                self.win = True

        if self.up_pressed and not self.down_pressed:
            self.dragon.move_up()
        elif self.down_pressed and not self.up_pressed:
            self.dragon.move_down()
        if self.left_pressed and not self.right_pressed:
            self.dragon.move_left()
        elif self.right_pressed and not self.left_pressed:
            self.dragon.move_right()
        if self.space_pressed:
            self.dragon.shoot_fire()
        self.physics_engine.update()

        change = False
        left_boundary = self.view_left + constants.LEFT_VIEWPOINT_MARGIN
        if self.dragon.left < left_boundary:
            self.view_left -= left_boundary - self.dragon.left
            change = True

        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_VIEWPOINT_MARGIN
        if self.dragon.right > right_boundary:
            self.view_left += self.dragon.right - right_boundary
            change = True

        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.TOP_VIEWPOINT_MARGIN
        if self.dragon.top > top_boundary:
            self.view_bottom += self.dragon.top - top_boundary
            change = True

        bottom_boundary = self.view_bottom + constants.BOTTOM_VIEWPOINT_MARGIN
        if self.dragon.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.dragon.bottom
            change = True

        if change:
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)
            arcade.set_viewport(self.view_left, constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom, constants.SCREEN_HEIGHT + self.view_bottom)

        for i in self.missile_list:
            if self.dragon.collides_with_sprite(i):
                arcade.play_sound(constants.DAMAGE_SOUND)
                self.dragon.lose_health()
                self.missile_list.remove(i)
                if self.dragon.health == 0:
                    self.game_over = True
                    self.dragon.reset_health()
            elif i.collides_with_list(self.ground_list):
                self.missile_list.remove(i)
            if i.left < 0 or i.top > 3000:
                self.missile_list.remove(i)

        for fire in self.dragon.fire_list:
            for flag in self.level_1.flag_list:
                if fire.collides_with_sprite(flag):
                    self.win = True

        if self.win:
            arcade.play_sound(constants.WIN_SOUND)
            time.sleep(0.6)
            arcade.close_window()

        if self.game_over:
            self.dragon.center_x = 50
            self.dragon.center_y = 150
            self.game_over = False

        if self.dragon.center_y < -400:
            arcade.play_sound(constants.LOSE_SOUND)
            time.sleep(0.6)
            self.game_over = True
            game_over_view = GameOverView(self.dragon.center_x, self.dragon.center_y)
            self.window.show_view(game_over_view)

        for gem in self.gem_list:
            if self.dragon.collides_with_sprite(gem):
                arcade.play_sound(constants.GEM_SOUND)
                gem.remove_from_sprite_lists()