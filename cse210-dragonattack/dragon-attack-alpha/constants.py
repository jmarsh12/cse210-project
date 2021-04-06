import os
import arcade

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Sprite with Moving Platforms Example"

GROUND_IMAGE = "images/ground.png"
DRAGON_IMAGE = "images/dragon.png"
SHEEP_IMAGE = "images/sheep_right.png"
FIRE_IMAGE = "images/small_fireball.png"
BACKGROUND_IMAGE = arcade.load_texture("images/Background2long.jpg")
FIRE_MIRROR_IMAGE = "images/small_fireball_mirror.png"
FIRE_SOUND = arcade.load_sound(":resources:sounds/explosion2.wav")
FIRE_IMPACT_SOUND = arcade.load_sound(":resources:/sounds/hit1.wav")
GAME_SONG = arcade.load_sound("assets/Monkey_Drama.mp3")
GAME_SONG_2 = arcade.load_sound("assets/dragonborne.mp3")
LOSE_SOUND = arcade.load_sound(":resources:sounds/lose4.wav")
DAMAGE_SOUND = arcade.load_sound(":resources:sounds/hurt3.wav")
WIN_SOUND = arcade.load_sound(":resources:sounds/coin2.wav")

SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)
TERRAIN_RADIUS = 55
TERRAIN_HEIGHT = 56

FLAG_HEIGHT = 75
FLAG_RADIUS = 15
FLAG_IMAGE = "images/flagGreen2.png"

GEM_IMAGE = "images/gemBlue.png"
GEM_HEIGHT = 5
GEM_RADIUS = 5
GEM_SOUND = arcade.load_sound(":resources:sounds/coin4.wav")


DRAGON_RADIUS = (130 / 2)
DRAGON_HEIGHT = (54 / 2)
DRAGON_MAX_HEALTH = 1000
DRAGON_DIVE_SPEED = -30

HEALTH_BAR_LENGTH = DRAGON_MAX_HEALTH / 10
HEALTH_BAR_HEIGHT = 10

FLYING_RIGHT_0 = "images/flying_right_0.png"
FLYING_RIGHT_1 = "images/flying_right_0.png"
FLYING_RIGHT_2 = "images/flying_right_0.png"
FLYING_RIGHT_3 = "images/flying_right_1.png"
FLYING_RIGHT_4 = "images/flying_right_1.png"
FLYING_RIGHT_5 = "images/flying_right_1.png"
FLYING_RIGHT_6 = "images/flying_right_2.png"
FLYING_RIGHT_7 = "images/flying_right_2.png"
FLYING_RIGHT_8 = "images/flying_right_2.png"

FLYING_LEFT_0 = "images/flying_left_0.png"
FLYING_LEFT_1 = "images/flying_left_0.png"
FLYING_LEFT_2 = "images/flying_left_0.png"
FLYING_LEFT_3 = "images/flying_left_1.png"
FLYING_LEFT_4 = "images/flying_left_1.png"
FLYING_LEFT_5 = "images/flying_left_1.png"
FLYING_LEFT_6 = "images/flying_left_2.png"
FLYING_LEFT_7 = "images/flying_left_2.png"
FLYING_LEFT_8 = "images/flying_left_2.png"

FIRE_RADIUS = 25
FIRE_REGEN_SPEED = 17
MAX_FIRE = 102

SHEEP_RADIUS = 65
SHEEP_HEIGHT = 27
SHEEP_SPEED = .5
SHEEP_HEALTH_BONUS = 200

PLAYER_MOVEMENT_SPEED = 75
FIRE_SPEED = 25

RIGHT_VIEWPOINT_MARGIN = 950
LEFT_VIEWPOINT_MARGIN = 950
TOP_VIEWPOINT_MARGIN = 500
BOTTOM_VIEWPOINT_MARGIN = 300

GRAVITY = 15
PLAYER_JUMP_SPEED = 20

VILLAGE_IMAGE = "images/village3.png"

MISSILE_IMAGE = "images/rock.png"
MISSILE_DAMAGE = 100
