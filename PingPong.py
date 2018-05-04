import pygame as pg, sys, time, random
from pygame.locals import *
from cpaddle import paddle

pg.init()

##Create Display
display_surf = pg.display.set_mode((1400, 800))
pg.display.set_caption("Pong")

##Create color scheme for game
gray_table = (130, 130, 130)
dark_gray_table = (80, 80, 80)
black_net = (0, 0, 0)

red_paddle_color = (255, 0, 0)
blue_paddle_color = (0, 0, 255)

white_ball = (255, 255, 255)

peach_background = (200, 175, 150)

ss_red = (255, 180, 180)
ss_blue = (180, 180, 255)

##Define Paddles
red_paddle_rect = paddle(1285, 340, 15, 120)
blue_paddle_rect = paddle(100, 340, 15, 120)

red_paddle, blue_paddle = paddle.images(6)

##Define board
outer_edge_table = pg.Rect(70, 50, 1260, 700)
inner_edge_table = pg.Rect(77.5, 57.5, 1245, 685)
net = pg.Rect(697, 50, 6, 700)

##Define Starting Screen
screen = "ss"

ss_red_half = pg.Rect(1, 1, 700, 800)
ss_blue_half = pg.Rect(701, 1, 700, 800)

fontObj_ss = pg.font.SysFont("Black Ops", 200)
textSurfaceObj_ss = fontObj_ss.render(("PING PONG"), True, black_net)
textRectObj_ss = textSurfaceObj_ss.get_rect()
textRectObj_ss.center = (737, 300)

fontObj_ss2 = pg.font.SysFont("Black Ops", 80)
textSurfaceObj_ss2 = fontObj_ss2.render(("Press ' ' to Begin"), True, black_net)
textRectObj_ss2 = textSurfaceObj_ss2.get_rect()
textRectObj_ss2.center = (705, 500)

##Define playmaker screen
gamemode = "null"

fontObj_ps = pg.font.SysFont("Black Ops", 100)
textSurfaceObj_ps = fontObj_ps.render(("PLAYMAKER"), True, black_net)
textRectObj_ps = textSurfaceObj_ps.get_rect()
textRectObj_ps.center = (700, 75)

fontObj_ps2 = pg.font.SysFont("Black Ops", 50)
textSurfaceObj_ps2 = fontObj_ps2.render(("Create your game here"), True, black_net)
textRectObj_ps2 = textSurfaceObj_ps2.get_rect()
textRectObj_ps2.center = (700, 145)

#ps 1
b1 = pg.Rect(250, 350, 250, 75)
b2 = pg.Rect(900, 350, 250, 75)

fontObj_buttontext = pg.font.SysFont("Black Ops", 35)
fontObj_buttontext_large = pg.font.SysFont("Black Ops", 100)

textSurfaceObj_b1 = fontObj_buttontext.render(("Games/Sets"), True, black_net)
textSurfaceObj_b2 = fontObj_buttontext.render(("Within Time"), True, black_net)

#ps 2 g/s
games = 1
sets = 0

b3 = pg.Rect(250, 325, 250, 75)
b4 = pg.Rect(250, 500, 250, 75)

textSurfaceObj_b3 = fontObj_buttontext.render(("Games"), True, black_net)
textSurfaceObj_b4 = fontObj_buttontext.render(("Sets"), True, black_net)

b5 = pg.Rect(600, 325, 75, 75)
b6 = pg.Rect(600, 500, 75, 75)

textSurfaceObj_b5 = fontObj_buttontext_large.render(("+"), True, black_net)
textSurfaceObj_b6 = fontObj_buttontext_large.render(("+"), True, black_net)

b7 = pg.Rect(725, 325, 75, 75)
b8 = pg.Rect(725, 500, 75, 75)

textSurfaceObj_b7 = fontObj_buttontext_large.render(("-"), True, black_net)
textSurfaceObj_b8 = fontObj_buttontext_large.render(("-"), True, black_net)

b9 = pg.Rect(900, 325, 125, 75)
b10 = pg.Rect(900, 500, 125, 75)

textSurfaceObj_b9 = fontObj_buttontext.render((str(games)), True, black_net)
textSurfaceObj_b10 = fontObj_buttontext.render((str(sets)), True, black_net)

b11 = pg.Rect(625, 660, 150, 65)

textSurfaceObj_b11 = fontObj_buttontext.render("Play", True, black_net)

##Define serve hit meter
D_up = True
D_down = False

meter_up = 1
meter_down = 1

def create_main_screen(display):
    pg.draw.rect(display, ss_red, ss_red_half)
    pg.draw.rect(display, ss_blue, ss_blue_half)

    display.blit(textSurfaceObj_ss, textRectObj_ss)
    display.blit(textSurfaceObj_ss2, textRectObj_ss2)

