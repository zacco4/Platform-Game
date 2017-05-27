# Platform game

import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialise game windows, etc
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
        # self.player2 = Player(self)
        self.all_sprites.add(self.player)
        # self.all_sprites.add(self.player2)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        # game loop - update
        self.all_sprites.update()
        # check if player hits platform - only if falling
        if self.player.vel.y  > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
                """
        if self.player2.vel.y  > 0:
            hits = pg.sprite.spritecollide(self.player2, self.platforms, False)
            if hits:
                self.player2.pos.y = hits[0].rect.top + 1
                self.player2.vel.y = 0
                """

    def events(self):
        # game loop - events
        for event in pg.event.get():
            # check if close window is pressed
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == JUMP_BUT or event.key == JUMP_BUT2:
                    self.player.jump()
                    """
            if event.type == pg.KEYDOWN:
                if event.key == JUMP_BUT2:
                    self.player2.jump()
                    """

    def draw(self):
        # game loop - draw
        self.image = pg.image.load(os.path.join(img_folder, "bg5.jpg")).convert()
        self.screen.blit(self.image, [-400, 0])
        self.all_sprites.draw(self.screen)
        # always flip after drawing everything
        pg.display.flip()

    def show_start_screen(self):
        # start screen
        pass

    def show_go_screen(self):
        # game over / continue
        pass



g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
