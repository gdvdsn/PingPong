import pygame as pg, sys
from pygame import *
from cmaze import *
from pygame.locals import *
from cplayer import *
from cbot import *

#initiate
pg.init()

def main():
    map = maze()

    #Create screen
    ds = pg.display.set_mode((1400, 800))
    pg.display.set_caption("Map")

    #background
    r_back = pg.Rect(0, 0, 700, 800)
    b_back = pg.Rect(701, 0, 700, 800)

    #colors
    peach_background = (200, 175, 150)
    b_red = (255, 180, 180)
    b_blu = (180, 180, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blu = (0, 0, 255)
    grn = (65, 215, 55)
    gray = (200, 200, 200)

    #player rects
    p1 = player(30, 195)
    p2 = player(730, 195)

    #bot rects
    bot_list = []
    #bot = bot()

    clock = pg.time.Clock()

    while True:
        #draws map
        map.drawall(ds, black, b_red, b_blu, r_back, b_back)

        #draws players
        p1.drawp(ds, red)
        p2.drawp(ds, blu)

        #checks players movements
        p1.checkmove1()
        p2.checkmove2()

        if map.checkwall(p1.getrects()[0], p1.getrects()[1], p1.getrects()[2]):
            p1.atwall()

        if map.checkwall(p2.getrects()[0], p2.getrects()[1], p2.getrects()[2]):
            p2.atwall()



        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN:
                p1.turn1(event.key)
                p2.turn2(event.key)

        pg.display.update()
        clock.tick()

main()
