from p5 import *

from snake_body import *


snake = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)]

def setup():
    size(900, 900)
    print_snake()

def draw():
    background(0)
    rect_mode(CENTER)
    global snake
    snake = move_body(snake, "Ost", False)
    draw_snake()

def draw_snake():
    secment_size = 20
    for secment in snake:
        rect(secment[0] * secment_size, secment[1] * secment_size, secment_size, secment_size)

def print_snake():
    for secment in snake:
        print(secment)
run()

