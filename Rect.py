import pygame
pg.init()
import pygame as pg
from math import pi
from dataclasses import dataclass
#
#clock = pg.time.Clock()
#
#FPS = 60
#BACKGROUND_COLOR = (70, 86, 94)
#
#pg.display.set_caption("PyGame")
#
#width = 450
#height = 200
#window_size = (width, height)
#screen = pg.display.set_mode((window_size))
#
#player_image = pg.image.load('Player.png').convert_alpha()
#player = pg.transform.scale
#(player_image, (50, 75))
#
#moving_right = False
#moving_left = False
#
#@dataclass
#class PlayerLocation:
#    x:int
#    y:int
#player_Location = PlayerLocation(x=155, y=125)
#velocity = 3,5
#
#running = True
#
#while running:
#    screen.fill((0,0,0))
#    screen.blit(player, (player_Location.x, player_Location.y))
#    
#    if moving_right:
#        player_Location.x += velocity
#    if moving_left:
#        player_Location -= velocity
#
#    for event in pg.event.get():
#        if event.type == pg.QUIT:
#            running = False
#
#        if event.type == pg.KEYDOWN:
#            if event.key == pg.K_RIGHT:
#                moving_right = True
#            if event.key == pg.K_LEFT:
#                moving_left = True
#        if event.type == pg.KEYUP:
#                if event.key == pg.K_RIGHT:
#                    moving_right = False
#                if event.key == pg.K_LEFT:
#                    moving_left = False
#                
#    if player_Location.x < 0:
#        player_Location.x = 0
#    if player_Location.x + player.get_width() > width:
#        player_Location.x = width - player.get_width()
#
    #pg.display.update()
    #lock.tick(FPS)
#    
#pg.quit()

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
#
#screen = pygame.display.set_mode((625, 450))
#screen.fill((255, 255, 255)) # Fundo Branco
#
#while True:
#    
#    # Desenha retângulos sólidos sobrepostos
#    pygame.draw.rect(screen, (255, 0, 0), (50, 20, 120, 100))
#    pygame.draw.rect(screen, (0, 255, 0), (100, 60, 120, 100))
#    pygame.draw.rect(screen, (0, 0, 255), (150, 100, 120, 100))
#
#    # Desenha retângulos contornados com larguras diferentes
#    pygame.draw.rect(screen, (255, 0, 0), (350, 20, 120, 100), 1)
#    pygame.draw.rect(screen, (0, 255, 0), (400, 60, 120, 100), 4)
#    pygame.draw.rect(screen, (0, 0, 255), (450, 100, 120, 100), 8)
#
#    pygame.display.flip()
#
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            exit()
#
#retangulos = [
#    pg.Rect(20, 20, 100, 50),
#    pg.Rect(20, 90, 50, 50),
#    pg.Rect(500, 30, 80, 60)
#]
#
#while True:
#    screen.fill(BLACK)
#    for event in pg.event.get():
#        if event.type == pg.QUIT:
#            exit()
#    
#    for retangulo in retangulos:
#        pg.draw.rect(screen, (0, 0, 255), retangulo)
#
#    pg.draw.rect(screen, GREEN, [115, 280, 70, 40])
#    pg.draw.rect(screen, RED, [115,280, 71, 41], 2)
#    pg.draw.circle(screen, YELLOW, [325, 70], 30)
#    pg.draw.circle(screen, BLUE, [250, 250], 25, True)
#    pg.draw.ellipse(screen, BLACK, [250, 300, 100, 100])
#    pg.draw.arc(screen, RED, [430, 150, 150, 125], pi/100, 1.13*pi, 2)
#    pg.draw.line(screen, BLUE, (0, height-100), (width, height-100), 5)
#    pg.draw.aaline(screen, GREEN, (0, height-200), (width, height-200))
#    pg.draw.lines(screen, WHITE, False, [[400, 400], [400, 20], [200, 20]], 2)
#    pg.draw.polygon(screen, YELLOW, [[140, 120], [100, 200], [300, 200]])
#    pg.draw.polygon(screen, GREEN, [[140, 120], [100, 200], [300, 200]], 3)
#
#    pygame.display.update()
#
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            exit()