import pygame as pg

# game options/settings
TITLE = "Platform Game"
WIDTH = 480
HEIGHT = 600
FPS = 60

# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.10
PLAYER_GRAV = 0.8

# starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 200, 20),
                 (175, 100, 50, 20)]

# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# controls - pg.K_(KEY)
JUMP_BUT = pg.K_SPACE
JUMP_BUT2 = ""
LEFT = pg.K_a
LEFT2 = pg.K_LEFT
RIGHT = pg.K_d
RIGHT2 = pg.K_RIGHT
