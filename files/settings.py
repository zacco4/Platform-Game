from random import randint

TITLE = "Platform"
WIDTH = 800
HEIGHT = 600
FPS = 60

PLAYER_ACC = 0.8
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.4
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
JUMP_HEIGHT = 15

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40)]

for i in range(3):
	PLATFORM_LIST.append((randint(0, WIDTH), randint(0, HEIGHT - 41), randint(40, 100), randint(40, 60)))




WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)