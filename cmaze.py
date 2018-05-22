import pygame as pg
import random
from cbot import *


class maze():
    def __init__(self):

        ##all lists for maze creation
        self.maze_rects = []
        self.green_trects1 = []
        self.green_trects2 = []
        self.spawn_rects = []
        self.orng_trects = []
        self.switch_rects1 = []
        self.switch_rects2 = []

        ##create walls, fill lists
        self.walls()
        self.transparentwalls()
        self.botspawns()
        self.switchspawns()

        ##colors
        self.black = (0, 0, 0)
        self.grn = (65, 215, 55)
        self.orng = (255, 102, 0)
        self.gray = (200, 200, 200)
        self.lightcyan = (200, 255, 255)

        ##vars for switches
        self.switch_num1 = 0
        self.switch_num2 = 0

        ##button
        self.font = pg.font.SysFont("Black Ops", 100)
        self.sscreen_b = pg.Rect(570, 280, 250, 90)
        self.escreen_b = pg.Rect(600, 420, 200, 90)

        ##model rects
        self.x, self.y = 700, 300
        self.rr1 = pg.Rect(self.x - 150, self.y, 25, 25)
        self.rr2 = pg.Rect(self.x - 155, self.y+5, 35, 15)
        self.rr3 = pg.Rect(self.x - 145, self.y-5, 15, 35)

        self.br1 = pg.Rect(self.x + 150, self.y, 25, 25)
        self.br2 = pg.Rect(self.x + 145, self.y+5, 35, 15)
        self.br3 = pg.Rect(self.x + 155, self.y-5, 15, 35)

        ##bot spawn
        self.bot_list = []
        self.bot_list.append(botplayer(30, 7.5))
        self.bot_list.append(botplayer(30 + 700, 7.5))

        self.bot_spawn_timer = 0
        self.bot_spawn = 1

    def sscreen(self, ds, r, b, rr, bb):
        pg.draw.rect(ds, r, rr)
        pg.draw.rect(ds, b, bb)
        pg.draw.rect(ds, self.gray, self.sscreen_b)

        self.start = self.font.render(("START"), True, (0, 0, 0))
        ds.blit(self.start, (585, 295))

    def cpscreen(self, ds, r, b):
        pg.draw.rect(ds, r, (0, 0, 800, 700))
        pg.draw.rect(ds, b, (700, 0, 800, 700))

        self.chooseplayer = self.font.render(("CHOOSE PLAYER"), True, (0, 0, 0))
        ds.blit(self.chooseplayer, (450, 150))

        pg.draw.rect(ds, (255, 0, 0), self.rr1)
        pg.draw.rect(ds, (255, 0, 0), self.rr2)
        pg.draw.rect(ds, (255, 0, 0), self.rr3)

        pg.draw.rect(ds, (0, 0, 255), self.br1)
        pg.draw.rect(ds, (0, 0, 255), self.br2)
        pg.draw.rect(ds, (0, 0, 255), self.br3)

    def escreen(self, ds, r, b, rr, bb, winner):
        pg.draw.rect(ds, r, rr)
        pg.draw.rect(ds, b, bb)
        pg.draw.rect(ds, self.gray, self.escreen_b)

        self.textSurfaceObj_1 = self.font.render(("WHO KNOWS"), True, self.black)

        if winner == "r":
            self.textSurfaceObj_1 = self.font.render(("RED WINS"), True, self.black)
        elif winner == "b":
            self.textSurfaceObj_1 = self.font.render(("BLU WINS"), True, self.black)

        self.textSurfaceObj_2 = self.font.render(("EXIT"), True, self.black)
        self.textRectObj_2 = self.textSurfaceObj_2.get_rect()
        self.textRectObj_2.center = (700, 465)

        self.textRectObj_1 = self.textSurfaceObj_1.get_rect()
        self.textRectObj_1.center = (700, 225)

        ds.blit(self.textSurfaceObj_1, self.textRectObj_1)
        ds.blit(self.textSurfaceObj_2, self.textRectObj_2)

    def checkbuttons(self, screen, point):
        if screen == "s":
            if self.sscreen_b.collidepoint(point):
                return True
        #elif screen == "c":

        elif screen == "e":
            if self.escreen_b.collidepoint(point):
                return True

    def drawall(self, ds, r, b, rr, br):
        pg.draw.rect(ds, r, rr)
        pg.draw.rect(ds, b, br)

        for wall in self.maze_rects:
            pg.draw.rect(ds, self.black, wall)

        for wall in self.green_trects1:
            pg.draw.rect(ds, self.grn, wall)

        for wall in self.green_trects2:
            pg.draw.rect(ds, self.grn, wall)

        for spawn in self.spawn_rects:
            pg.draw.rect(ds, self.gray, spawn)

        for twall in self.orng_trects:
            pg.draw.rect(ds, self.orng, twall)

        for b in self.bot_list:
            b.drawb(ds)
            b.move(self.checkwall(b.getrects(), b.getrects(), b.getrects()))

    def get_bot_list(self):
        return self.bot_list

    def checkwall(self, rect1, rect2, rect3):
        if rect1.collidelist(self.maze_rects) != -1 or rect1.collidelist(self.orng_trects) != -1:
            return True
        elif rect2.collidelist(self.maze_rects) != -1 or rect2.collidelist(self.orng_trects) != -1:
            return True
        elif rect3.collidelist(self.maze_rects) != -1 or rect3.collidelist(self.orng_trects) != -1:
            return True
        else:
            return False

    def botspawn_function(self):
        self.place1 = [((27.5), (7.5)), ((627.5), (187.5)), ((602.5), (687.5)), ((152.5), (677.5))]
        self.place2 = [((27.5 + 700), (7.5)), ((627.5 + 700), (187.5)), ((602.5 + 700), (687.5)), ((152.5 + 700), (677.5))]

        if self.bot_spawn_timer > 650:
            self.bot_list.append(botplayer(self.place1[self.bot_spawn][0], self.place1[self.bot_spawn][1]))
            self.bot_list.append(botplayer(self.place2[self.bot_spawn][0], self.place2[self.bot_spawn][1]))

            self.bot_spawn += 1
            self.bot_spawn_timer = 0
        else:
            self.bot_spawn_timer += 1

        if self.bot_spawn > 3:
            self.bot_spawn = 0

    def switch_function(self, ds, player1, player2):
        if len(self.green_trects2) > 0:

            if len(self.green_trects2) > 0:
                self.rand1 = random.randint(0, len(self.green_trects2) - 1)
            else:
                self.rand1 = 1

            pg.draw.rect(ds, self.lightcyan, self.switch_rects1[self.switch_num1])

            if (self.switch_rects1[self.switch_num1]).colliderect(player1):
                self.orng_trects.append(self.green_trects2[self.rand1])
                self.green_trects2.remove(self.green_trects2[self.rand1])

                self.switch_num1 += 1

                if self.switch_num1 > len(self.switch_rects1)- 1:
                    self.switch_num1 = 0

        if len(self.green_trects1) > 0:

            if len(self.green_trects1) > 0:
                self.rand2 = random.randint(0, len(self.green_trects1) - 1)
            else:
                self.rand2 = 1

            pg.draw.rect(ds, self.lightcyan, self.switch_rects2[self.switch_num2])

            if (self.switch_rects2[self.switch_num2]).colliderect(player2):
                self.orng_trects.append(self.green_trects1[self.rand2])
                self.green_trects1.remove(self.green_trects1[self.rand2])

                self.switch_num2 += 1

                if self.switch_num2 > len(self.switch_rects2) - 1:
                    self.switch_num2 = 0

    def switchspawns(self):
        self.switch_rects1.append(pg.Rect(285, 140, 15, 15))
        self.switch_rects1.append(pg.Rect(550, 195, 15, 15))
        self.switch_rects1.append(pg.Rect(225, 615, 15, 15))
        self.switch_rects1.append(pg.Rect(480, 630, 15, 15))

        self.switch_rects2.append(pg.Rect(285 + 700, 140, 15, 15))
        self.switch_rects2.append(pg.Rect(550 + 700, 195, 15, 15))
        self.switch_rects2.append(pg.Rect(225 + 700, 615, 15, 15))
        self.switch_rects2.append(pg.Rect(480 + 700, 630, 15, 15))

    def botspawns(self):
        self.bs1 = pg.Rect(25, 5, 35, 35)
        self.spawn_rects.append(self.bs1)
        self.bs2 = pg.Rect(625, 185, 35, 35)
        self.spawn_rects.append(self.bs2)
        self.bs3 = pg.Rect(600, 685, 35, 35)
        self.spawn_rects.append(self.bs3)
        self.bs4 = pg.Rect(150, 675, 35, 35)
        self.spawn_rects.append(self.bs4)

        self.bs5 = pg.Rect(25 + 700, 5, 35, 35)
        self.spawn_rects.append(self.bs5)
        self.bs6 = pg.Rect(625 + 700, 185, 35, 35)
        self.spawn_rects.append(self.bs6)
        self.bs7 = pg.Rect(600 + 700, 685, 35, 35)
        self.spawn_rects.append(self.bs7)
        self.bs8 = pg.Rect(150 + 700, 675, 35, 35)
        self.spawn_rects.append(self.bs8)

    def transparentwalls(self):
        self.tr1 = pg.Rect(350, 190, 10, 55)
        self.green_trects1.append(self.tr1)
        self.tr2 = pg.Rect(240, 0, 10, 45)
        self.green_trects1.append(self.tr2)
        self.tr3 = pg.Rect(535, 45, 45, 10)
        self.green_trects1.append(self.tr3)
        self.tr4 = pg.Rect(410, 255, 10, 45)
        self.green_trects1.append(self.tr4)
        self.tr5 = pg.Rect(260, 390, 10, 50)
        self.green_trects1.append(self.tr5)
        self.tr6 = pg.Rect(475, 530, 10, 50)
        self.green_trects1.append(self.tr6)
        self.tr7 = pg.Rect(50, 590, 10, 40)
        self.green_trects1.append(self.tr7)
        self.tr8 = pg.Rect(120, 680, 10, 50)
        self.green_trects1.append(self.tr8)
        self.tr9 = pg.Rect(360, 670, 60, 10)
        self.green_trects1.append(self.tr9)
        self.tr10 = pg.Rect(1, 440, 49, 10)
        self.green_trects1.append(self.tr10)

        self.tr11 = pg.Rect(350 + 700, 190, 10, 55)
        self.green_trects2.append(self.tr11)
        self.tr12 = pg.Rect(240 + 700, 0, 10, 45)
        self.green_trects2.append(self.tr12)
        self.tr13 = pg.Rect(535 + 700, 45, 45, 10)
        self.green_trects2.append(self.tr13)
        self.tr14 = pg.Rect(410 + 700, 255, 10, 45)
        self.green_trects2.append(self.tr14)
        self.tr15 = pg.Rect(260 + 700, 390, 10, 50)
        self.green_trects2.append(self.tr15)
        self.tr16 = pg.Rect(475 + 700, 530, 10, 50)
        self.green_trects2.append(self.tr16)
        self.tr17 = pg.Rect(50 + 700, 590, 10, 40)
        self.green_trects2.append(self.tr17)
        self.tr18 = pg.Rect(120 + 700, 680, 10, 50)
        self.green_trects2.append(self.tr18)
        self.tr19 = pg.Rect(360 + 700, 670, 60, 10)
        self.green_trects2.append(self.tr19)
        self.tr20 = pg.Rect(1 + 700, 440, 49, 10)
        self.green_trects2.append(self.tr20)

    def walls(self):
        self.topwall = pg.Rect(0, 0, 1400, 1)
        self.rightwall = pg.Rect(1400, 0, 1, 800)
        self.botwall = pg.Rect(0, 800, 1400, 1)
        self.leftwall = pg.Rect(0, 0, 1, 800)
        self.midwall = pg.Rect(700, 0, 1, 800)

        self.r1 = pg.Rect(45, 45, 10, 55)
        self.r2 = pg.Rect(100, 45, 140, 10)
        self.r3 = pg.Rect(45, 100, 150, 10)
        self.r4 = pg.Rect(240, 45, 10, 90)
        self.r5 = pg.Rect(250, 100, 45, 10)
        self.r6 = pg.Rect(295, 45, 55, 10)
        self.r7 = pg.Rect(350, 45, 10, 145)
        self.r8 = pg.Rect(405, 0, 10, 110)
        self.r9 = pg.Rect(195, 190, 100, 10)
        self.r10 = pg.Rect(185, 155, 10, 45)
        self.r11 = pg.Rect(130, 110, 10, 90)
        self.r12 = pg.Rect(0, 155, 70, 10)
        self.r13 = pg.Rect(460, 45, 65, 10)
        self.r14 = pg.Rect(525, 0, 10, 55)
        self.r15 = pg.Rect(460, 100, 75, 10)
        self.r16 = pg.Rect(460, 110, 10, 45)
        self.r17 = pg.Rect(405, 155, 65, 10)
        self.r18 = pg.Rect(580, 45, 65, 10)
        self.r19 = pg.Rect(580, 55, 10, 45)
        self.r20 = pg.Rect(635, 55, 10, 100)
        self.r21 = pg.Rect(535, 155, 110, 10)
        ###
        self.r22 = pg.Rect(0, 245, 105, 10)
        self.r23 = pg.Rect(160, 245, 200, 10)
        self.r24 = pg.Rect(410, 245, 85, 10)
        self.r25 = pg.Rect(555, 245, 145, 10)
        ###
        self.r26 = pg.Rect(50, 300, 90, 10)
        self.r27 = pg.Rect(50, 300, 10, 90)
        self.r28 = pg.Rect(50, 380, 90, 10)
        self.r29 = pg.Rect(130, 300, 10, 90)
        self.r30 = pg.Rect(190, 300, 90, 10)
        self.r31 = pg.Rect(190, 300, 10, 90)
        self.r32 = pg.Rect(190, 380, 90, 10)
        self.r33 = pg.Rect(270, 300, 10, 90)
        self.r34 = pg.Rect(330, 300, 90, 10)
        self.r35 = pg.Rect(330, 300, 10, 90)
        self.r36 = pg.Rect(330, 380, 90, 10)
        self.r37 = pg.Rect(410, 300, 10, 90)
        self.r38 = pg.Rect(470, 300, 90, 10)
        self.r39 = pg.Rect(470, 300, 10, 90)
        self.r40 = pg.Rect(470, 380, 90, 10)
        self.r41 = pg.Rect(550, 300, 10, 90)
        
        self.r42 = pg.Rect(120, 440, 90, 10)
        self.r43 = pg.Rect(120, 440, 10, 90)
        self.r44 = pg.Rect(120, 520, 90, 10)
        self.r45 = pg.Rect(200, 440, 10, 90)
        self.r46 = pg.Rect(260, 440, 90, 10)
        self.r47 = pg.Rect(260, 440, 10, 90)
        self.r48 = pg.Rect(260, 520, 90, 10)
        self.r49 = pg.Rect(340, 440, 10, 90)
        self.r50 = pg.Rect(400, 440, 90, 10)
        self.r51 = pg.Rect(400, 440, 10, 90)
        self.r52 = pg.Rect(400, 520, 90, 10)
        self.r53 = pg.Rect(480, 440, 10, 90)
        self.r54 = pg.Rect(540, 440, 90, 10)
        self.r55 = pg.Rect(540, 440, 10, 90)
        self.r56 = pg.Rect(540, 520, 90, 10)
        self.r57 = pg.Rect(620, 440, 10, 90)
        
        self.r58 = pg.Rect(610, 300, 10, 90)
        self.r59 = pg.Rect(610, 300, 90, 10)
        self.r60 = pg.Rect(50, 440, 10, 90)
        self.r61 = pg.Rect(0, 520, 50, 10)
        ###
        self.r62 = pg.Rect(0, 580, 60, 10)
        self.r63 = pg.Rect(120, 580, 365, 10)
        self.r64 = pg.Rect(540, 580, 160, 10)
        ###
        self.r65 = pg.Rect(50, 630, 70, 10)
        self.r66 = pg.Rect(120, 630, 10, 50)
        self.r67 = pg.Rect(50, 690, 10, 40)
        self.r68 = pg.Rect(50, 730, 135, 10)
        self.r69 = pg.Rect(190, 580, 10, 85)
        self.r70 = pg.Rect(200, 655, 90, 10)
        self.r71 = pg.Rect(240, 725, 10, 75)
        self.r72 = pg.Rect(300, 725, 50, 10)
        self.r73 = pg.Rect(350, 635, 10, 100)
        self.r74 = pg.Rect(420, 580, 10, 100)
        self.r75 = pg.Rect(565, 650, 10, 90)
        self.r76 = pg.Rect(420, 730, 75, 10)
        self.r77 = pg.Rect(485, 680, 10, 120)
        self.r78 = pg.Rect(565, 650, 90, 10)
        
        self.maze_rects.append(self.r1)
        self.maze_rects.append(self.r2)
        self.maze_rects.append(self.r3)
        self.maze_rects.append(self.r4)
        self.maze_rects.append(self.r5)
        self.maze_rects.append(self.r6)
        self.maze_rects.append(self.r7)
        self.maze_rects.append(self.r8)
        self.maze_rects.append(self.r9)
        self.maze_rects.append(self.r10)
        self.maze_rects.append(self.r11)
        self.maze_rects.append(self.r12)
        self.maze_rects.append(self.r13)
        self.maze_rects.append(self.r14)
        self.maze_rects.append(self.r15)
        self.maze_rects.append(self.r16)
        self.maze_rects.append(self.r17)
        self.maze_rects.append(self.r18)
        self.maze_rects.append(self.r19)
        self.maze_rects.append(self.r20)
        self.maze_rects.append(self.r21)
        self.maze_rects.append(self.r22)
        self.maze_rects.append(self.r23)
        self.maze_rects.append(self.r24)
        self.maze_rects.append(self.r25)
        self.maze_rects.append(self.r26)
        self.maze_rects.append(self.r27)
        self.maze_rects.append(self.r28)
        self.maze_rects.append(self.r29)
        self.maze_rects.append(self.r30)
        self.maze_rects.append(self.r31)
        self.maze_rects.append(self.r32)
        self.maze_rects.append(self.r33)
        self.maze_rects.append(self.r34)
        self.maze_rects.append(self.r35)
        self.maze_rects.append(self.r36)
        self.maze_rects.append(self.r37)
        self.maze_rects.append(self.r38)
        self.maze_rects.append(self.r39)
        self.maze_rects.append(self.r40)
        self.maze_rects.append(self.r41)
        
        self.maze_rects.append(self.r42)
        self.maze_rects.append(self.r43)
        self.maze_rects.append(self.r44)
        self.maze_rects.append(self.r45)
        self.maze_rects.append(self.r46)
        self.maze_rects.append(self.r47)
        self.maze_rects.append(self.r48)
        self.maze_rects.append(self.r49)
        self.maze_rects.append(self.r50)
        self.maze_rects.append(self.r51)
        self.maze_rects.append(self.r52)
        self.maze_rects.append(self.r53)
        self.maze_rects.append(self.r54)
        self.maze_rects.append(self.r55)
        self.maze_rects.append(self.r56)
        self.maze_rects.append(self.r57)
        self.maze_rects.append(self.r58)
        self.maze_rects.append(self.r59)
        self.maze_rects.append(self.r60)
        self.maze_rects.append(self.r61)

        self.maze_rects.append(self.r62)
        self.maze_rects.append(self.r63)
        self.maze_rects.append(self.r64)
        
        self.maze_rects.append(self.r65)
        self.maze_rects.append(self.r66)
        self.maze_rects.append(self.r67)
        self.maze_rects.append(self.r68)
        self.maze_rects.append(self.r69)
        self.maze_rects.append(self.r70)
        self.maze_rects.append(self.r71)
        self.maze_rects.append(self.r72)
        self.maze_rects.append(self.r73)
        self.maze_rects.append(self.r74)
        self.maze_rects.append(self.r75)
        self.maze_rects.append(self.r76)
        self.maze_rects.append(self.r77)
        self.maze_rects.append(self.r78)

        ###################################################################

        self.r79 = pg.Rect(45 + 700, 45, 10, 55)
        self.r80 = pg.Rect(100 + 700, 45, 140, 10)
        self.r81 = pg.Rect(45 + 700, 100, 150, 10)
        self.r82 = pg.Rect(240 + 700, 45, 10, 110)
        self.r83 = pg.Rect(250 + 700, 100, 45, 10)
        self.r84 = pg.Rect(295 + 700, 45, 55, 10)
        self.r85 = pg.Rect(350 + 700, 45, 10, 145)
        self.r86 = pg.Rect(405 + 700, 0, 10, 110)
        self.r87 = pg.Rect(195 + 700, 190, 100, 10)
        self.r88 = pg.Rect(185 + 700, 155, 10, 45)
        self.r89 = pg.Rect(130 + 700, 110, 10, 90)
        self.r90 = pg.Rect(0 + 700, 155, 70, 10)
        self.r91 = pg.Rect(460 + 700, 45, 65, 10)
        self.r92 = pg.Rect(525 + 700, 0, 10, 55)
        self.r93 = pg.Rect(460 + 700, 100, 75, 10)
        self.r94 = pg.Rect(460 + 700, 110, 10, 45)
        self.r95 = pg.Rect(405 + 700, 155, 65, 10)
        self.r96 = pg.Rect(580 + 700, 45, 65, 10)
        self.r97 = pg.Rect(580 + 700, 55, 10, 45)
        self.r98 = pg.Rect(635 + 700, 55, 10, 100)
        self.r99 = pg.Rect(535 + 700, 155, 110, 10)
        ###
        self.r100 = pg.Rect(0 + 700, 245, 105, 10)
        self.r101 = pg.Rect(160 + 700, 245, 200, 10)
        self.r102 = pg.Rect(410 + 700, 245, 85, 10)
        self.r103 = pg.Rect(555 + 700, 245, 145, 10)
        ###
        self.r104 = pg.Rect(50 + 700, 300, 90, 10)
        self.r105 = pg.Rect(50 + 700, 300, 10, 90)
        self.r106 = pg.Rect(50 + 700, 380, 90, 10)
        self.r107 = pg.Rect(130 + 700, 300, 10, 90)
        self.r108 = pg.Rect(190 + 700, 300, 90, 10)
        self.r109 = pg.Rect(190 + 700, 300, 10, 90)
        self.r110 = pg.Rect(190 + 700, 380, 90, 10)
        self.r111 = pg.Rect(270 + 700, 300, 10, 90)
        self.r112 = pg.Rect(330 + 700, 300, 90, 10)
        self.r113 = pg.Rect(330 + 700, 300, 10, 90)
        self.r114 = pg.Rect(330 + 700, 380, 90, 10)
        self.r115 = pg.Rect(410 + 700, 300, 10, 90)
        self.r116 = pg.Rect(470 + 700, 300, 90, 10)
        self.r117 = pg.Rect(470 + 700, 300, 10, 90)
        self.r118 = pg.Rect(470 + 700, 380, 90, 10)
        self.r119 = pg.Rect(550 + 700, 300, 10, 90)

        self.r120 = pg.Rect(120 + 700, 440, 90, 10)
        self.r121 = pg.Rect(120 + 700, 440, 10, 90)
        self.r122 = pg.Rect(120 + 700, 520, 90, 10)
        self.r123 = pg.Rect(200 + 700, 440, 10, 90)
        self.r124 = pg.Rect(260 + 700, 440, 90, 10)
        self.r125 = pg.Rect(260 + 700, 440, 10, 90)
        self.r126 = pg.Rect(260 + 700, 520, 90, 10)
        self.r127 = pg.Rect(340 + 700, 440, 10, 90)
        self.r128 = pg.Rect(400 + 700, 440, 90, 10)
        self.r129 = pg.Rect(400 + 700, 440, 10, 90)
        self.r130 = pg.Rect(400 + 700, 520, 90, 10)
        self.r131 = pg.Rect(480 + 700, 440, 10, 90)
        self.r132 = pg.Rect(540 + 700, 440, 90, 10)
        self.r133 = pg.Rect(540 + 700, 440, 10, 90)
        self.r134 = pg.Rect(540 + 700, 520, 90, 10)
        self.r135 = pg.Rect(620 + 700, 440, 10, 90)

        self.r136 = pg.Rect(610 + 700, 300, 10, 90)
        self.r137 = pg.Rect(610 + 700, 300, 90, 10)
        self.r138 = pg.Rect(50 + 700, 440, 10, 90)
        self.r139 = pg.Rect(0 + 700, 520, 50, 10)
        ###
        self.r140 = pg.Rect(0 + 700, 580, 60, 10)
        self.r141 = pg.Rect(120 + 700, 580, 365, 10)
        self.r142 = pg.Rect(540 + 700, 580, 160, 10)
        ###
        self.r143 = pg.Rect(50 + 700, 630, 70, 10)
        self.r144 = pg.Rect(120 + 700, 630, 10, 50)
        self.r145 = pg.Rect(50 + 700, 690, 10, 40)
        self.r146 = pg.Rect(50 + 700, 730, 135, 10)
        self.r147 = pg.Rect(190 + 700, 580, 10, 85)
        self.r148 = pg.Rect(200 + 700, 655, 90, 10)
        self.r149 = pg.Rect(240 + 700, 725, 10, 75)
        self.r150 = pg.Rect(300 + 700, 725, 50, 10)
        self.r151 = pg.Rect(350 + 700, 635, 10, 100)
        self.r152 = pg.Rect(420 + 700, 580, 10, 100)
        self.r153 = pg.Rect(565 + 700, 650, 10, 90)
        self.r154 = pg.Rect(420 + 700, 730, 75, 10)
        self.r155 = pg.Rect(485 + 700, 680, 10, 120)
        self.r156 = pg.Rect(565 + 700, 650, 90, 10)

        self.maze_rects.append(self.r79)
        self.maze_rects.append(self.r80)
        self.maze_rects.append(self.r81)
        self.maze_rects.append(self.r82)
        self.maze_rects.append(self.r83)
        self.maze_rects.append(self.r84)
        self.maze_rects.append(self.r85)
        self.maze_rects.append(self.r86)
        self.maze_rects.append(self.r87)
        self.maze_rects.append(self.r88)
        self.maze_rects.append(self.r89)
        self.maze_rects.append(self.r90)
        self.maze_rects.append(self.r91)
        self.maze_rects.append(self.r92)
        self.maze_rects.append(self.r93)
        self.maze_rects.append(self.r94)
        self.maze_rects.append(self.r95)
        self.maze_rects.append(self.r96)
        self.maze_rects.append(self.r97)
        self.maze_rects.append(self.r98)
        self.maze_rects.append(self.r99)
        self.maze_rects.append(self.r100)
        self.maze_rects.append(self.r101)
        self.maze_rects.append(self.r102)
        self.maze_rects.append(self.r103)
        self.maze_rects.append(self.r104)
        self.maze_rects.append(self.r105)
        self.maze_rects.append(self.r106)
        self.maze_rects.append(self.r107)
        self.maze_rects.append(self.r108)
        self.maze_rects.append(self.r109)
        self.maze_rects.append(self.r110)
        self.maze_rects.append(self.r111)
        self.maze_rects.append(self.r112)
        self.maze_rects.append(self.r113)
        self.maze_rects.append(self.r114)
        self.maze_rects.append(self.r115)
        self.maze_rects.append(self.r116)
        self.maze_rects.append(self.r117)
        self.maze_rects.append(self.r118)
        self.maze_rects.append(self.r119)

        self.maze_rects.append(self.r120)
        self.maze_rects.append(self.r121)
        self.maze_rects.append(self.r122)
        self.maze_rects.append(self.r123)
        self.maze_rects.append(self.r124)
        self.maze_rects.append(self.r125)
        self.maze_rects.append(self.r126)
        self.maze_rects.append(self.r127)
        self.maze_rects.append(self.r128)
        self.maze_rects.append(self.r129)
        self.maze_rects.append(self.r130)
        self.maze_rects.append(self.r131)
        self.maze_rects.append(self.r132)
        self.maze_rects.append(self.r133)
        self.maze_rects.append(self.r134)
        self.maze_rects.append(self.r135)
        self.maze_rects.append(self.r136)
        self.maze_rects.append(self.r137)
        self.maze_rects.append(self.r138)
        self.maze_rects.append(self.r139)

        self.maze_rects.append(self.r140)
        self.maze_rects.append(self.r141)
        self.maze_rects.append(self.r142)

        self.maze_rects.append(self.r143)
        self.maze_rects.append(self.r144)
        self.maze_rects.append(self.r145)
        self.maze_rects.append(self.r146)
        self.maze_rects.append(self.r147)
        self.maze_rects.append(self.r148)
        self.maze_rects.append(self.r149)
        self.maze_rects.append(self.r150)
        self.maze_rects.append(self.r151)
        self.maze_rects.append(self.r152)
        self.maze_rects.append(self.r153)
        self.maze_rects.append(self.r154)
        self.maze_rects.append(self.r155)
        self.maze_rects.append(self.r156)

        self.maze_rects.append(self.topwall)
        self.maze_rects.append(self.rightwall)
        self.maze_rects.append(self.leftwall)
        self.maze_rects.append(self.botwall)
        self.maze_rects.append(self.midwall)
