import pygame as pg

class paddle:
    def __init__(self, x, y, l, w):
        self.rx = x
        self.ry = y
        self.rect = pg.Rect(self.rx, self.ry, l, w)

    def update_display(self, win, img):
        #print("update display")
        win.blit(img, self.rect)

    def images(self):
        rpaddle = pg.image.load('red_paddle.png')
        rpaddle = pg.transform.scale(rpaddle, (15, 120))
        bpaddle = pg.image.load('blue_paddle.png')
        bpaddle = pg.transform.scale(bpaddle, (15, 120))

        return rpaddle, bpaddle

    def update_rect(self, event, note):
        print("update_rect", self.rx, self.ry)
        ##UP FOR PADDLES
        if note == 'b':
            if event.key == pg.K_w and self.ry > 0:
                self.ry -= 6
        if note == 'r':
            if event.key == pg.K_UP and self.ry > 0:
                self.ry -= 6

        ##DOWN FOR PADDLES
        if note == 'b':
            if event.key == pg.K_s and self.ry + 120 < 800:
                self.ry += 6
        if note == 'r':
            if event.key == pg.K_DOWN and self.ry + 120 < 800:
                self.ry += 6

        ##LEFT FOR PADDLES
        if note == 'b':
            if event.key == pg.K_a and self.rx > 0:
                self.rx -= 6
        if note == 'r':
            if event.key == pg.K_LEFT and self.rx > 703:
                self.rx -= 6

        ##RIGHT FOR PADDLES
        if note == 'b':
            if event.key == pg.K_d and self.rx + 15 < 697:
                self.rx += 6
        if note == 'r':
            if event.key == pg.K_RIGHT and self.rx + 15 < 1400:
                self.rx += 6
