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

        p1 = Platform(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2 = Platform(WIDTH / 2 - 60, HEIGHT * 3 / 4, 150, 30)
        self.all_sprites.add(p2)
        self.platforms.add(p2)

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

        # hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        # if hits and self.player.vel.y > 0:
        #     if self.player.pos.y - 41 == hits[0].rect.bottom:
        #         self.player.vel.y = 0
        #         self.player.pos.y = hits[0].rect.bottom + PLAYER_HEIGHT

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
        elif self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.bottom + PLAYER_HEIGHT
                self.player.vel.y = 0
                

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
        self.screen.fill(BLACK)
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
