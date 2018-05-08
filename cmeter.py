import pygame as pg

class meter():

    def __init__(self, x, y):
        ##Create color
        self.WHITE = (255, 255, 255)
        self.peach_background = (175, 200, 225)

        self.meter_rect = pg.Rect(x, y, 25, 1)

        self.D_up = True
        self.D_down = False

        self.meter_up= 1
        self.meter_down = 1

        self.nx = 6

    def go_meter(self, display_surf):
        display_surf.fill(self.WHITE)

        pg.draw.rect(display_surf, self.peach_background, self.meter_rect)

        if self.D_up == True and self.D_down == False:
            self.meter_rect.h -= self.nx
            self.meter_up += self.nx

            if self.meter_up > 498:
                self.meter_up = 1
                self.D_up = False
                self.D_down = True

        elif self.D_down == True and self.D_up == False:
            self.meter_rect.h += self.nx
            self.meter_down += self.nx

            if self.meter_down > 498:
                self.meter_down = 1
                self.D_up = True
                self.D_down = False
