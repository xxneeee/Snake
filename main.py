from p5 import *
from p5 import rect_mode

import snake_Head
from snake_Head import *
from snake_Head import running

frame_max = 30
frame_number = 0
from snake_body import *


snake = [(22, 22), (21, 22), (20, 22), (19, 22), (18, 22)]

def setup():
    size(900, 900)
    set_start()
    print_snake()

def draw():
    background(50)
    global frame_number, snake
    rect_mode(CENTER)
    draw_snake()
    if not snake_Head.running:
        return
    frame_number += 1
    if frame_number < frame_max:
        return
    frame_number = 0
    new_position = move_head()
    snake = move_body(snake, new_position, False)

def draw_snake():
    segment_size = 20
    for segment in snake:
        fill(200, 250, 120)
        rect(segment[0] * segment_size, segment[1] * segment_size, segment_size, segment_size)

def print_snake():
    for segment in snake:
        print(segment)
run()

