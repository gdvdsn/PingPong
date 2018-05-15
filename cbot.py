import pygame as pg

class bot():
    def __init__(self):
        self.x = 2
        self.y = 2

        self.dir = 180

        self.r = pg.Rect(self.x, self.y, 30, 30)

    def drawb(self, ds, col):
        pg.draw.rect(ds, col, self.r)

    def move(self, bool):
        print(2)
