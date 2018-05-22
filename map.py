import pygame as pg, sys
from pygame import *
from pygame.locals import *
from cplayer import *
from cbot import *
from cmaze import *

#initiate
pg.init()

def end_screen(ds, col1, col2):
    pg.draw.rect(ds, col1, (0, 0, 700, 700))
    pg.draw.rect(ds, col2, (700, 0, 700, 700))

    font = pg.font.SysFont("Black Ops", 100)
    t_surf = font.render(("PLAYMAKER"), True, (0, 0, 0))
    t_rect = t_surf.get_rect()
    t_rect.center = (700, 375)

def switch_creation(switch):
    switch, b = maze.switch_function(switch)

    return b, switch

def main():
    map = maze()

    #Create screen
    ds = pg.display.set_mode((1400, 800))
    pg.display.set_caption("Map")

    screen = "s"

    #background
    r_back = pg.Rect(0, 0, 700, 800)
    b_back = pg.Rect(701, 0, 700, 800)

    #colors
    b_red = (255, 180, 180)
    b_blu = (180, 180, 255)
    red = (255, 0, 0)
    blu = (0, 0, 255)

    #player rects
    p1 = player(30, 195)
    p2 = player(730, 195)

    #bot rects (and use)

    while True:
        if screen == "s":
            map.sscreen(ds, b_red, b_blu, r_back, b_back)

        elif screen == "c":
            map.cpscreen(ds, b_red, b_blu)

        elif screen == "g":
            #draw map
            map.drawall(ds, b_red, b_blu, r_back, b_back)

            #draw players
            p1.drawp(ds, red)
            p2.drawp(ds, blu)

            ##check players movements
            p1.checkmove1()
            p2.checkmove2()

            #check player/wall positions
            if map.checkwall(p1.getrects()[0], p1.getrects()[1], p1.getrects()[2]):
                p1.atwall()

            if map.checkwall(p2.getrects()[0], p2.getrects()[1], p2.getrects()[2]):
                p2.atwall()

            #check bot/player positions
            for b in map.get_bot_list():
                winner = b.checkred([p1.getrects(), p2.getrects()])
                if winner == False:
                    winner = b.checkblu([p1.getrects(), p2.getrects()])

                if isinstance(winner, str):
                    screen = "e"
                    break

            #bot function
            map.botspawn_function()

            #transparent walls
            map.switch_function(ds, p1.getrects()[0], p2.getrects()[0])

        elif screen == "e":
            map.escreen(ds, b_red, b_blu, r_back, b_back, winner)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if screen == "s":
                        if map.checkbuttons(screen, event.pos):
                            screen = "g"
                    elif screen == "e":
                        if map.checkbuttons(screen, event.pos):
                            pg.quit()
                            sys.exit()

            if event.type == KEYDOWN:
                p1.turn1(event.key)
                p2.turn2(event.key)

        pg.display.update()

main()
