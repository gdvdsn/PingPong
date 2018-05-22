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

def bot_creation(time, spawn):
    place1 = [((27.5), (7.5)), ((627.5), (187.5)), ((602.5), (687.5)), ((152.5), (677.5))]
    place2 = [((27.5 + 700), (7.5)), ((627.5 + 700), (187.5)), ((602.5 + 700), (687.5)), ((152.5 + 700), (677.5))]

    if time > 650:
        bot_list.append(botplayer(place1[spawn][0], place1[spawn][1]))
        bot_list.append(botplayer(place2[spawn][0], place2[spawn][1]))

        return spawn + 1, 0

    return spawn, time

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
    global bot_list

    bot_list = []
    bot_list.append(botplayer(30, 7.5))
    bot_list.append(botplayer(30 + 700, 7.5))

    bot_spawn_timer = 0
    bot_spawn = 1

    while True:
        if screen == "s":
            screen = map.sscreen(ds, b_red, b_blu)

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

            ##bot functions
            for b in bot_list:
                #draw bot(s)
                b.drawb(ds)

                #check player/wall positions
                b.move(map.checkwall(b.getrects(), b.getrects(), b.getrects()))

                #check bot/player positions
                collision = b.checkplayer([p1.getrects(), p2.getrects()])

            #create new bots
            bot_spawn_timer += 1

            bot_spawn, bot_spawn_timer = bot_creation(bot_spawn_timer, bot_spawn)

            if bot_spawn > 3:
                bot_spawn = 0

            #transparent walls
            map.switch_function(ds, p1.getrects()[0], p2.getrects()[0])

            if collision:
                screen = "e"

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if screen == "s":
                            if map.checkbutton("s", event.pos):
                                screen = "g"

                if event.type == KEYDOWN:
                    p1.turn1(event.key)
                    p2.turn2(event.key)

        pg.display.update()

main()
