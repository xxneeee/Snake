from p5 import *

snake = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)]

def setup():
    size(200, 200)
    print_snake()

def draw():
    rect_mode(CENTER)
    draw_snake()

def draw_snake():
    secment_size = 20
    for secment in snake:
        rect(secment[0] * secment_size, secment[1] * secment_size, secment_size, secment_size)

def print_snake():
    for secment in snake:
        print(secment)
run()

