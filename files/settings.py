# SETTINGS

from random import randint

# Window specs
TITLE = "Platform"
WIDTH = 800
HEIGHT = 600
FPS = 60

# Player attributes
PLAYER_ACC = 0.8
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.5
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
JUMP_HEIGHT = 15

# Set bottom platform 
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40)]

# Platform generation settings
NUMBER_OF_PLATFORMS = 6
PLATFORM_X_1 = 0
PLATFORM_X_2 = WIDTH
PLATFORM_Y_1 = 0
PLATFORM_Y_2 = HEIGHT - 140
PLATFORM_X_LENGTH = 100
PLATFORM_Y_LENGTH = 20
PLATFORMS_MOVING_FASTER = 10

# Setting up platforms
for i in range(NUMBER_OF_PLATFORMS):
	PLATFORM_LIST.append((randint(PLATFORM_X_1, PLATFORM_X_2), randint(PLATFORM_Y_1, PLATFORM_Y_2),
	 PLATFORM_X_LENGTH, PLATFORM_Y_LENGTH))

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)