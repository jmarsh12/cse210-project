import arcade
import constants
from missile import Missile


class Village(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.VILLAGE_IMAGE)
        self.bottom = 80
        self.missile_list = []
        
    def add_missile(self, delta_time:float):
        missile = Missile(self.center_x, self.center_y)
        
        self.missile_list.append(missile)
        
        #missile.gravity