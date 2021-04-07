#from game import Game
from start_screen import MenuView
import arcade
import constants

window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, "Dragon Attack")
menu_view = MenuView()
window.show_view(menu_view)
arcade.run()
