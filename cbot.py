import pygame as pg
from cmaze import *
import random

class botplayer():
    def __init__(self, nx, ny):
        self.x, self.y = nx, ny

        self.dir = 0

        self.gray = (100, 100, 100)
        self.r = pg.Rect(self.x, self.y, 30, 30)

    def getrects(self):
        return self.r

    def drawb(self, ds):
        self.r = pg.Rect(self.x, self.y, 30, 30)

        pg.draw.rect(ds, self.gray, self.r)

    def go(self):
        if self.dir == 0:
            self.x += 2
        elif self.dir == 90:
            self.y -= 2
        elif self.dir == 180:
            self.x -= 2
        elif self.dir == 270:
            self.y += 2

    def nogo(self):
        if self.dir == 0:
            self.x -= 4
        elif self.dir == 90:
            self.y += 4
        elif self.dir == 180:
            self.x += 4
        elif self.dir == 270:
            self.y -= 4

        self.dir = self.changedir()

    def move(self, bool):
        if bool == False:
            self.go()
        else:
            self.nogo()

            self.dir = self.changedir()

    def changedir(self):
        self.dirs = [0, 90, 180, 270]

        self.dirs.remove(self.dir)

        self.ndir = random.randint(0, 2)

        return self.dirs[self.ndir]

    def checkred(self, players):
        for a in players[0]:
            if self.r.colliderect(a):
                return "b"
            else:
                return False

    def checkblu(self, players):
        for c in players[1]:
            if self.r.colliderect(c):
                return "r"
            else:
                return False
