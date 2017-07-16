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

        if self.player.rect.left >= WIDTH / 5 * 4:
            self.player.pos.x -= abs(self.player.vel.x)
            for plat in self.platforms:
                if plat.rect.top != 560:
                    plat.rect.x -= abs(self.player.vel.x)
                    if plat.rect.x + plat.rect.width < 0 :
                        plat.kill()                      
                        platformAdd = Platform(randint(WIDTH, WIDTH * 2), randint(0, HEIGHT - 140), randint(40, 100), randint(40, 60))
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