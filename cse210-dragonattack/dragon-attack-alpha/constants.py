import os
import arcade

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Sprite with Moving Platforms Example"

GROUND_IMAGE = "images/terrain.png"
DRAGON_IMAGE = "images/dragon.png"
SHEEP_IMAGE = "images/sheep.png"
FIRE_IMAGE = "images/fire.png"
FIRE_SOUND = arcade.load_sound(":resources:sounds/explosion2.wav")
FIRE_IMPACT_SOUND = arcade.load_sound(":resources:/sounds/hit1.wav")

SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)
TERRAIN_RADIUS = 55
TERRAIN_HEIGHT = 56

DRAGON_RADIUS = (130 / 2)
DRAGON_HEIGHT = (54 / 2)
FIRE_RADIUS = 25
FIRE_REGEN_SPEED = 17
MAX_FIRE = 102

SHEEP_RADIUS = 65
SHEEP_HEIGHT = 27
SHEEP_SPEED = .5

PLAYER_MOVEMENT_SPEED = 50
FIRE_SPEED = 25

RIGHT_VIEWPOINT_MARGIN = 950
LEFT_VIEWPOINT_MARGIN = 950
TOP_VIEWPOINT_MARGIN = 500
BOTTOM_VIEWPOINT_MARGIN = 300

GRAVITY = 15
PLAYER_JUMP_SPEED = 20
