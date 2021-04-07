import arcade


class GameOverView(arcade.View):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """

        arcade.draw_text("Game Over", self.x, self.y, arcade.color.WHITE, 54, anchor_x="center")
