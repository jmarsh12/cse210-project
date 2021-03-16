import os
import arcade

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Sprite with Moving Platforms Example"

GROUND_IMAGE = "images/terrain.png"
DRAGON_IMAGE = "images/dragon.png"
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

PLAYER_MOVEMENT_SPEED = 8
FIRE_SPEED = 5

