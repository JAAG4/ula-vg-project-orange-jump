"""
This module was autogenerated by gale.
"""
import pathlib

import pygame

from gale import frames
from gale import input_handler
import logging
from sys import stdout

logging.basicConfig(level=logging.DEBUG, stream=stdout)

input_handler.InputHandler.set_keyboard_action(input_handler.KEY_ESCAPE, "quit")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RETURN, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_KP_ENTER, "enter")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_RIGHT, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_d, "move_right")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_LEFT, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_a, "move_left")
input_handler.InputHandler.set_keyboard_action(input_handler.KEY_SPACE, "jump")
input_handler.InputHandler.set_mouse_click_action(input_handler.MOUSE_BUTTON_1, "jump")

PYGAME_RAW_INPUT = {
    "move_right": (pygame.K_LEFT, pygame.K_d),
    "move_left": (pygame.K_LEFT, pygame.K_a),
}

# Size we want to emulate
VIRTUAL_WIDTH = 540
VIRTUAL_HEIGHT = 540

# Size of our actual window
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

BASE_DIR = pathlib.Path(__file__).parent

GRAVITY_PPX = 64
PLAYER_WALK_PPX = 100
TERMINAL_VEL = 300
PLAYER_FALL_X_CTRL_RATE = 0.8
PLAYER_JUMP_X_CTRL_RATE = 0.9
LEVELS_DEFAULT_CONFIG = {
    "ldtkworldpath": BASE_DIR / "assets" / "ldtk" / "World.ldtk",
    "level_n": 0,
}
MAX_WIDTH = 540
# Register your textures from the graphics folder, for instance:
# TEXTURES = {
#     'my_texture': pygame.image.load(BASE_DIR / "assets" / "graphics" / "my_texture.png")
# }
TEXTURES = {
    "orange": pygame.image.load(
        BASE_DIR / "assets" / "graphics" / "sprites" / "orange_spritesheet_32x34.png"
    ),
    "tiles": pygame.image.load(
        BASE_DIR / "assets" / "graphics" / "tilesheets" / "tiles_packed.png"
    ),
}

# Register your frames, for instance:
# FRAMES = {
#     'my_frames': frames.generate_frames(TEXTURES['my_texture'], 16, 16)
# }
FRAMES = {
    "orange": frames.generate_frames(TEXTURES["orange"], 32, 34),
    "tiles": frames.generate_frames(TEXTURES["tiles"], 18, 18),
}

pygame.mixer.init()

# Register your sound from the sounds folder, for instance:
# SOUNDS = {
#     'my_sound': pygame.mixer.Sound(BASE_DIR / "assets"  / "sounds" / "my_sound.wav"),
# }
SOUNDS = {
    # "music1": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "song.mp3"),
    "jump": pygame.mixer.Sound(BASE_DIR / "assets" / "sounds" / "jump.wav"),
}
DEFAULT_SONG = BASE_DIR / "assets" / "sounds" / "song.mp3"
pygame.font.init()

# Register your fonts from the fonts folder, for instance:
# FONTS = {
#     'small': pygame.font.Font(BASE_DIR / "assets"  / "fonts" / "font.ttf", 8)
# }
FONTS = {
    "small": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "grafxkid_at01.ttf", 8),
    "mid": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "grafxkid_at01.ttf", 16),
    "huge": pygame.font.Font(BASE_DIR / "assets" / "fonts" / "grafxkid_at01.ttf", 64),
}
