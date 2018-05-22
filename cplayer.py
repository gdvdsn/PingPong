from cmaze import *

class player():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.dir = 0
        
        self.r1 = pg.Rect(self.x, self.y, 25, 25)
        self.r2 = pg.Rect(self.x-5, self.y+5, 35, 15)
        self.r3 = pg.Rect(self.x+5, self.y-5, 15, 35)

    def drawp(self, ds, col):
        self.r1 = pg.Rect(self.x, self.y, 25, 25)
        self.r2 = pg.Rect(self.x-5, self.y+5, 35, 15)
        self.r3 = pg.Rect(self.x+5, self.y-5, 15, 35)

        pg.draw.rect(ds, col, self.r1)
        pg.draw.rect(ds, col, self.r2)
        pg.draw.rect(ds, col, self.r3)

    def checkmove1(self):
        if self.x + 30 < 700 and self.x - 5 > 0 and self.y + 30 < 800 and self.y - 5 > 0:
            if self.dir == 0:
                self.x += 2
            elif self.dir == 90:
                self.y -= 2
            elif self.dir == 180:
                self.x -= 2
            elif self.dir == 270:
                self.y += 2
        elif self.x + 30 >= 700:
            self.x -= 1
            self.dir = 2
        elif self.x - 5 <= 0:
            self.x += 1
            self.dir = 2
        elif self.y + 30 >= 800:
            self.y -= 1
            self.dir = 2
        elif self.y - 5 <= 0:
            self.y += 1
            self.dir = 2

    def checkmove2(self):
        if self.x + 30 < 1400 and self.x - 5 > 701 and self.y + 30 < 800 and self.y - 5 > 0:
            if self.dir == 0:
                self.x += 2
            elif self.dir == 90:
                self.y -= 2
            elif self.dir == 180:
                self.x -= 2
            elif self.dir == 270:
                self.y += 2
        elif self.x + 30 >= 1400:
            self.x -= 2
            self.dir = 2
        elif self.x - 5 <= 701:
            self.x += 2
            self.dir = 2
        elif self.y + 30 >= 800:
            self.y -= 2
            self.dir = 2
        elif self.y - 5 <= 0:
            self.y += 2
            self.dir = 2

    def atwall(self):
        if self.dir == 0:
            self.x -= 5
        elif self.dir == 90:
            self.y += 5
        elif self.dir == 180:
            self.x += 5
        elif self.dir == 270:
            self.y -= 5

        self.dir = 2

    def getrects(self):
        return self.r1, self.r2, self.r3

    def turn1(self, event):
        if event == pg.K_d:
            self.dir = 0
        if event == pg.K_w:
            self.dir = 90
        if event == pg.K_a:
            self.dir = 180
        if event == pg.K_s:
            self.dir = 270

    def turn2(self, event):
        if event == pg.K_RIGHT:
            self.dir = 0
        if event == pg.K_UP:
            self.dir = 90
        if event == pg.K_LEFT:
            self.dir = 180
        if event == pg.K_DOWN:
            self.dir = 270
