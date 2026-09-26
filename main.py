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
    rect_mode(CENTER)
    background(100)
    draw_border()
    global frame_number, snake

    draw_snake()
    if not snake_Head.running:
        return
    frame_number += 2
    if frame_number < frame_max:
        return
    frame_number = 0
    new_position = move_head(snake)
    if not snake_Head.running:
        return
    snake = move_body(snake, new_position, False)

def draw_border():
    no_fill()
    stroke(30)
    stroke_weight(60)
    rect(450,450,900,900)

def draw_snake():
    no_stroke()
    segment_size = 20
    fill(100, 150, 60)
    rect(snake[0][0] * segment_size, snake[0][1] * segment_size, segment_size, segment_size)
    for segment in snake[1:]:
        fill(200, 250, 120)
        rect(segment[0] * segment_size, segment[1] * segment_size, segment_size, segment_size)

def print_snake():
    for segment in snake:
        print(segment)
run()

