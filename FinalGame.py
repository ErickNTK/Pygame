import pygame
import pygame as pg

pg.init()

WIDTH = 800
HEIGHT = 600
WINDOW_SIZE = (WIDTH,HEIGHT)
screen = pg.display.set_mode((WINDOW_SIZE))

pg.display.set_caption("Game")

FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

while True:
    for event in pg.event.get():
     if event.type == pg.QUIT:
        exit()
    screen.fill(WHITE)
    pg.draw.circle(screen, BLUE, (400, 300), 75)
    pg.display.flip()