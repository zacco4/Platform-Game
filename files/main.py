# MAIN

DELETE THIS CODE TO RUN

import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # Initialize the game window etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        # Update Game Loop
        self.all_sprites.update()

        # COLLISION DETECTION

        # If player is falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                # If standing on top of the platforms, don't go through
                if self.player.rect.right > hits[0].rect.left and self.player.rect.left < hits[0].rect.right and self.player.pos.x + PLAYER_WIDTH / 2 - 8 > hits[0].rect.left and self.player.pos.x - PLAYER_WIDTH / 2 + 2 < hits[0].rect.right:
                    self.player.pos.y = hits[0].rect.top + 1
                    self.player.vel.y = 0

                # If player is coming from a side, keep it there
                else:
                    if self.player.vel.x > 0 and self.player.pos.x + PLAYER_WIDTH / 2 - 5 <= hits[0].rect.left:
                        self.player.pos.x = hits[0].rect.left - PLAYER_WIDTH / 2
                        self.player.vel.x = 0
                    elif self.player.vel.x < 0 and self.player.pos.x - PLAYER_WIDTH / 2 + 5 >= hits[0].rect.right:
                        self.player.pos.x = hits[0].rect.right + PLAYER_WIDTH / 2
                        self.player.vel.x = 0

        # If player is jumping
        elif self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if self.player.pos.x + PLAYER_WIDTH / 2 - 6 > hits[0].rect.left and self.player.pos.x - PLAYER_WIDTH / 2 + 6 < hits[0].rect.right:
                # If player hits bottom of platform, go down
                    self.player.pos.y = hits[0].rect.bottom + PLAYER_HEIGHT
                    self.player.vel.y = 0

                else:
                    if self.player.vel.x > 0:
                        self.player.pos.x = hits[0].rect.left - PLAYER_WIDTH / 2
                        self.player.vel.x = 0
                    elif self.player.vel.x < 0:
                        self.player.pos.x = hits[0].rect.right + PLAYER_WIDTH / 2 
                        self.player.vel.x = 0

        # If player reaches 4 fiths across the screen
        if self.player.rect.left >= WIDTH / 5 * 4:
            # Move the player to the left
            self.player.pos.x -= abs(self.player.vel.x)
            # Move all platforms to the left
            for plat in self.platforms:
                if plat.rect.top != 560:
                    plat.rect.x -= abs(self.player.vel.x * PLATFORMS_MOVING_FASTER)
                    if plat.rect.x + plat.rect.width < 0:
                        # Despawn the platforms not in sight
                        plat.kill()                      
                        # Create new platforms
                        platformAdd = Platform(randint(WIDTH, WIDTH * 2), randint(PLATFORM_Y_1, PLATFORM_Y_2), PLATFORM_X_LENGTH, PLATFORM_Y_LENGTH)
                        self.all_sprites.add(platformAdd)
                        self.platforms.add(platformAdd)

                

    def events(self):
        # Game loop events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # Draw game
        self.screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        # show start screen
        pass

    def show_go_screen(self):
        # show game over screen
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()