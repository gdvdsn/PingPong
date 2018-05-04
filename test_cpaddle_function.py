from cpaddle import *
import pygame as pg, sys
from pygame.locals import *

pg.init()

rpi, bpi = paddle.images(0)

display_surf = pg.display.set_mode((1400, 800))
pg.display.set_caption("Pong")

bp = paddle(200, 300, 40, 20)

peach_background = (200, 175, 150)

while True:
    display_surf.fill(peach_background)
    bp.update_display(display_surf, bpi, 2)
    for event in pg.event.get():
        if event.type == KEYDOWN:
            bp.update_rect(event, 'b')
        if event.type == QUIT:
            pg.quit()
            sys.exit()

pg.display.update()
