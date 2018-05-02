import pygame as pg

pg.init()

g = "null"

print(g)

def change_g():
    global g
    g = "gameset"

def print_g():
    print(g)

change_g()
print_g()

