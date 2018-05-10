import pygame as pg, sys
from pygame import *
import os
from cmaze import *
from pygame.locals import *

#initiate
pg.init()

#Create screen
ds = pg.display.set_mode((1400, 800))
pg.display.set_caption("Map")

#background
ss_red_half = pg.Rect(0, 0, 700, 800)
ss_blue_half = pg.Rect(701, 0, 700, 800)

#colors
peach_background = (200, 175, 150)
ss_red = (255, 180, 180)
ss_blue = (180, 180, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blu = (0, 0, 255)

#player rects
x1, y1 = 100, 100
dir1 = 0

rr1 = pg.Rect(x1, y1, 25, 25)
rr2 = pg.Rect(x1-5, y1+5, 35, 15)
rr3 = pg.Rect(x1+5, y1-5, 15, 35)

x2, y2 = 800, 100
dir2 = 0

br1 = pg.Rect(x2, y2, 25, 25)
br2 = pg.Rect(x2-5, y2+5, 35, 15)
br3 = pg.Rect(x2+5, y2-5, 15, 35)

#maze rects
wall1 = pg.Rect(75, 400, 300, 25)
maze_rects = []
maze_rects.append(wall1)

def turn1(event):
    if event == K_d:
        return 0
    if event == K_w:
        return 90
    if event == K_a:
        return 180
    if event == K_s:
        return 270

def turn2(event):
    if event == K_RIGHT:
        return 0
    if event == K_UP:
        return 90
    if event == K_LEFT:
        return 180
    if event == K_DOWN:
        return 270

def draw_players():
    pg.draw.rect(ds, red, rr1)
    pg.draw.rect(ds, red, rr2)
    pg.draw.rect(ds, red, rr3)

    pg.draw.rect(ds, blu, br1)
    pg.draw.rect(ds, blu, br2)
    pg.draw.rect(ds, blu, br3)

def at_wall(r1, r2, r3, dir):
    print("At wall")
    for wall in maze_rects:
        if r1.colliderect(wall) or r2.colliderect(wall) or r3.colliderect(wall):
            if dir == 0:
                return 'right'
            elif dir == 90:
                return 'top'
            elif dir == 180:
                return 'left'
            elif dir == 270:
                return 'bottom'

clock = pygame.time.Clock()

while True:
    pg.draw.rect(ds, ss_red, ss_red_half)
    pg.draw.rect(ds, ss_blue, ss_blue_half)

    pg.draw.rect(ds, black, wall1)

    rr1 = pg.Rect(x1, y1, 25, 25)
    rr2 = pg.Rect(x1-5, y1+5, 35, 15)
    rr3 = pg.Rect(x1+5, y1-5, 15, 35)

    br1 = pg.Rect(x2, y2, 25, 25)
    br2 = pg.Rect(x2-5, y2+5, 35, 15)
    br3 = pg.Rect(x2+5, y2-5, 15, 35)

    draw_players()

    if x1 + 30 < 700 and x1 - 5 > 0 and y1 + 30 < 800 and y1 - 5 > 0:
        if dir1 == 0:
            x1 += 5
        elif dir1 == 90:
            y1 -= 5
        elif dir1 == 180:
            x1 -= 5
        elif dir1 == 270:
            y1 += 5
    elif x1 + 30 >= 700 or at_wall(rr1, rr2, rr3, dir1) == 'right':
        x1 -= 1
        dir1 = 2
    elif x1 - 5 <= 0 or at_wall(rr1, rr2, rr3, dir1) == 'left':
        x1 += 1
        dir1 = 2
    elif y1 + 30 >= 800 or at_wall(rr1, rr2, rr3, dir1) == 'bottom':
        y1 -= 1
        dir1 = 2
    elif y1 - 5 <= 0 or at_wall(rr1, rr2, rr3, dir1) == 'top':
        y1 += 1
        dir1 = 2

    if x2 + 30 < 1400 and x2 - 5 > 700 and y2 + 30 < 800 and y2 - 5 > 0:
        if dir2 == 0:
            x2 += 5
        elif dir2 == 90:
            y2 -= 5
        elif dir2 == 180:
            x2 -= 5
        elif dir2 == 270:
            y2 += 5
    elif x2 + 30 >= 1400 or at_wall(br1, br2, br3, dir2) == 'right':
        x2 -= 1
        dir2 = 2
    elif x2 - 5 <= 700 or at_wall(br1, br2, br3, dir2) == 'left':
        x2 += 1
        dir2 = 2
    elif y2 + 30 >= 800 or at_wall(br1, br2, br3, dir2) == 'bottom':
        y2 -= 1
        dir2 = 2
    elif y2 - 5 <= 0 or at_wall(br1, br2, br3, dir2) == 'top':
        y2 += 1
        dir2 = 2

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        if event.type == KEYDOWN:
            print("Keydown")
            if event.key == K_w or event.key == K_a or event.key == K_s or event.key == K_d:
                dir1 = turn1(event.key)
            if event.key == K_UP or event.key == K_LEFT or event.key == K_DOWN or event.key == K_RIGHT:
                dir2 = turn2(event.key)

    pg.display.update()
    clock.tick()