def create_play_maker(display):
    pg.draw.rect(display, ss_red, ss_red_half)
    pg.draw.rect(display, ss_blue, ss_blue_half)

    display.blit(textSurfaceObj_ps, textRectObj_ps)
    display.blit(textSurfaceObj_ps2, textRectObj_ps2)

    pg.draw.rect(display, peach_background, b1)
    pg.draw.rect(display, peach_background, b2)

    display.blit(textSurfaceObj_b1, (298, 372))
    display.blit(textSurfaceObj_b2, (951, 372))

def pm2_set_game(display):
    pg.draw.rect(display, ss_red, ss_red_half)
    pg.draw.rect(display, ss_blue, ss_blue_half)

    display.blit(textSurfaceObj_ps, textRectObj_ps)
    display.blit(textSurfaceObj_ps2, textRectObj_ps2)

    pg.draw.rect(display, peach_background, b3)
    pg.draw.rect(display, peach_background, b4)

    display.blit(textSurfaceObj_b3, (325, 350))
    display.blit(textSurfaceObj_b4, (345, 525))

    pg.draw.rect(display, peach_background, b5)
    pg.draw.rect(display, peach_background, b6)

    display.blit(textSurfaceObj_b5, (616, 323))
    display.blit(textSurfaceObj_b6, (616, 498))

    pg.draw.rect(display, peach_background, b7)
    pg.draw.rect(display, peach_background, b8)

    display.blit(textSurfaceObj_b7, (750, 325))
    display.blit(textSurfaceObj_b8, (750, 500))

    pg.draw.rect(display, peach_background, b9)
    pg.draw.rect(display, peach_background, b10)

    textSurfaceObj_b9 = fontObj_buttontext.render((str(games)), True, black_net)
    textSurfaceObj_b10 = fontObj_buttontext.render((str(sets)), True, black_net)

    display.blit(textSurfaceObj_b9, (955, 350))
    display.blit(textSurfaceObj_b10, (955, 525))

    pg.draw.rect(display, peach_background, b11)

    display.blit(textSurfaceObj_b11, (672, 680))

def pm2_timergame(display):
    pg.draw.rect(display, ss_red, ss_red_half)
    pg.draw.rect(display, ss_blue, ss_blue_half)

    display.blit(textSurfaceObj_ps, textRectObj_ps)
    display.blit(textSurfaceObj_ps2, textRectObj_ps2)

while True:
    #Run starting screen
    if screen == "ss":
        create_main_screen(display_surf)

    #Run play maker screen
    if screen == "ps":
        create_play_maker(display_surf)

    if screen == "pm2_set/game":
        pm2_set_game(display_surf)

        if games > 4:
            games = 0
            sets += 1
        if sets == 5:
            games = 0
        if sets == 0 and games == 0:
            games = 1

    if screen == "pm2_timergame":
        pm2_timergame(display_surf)

    #Run game
    if screen == "g":
        display_surf.fill(peach_background)
        pg.draw.rect(display_surf, dark_gray_table, outer_edge_table)
        pg.draw.rect(display_surf, gray_table, inner_edge_table)
        pg.draw.rect(display_surf, black_net, net)

        blue_paddle_rect.update_display(ss_blue, blue_paddle)
        red_paddle_rect.update_display(ss_red, red_paddle)

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        ##Check to exit starting screen
        if event.type == KEYDOWN:
            print("Key down")
            if screen == "pm2_set/game" or screen == "pm2_timergame" or screen == "ss":
                if event.key == K_SPACE:
                    screen = "ps"
            if screen == "g":
                blue_paddle_rect.update_rect(event, 'b')
                red_paddle_rect.update_rect(event, 'r')

        if event.type == pg.MOUSEBUTTONDOWN:
            print("Mouse button")
            if event.button == 1:
                if screen == "ps":
                    if b1.collidepoint(event.pos):
                        gamemode = "setgames"
                        screen = "pm2_set/game"

                    if b2.collidepoint(event.pos):
                        gamemode = "timer"
                        screen = "pm2_timergame"
                if screen == "pm2_set/game":
                    if b5.collidepoint(event.pos):
                        print("+++")
                        if sets < 5:
                            games += 1
                        else:
                            print("You cannot add any more games!")
                    elif b7.collidepoint(event.pos):
                        print("---")
                        if games > 0:
                            games -= 1
                        else:
                            print("You cannot subtract any more games!")

                    if b6.collidepoint(event.pos):
                        if sets < 5:
                            sets += 1
                        else:
                            print("You cannot add any more sets!")
                    elif b8.collidepoint(event.pos):
                        if sets > 0:
                            sets -= 1
                        else:
                            print("You cannot subtract any more sets!")

                    if b11.collidepoint(event.pos):
                        screen = "g"

    pg.display.update()
