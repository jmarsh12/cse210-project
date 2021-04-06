import arcade
import random
import os
import constants
from game import Game

WIDTH = constants.SCREEN_WIDTH
HEIGHT = constants.SCREEN_HEIGHT
SPRITE_SCALING = constants.SPRITE_SCALING

class MenuView(arcade.View):
    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("DRAGON ATTACK", WIDTH/2, HEIGHT/2,
                         arcade.color.RED, font_size=60, anchor_x="center")

        arcade.draw_text("Press space to play", WIDTH/2, HEIGHT/2 - 150,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ Handle keypresses. In this case, we'll just count a 'space' as
        game over and advance to the game over view. """
        if key == arcade.key.SPACE:
            #game_over_view = GameOverView()
            game = Game()
            self.window.show_view(game)
            game.setup()