from random import randint

from p5 import *
from p5 import rect_mode

import snake_Head
from snake_Head import *
from snake_Head import running

frame_max = 30
frame_number = 0
from snake_body import *

snake = [(22, 22), (21, 22), (20, 22), (19, 22), (18, 22)]

food = []

grid_size = 90
segment_size = 20
grid_in_pixel=grid_size*segment_size

def setup():
    size(grid_in_pixel, grid_in_pixel)
    set_start()
    print_snake()

    #food anfangswert zuweisen
    for e in range(5):
        x = randint(0, grid_size)
        y = randint(0, grid_size)

        food.append( [x, y] )
    print(f'food{food}')
def has_eaten():
    pass


def draw():
    background(50)
    draw_grid()
    global frame_number, snake
    rect_mode(CENTER)
    draw_food()
    draw_snake()
    if not snake_Head.running:
        return
    frame_number += 1
    if frame_number < frame_max:
        return
    frame_number = 0
    new_position = move_head(snake)
    wachsen = has_eaten()
    snake = move_body(snake, new_position, False)

def draw_food():
    for apple in food:
        fill('red')
        circle(apple[0] * segment_size, apple[1] * segment_size, segment_size / 2)

def draw_snake():
    for segment in snake:
        fill(200, 250, 120)
        rect(segment[0] * segment_size, segment[1] * segment_size, segment_size, segment_size)

def draw_grid():
    stroke(30)
    begin_shape()
    for row in range(grid_size):
        line(0, row * segment_size, grid_in_pixel, row * segment_size)
    for col in range(grid_size):
        line(col * segment_size, 0, col * segment_size, grid_in_pixel)

    end_shape()

def print_snake():
    for segment in snake:
        print(segment)


run()
