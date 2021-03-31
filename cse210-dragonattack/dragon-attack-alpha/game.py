import arcade
import constants
import random
from ground import Ground
from dragon import Dragon
from fire import Fire
from health_bar import HealthBar
from village import Village
from sheep import Sheep
import time
from flag import Flag
from gem import Gem


class Game(arcade.Window):

    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, "Dragon Attack")
        arcade.set_background_color(arcade.color.ALICE_BLUE)

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

        self.missile_list = arcade.SpriteList()
        self.village_list = arcade.SpriteList()
        self.physics_engine_missile = None

        self.win = False
        self.game_over = False

    def on_draw(self):
        arcade.start_render()

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

        self.missile_list.draw()

        if len(self.sheep.sheep_list) < 5:

            self.sheep.center_x = random.randint(200, 1000)
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

        arcade.play_sound(constants.GAME_SONG_2)

        for i in range(0, 30, 1):
            self.ground = Ground()
            self.ground.center_x = constants.TERRAIN_RADIUS * (i * 2)
            self.ground_list.append(self.ground)

        for i in range(40, 100, 1):
            self.ground = Ground()
            self.ground.center_x = constants.TERRAIN_RADIUS * (i * 2)
            self.ground_list.append(self.ground)

        for i in range(125, 250, 1):
            self.ground = Ground()
            self.ground.center_x = constants.TERRAIN_RADIUS * (i * 2)
            self.ground_list.append(self.ground)

            # for i in range(10, 15, 6):
            #     self.gem = Gem()
            #     self.gem.center_x = i * 17
            #     self.gem.center_y = 150
            #     self.gem_list.append(self.gem)

            # self.level_builder.build_level_1()

        for i in range(60, 75, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 600
            self.ground_list.append(self.ground)
            for gem in range(69, 70, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 650
                self.gem_list.append(self.gem)

        for i in range(100, 125, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 350
            self.ground_list.append(self.ground)

        for i in range(130, 140, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 700
            self.ground_list.append(self.ground)

        for i in range(85, 100, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 815
            self.ground_list.append(self.ground)

        for i in range(95, 120, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1050
            self.ground_list.append(self.ground)
            for gem in range(96, 97, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 1100
                self.gem_list.append(self.gem)

        for i in range(150, 160, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 950
            self.ground_list.append(self.ground)
            for gem in range(151, 152, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 1000
                self.gem_list.append(self.gem)

        for i in range(200, 220, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)

        for i in range(230, 240, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 550
            self.ground_list.append(self.ground)
            for gem in range(239, 240, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 600
                self.gem_list.append(self.gem)

        for i in range(220, 235, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 0
            self.ground_list.append(self.ground)
            for gem in range(231, 232, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 50
                self.gem_list.append(self.gem)

        for i in range(245, 260, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 250
            self.ground_list.append(self.ground)

        for i in range(300, 320, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)
            for gem in range(313, 314, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 450
                self.gem_list.append(self.gem)

        for i in range(345, 355, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 600
            self.ground_list.append(self.ground)

        for i in range(390, 400, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 800
            self.ground_list.append(self.ground)
            for gem in range(394, 395, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 850
                self.gem_list.append(self.gem)

        for i in range(415, 425, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 650
            self.ground_list.append(self.ground)
            for gem in range(420, 421, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 700
                self.gem_list.append(self.gem)

        for i in range(400, 410, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)
            for gem in range(409, 410, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 450
                self.gem_list.append(self.gem)

        for i in range(450, 475, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 330
            self.ground_list.append(self.ground)
            for gem in range(471, 472, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 380
                self.gem_list.append(self.gem)

        for i in range(650, 660, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)

        for i in range(675, 680, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)
            for gem in range(679, 680, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 450
                self.gem_list.append(self.gem)

        for i in range(695, 700, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)

        for i in range(685, 695, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 650
            self.ground_list.append(self.ground)
            for gem in range(694, 695, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 700
                self.gem_list.append(self.gem)

        for i in range(715, 720, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)

        for i in range(735, 740, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)
            for gem in range(739, 740, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 450
                self.gem_list.append(self.gem)

        for i in range(755, 760, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)

        for i in range(775, 780, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)

        for i in range(795, 800, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 400
            self.ground_list.append(self.ground)

        for i in range(875, 900, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 350
            self.ground_list.append(self.ground)

        for i in range(915, 930, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 500
            self.ground_list.append(self.ground)
            for gem in range(924, 925, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 550
                self.gem_list.append(self.gem)

        for i in range(940, 960, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 700
            self.ground_list.append(self.ground)

        for i in range(920, 935, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 900
            self.ground_list.append(self.ground)

        for i in range(950, 960, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1100
            self.ground_list.append(self.ground)

        for i in range(980, 985, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1250
            self.ground_list.append(self.ground)
            for gem in range(981, 982, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 1300
                self.gem_list.append(self.gem)

        for i in range(1000, 1005, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1350
            self.ground_list.append(self.ground)

        for i in range(1020, 1025, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1450
            self.ground_list.append(self.ground)

        for i in range(1040, 1045, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1550
            self.ground_list.append(self.ground)
            for gem in range(1041, 1042, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 1600
                self.gem_list.append(self.gem)

        for i in range(1060, 1065, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1700
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 150
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 250
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 350
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 450
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 550
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 650
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 750
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 850
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 950
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1050
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1150
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1250
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1350
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1450
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1550
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1650
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1750
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1850
            self.ground_list.append(self.ground)

        for i in range(1090, 1095, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 1950
            self.ground_list.append(self.ground)
            for gem in range(1091, 1092, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 2000
                self.gem_list.append(self.gem)

        for i in range(1125, 1130, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 850
            self.ground_list.append(self.ground)

        for i in range(1150, 1175, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 850
            self.ground_list.append(self.ground)
            for gem in range(1164, 1165, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 900
                self.gem_list.append(self.gem)

        for i in range(1350, 1360, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 450
            self.ground_list.append(self.ground)

        for i in range(1375, 1390, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 650
            self.ground_list.append(self.ground)

        for i in range(1410, 1425, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 750
            self.ground_list.append(self.ground)
            for gem in range(1416, 1417, 6):
                self.gem = Gem()
                self.gem.center_x = gem * 17
                self.gem.center_y = 800
                self.gem_list.append(self.gem)

        for i in range(1445, 1460, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 750
            self.ground_list.append(self.ground)

        for i in range(1480, 1495, 6):
            self.ground = Ground()
            self.ground.center_x = i * 17
            self.ground.center_y = 750
            self.ground_list.append(self.ground)
            #         TODO: add platforms to their own class

        for i in range(1610, 1615, 6):
            self.flag = Flag()
            self.flag.center_x = i * 17
            self.flag.center_y = 200
            self.ground_list.append(self.flag)

        # Create the 'physics engine'

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.dragon, self.ground_list, constants.GRAVITY)

        self.village1 = Village(self.missile_list)
        self.village1.center_x = 400
        self.village1.center_y = 152
        self.village_list.append(self.village1)
        arcade.schedule(self.village1.add_missile, 1)

        self.village2 = Village(self.missile_list)
        self.village2.center_x = 2500
        self.village2.center_y = 152
        self.village_list.append(self.village2)
        arcade.schedule(self.village2.add_missile, 1)

        # self.physics_engine = \
        #     arcade.PhysicsEnginePlatformer(self.dragon,
        #                                     self.village_list,
        #                                    constants.GRAVITY)

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
        self.dragon.regenerate_fire()
        self.health.update(self.dragon.get_center_x(), self.dragon.get_center_y(), self.dragon.health)
        self.dragon.move_fire()
        self.dragon.change_x = 0
        self.dragon.change_y = 0
        # TODO: If continuous movement is desired, erase 2 previous lines; makes for harder game
        for sheep in self.sheep.sheep_list:
            print(len(self.sheep.sheep_list))
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

        for ground in self.ground_list:
            if self.dragon.collides_with_sprite(ground):
                self.dragon.center_y = (2 * constants.TERRAIN_HEIGHT) + constants.DRAGON_HEIGHT
        # TODO: resolve collisions with platforms bug

        if self.up_pressed and not self.down_pressed:
            self.dragon.move_up()
            # self.health.move_up()
        elif self.down_pressed and not self.up_pressed:
            self.dragon.move_down()
            # self.health.move_down()
        if self.left_pressed and not self.right_pressed:
            self.dragon.move_left()
        # self.health.move_left()
        elif self.right_pressed and not self.left_pressed:
            self.dragon.move_right()
            # self.health.move_right()
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
                # self.game_over = True
                arcade.play_sound(constants.DAMAGE_SOUND)
                self.dragon.lose_health()
                i.remove_from_sprite_lists()
                if self.dragon.health == 0:
                    self.game_over = True
                    self.dragon.reset_health()
            elif i.collides_with_list(self.ground_list):
                i.remove_from_sprite_lists()
            if i.left < 0 or i.top > 1200:
                i.remove_from_sprite_lists()

        if self.dragon.collides_with_sprite(self.flag):
            self.win = True

        if self.win:
            arcade.play_sound(constants.WIN_SOUND)
            time.sleep(0.6)
            arcade.close_window()

        if self.game_over:
            # arcade.close_window()
            self.dragon.center_x = 50
            self.game_over = False
            # if we want to just start the level over, use the above code

        if self.dragon.center_y < -400:
            arcade.play_sound(constants.LOSE_SOUND)
            time.sleep(0.6)
            arcade.close_window()
            # self.dragon.center_x = 50
            # self.dragon.center_y = 150

            # self.game_over = False
            # if we want to just start the level over, use the above code

        for gem in self.gem_list:
            if self.dragon.collides_with_sprite(gem):
                arcade.play_sound(constants.GEM_SOUND)
                gem.remove_from_sprite_lists()
