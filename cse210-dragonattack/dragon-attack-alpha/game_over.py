import arcade
import random
import os
import constants
class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", 600, 600, arcade.color.WHITE, font_size=54, anchor_x="center")
        # arcade.draw_text("Press space to play", WIDTH/2, HEIGHT/2 - 150,
        #                  arcade.color.WHITE, font_size=30, anchor_x="center")