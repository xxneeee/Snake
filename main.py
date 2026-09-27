from operator import truediv

from p5 import *
from p5 import rect_mode

from random import randint

import snake_Head
from snake_Head import *
from snake_Head import running

frame_max = 10
frame_number = 0
from snake_body import *


snake = []

food = []

f = None

grid_size = 45
segment_size = 20
grid_in_pixel=grid_size*segment_size

def setup():
    size(900, 900)
    reset_game()
    print_snake()

def reset_game():
    global snake, f, food
    size(grid_in_pixel, grid_in_pixel)
    set_start()
    snake = [(22, 22), (21, 22), (20, 22), (19, 22), (18, 22)]
    snake_Head.running = True
    print ('Reset game')
    f = create_font("Arial.ttf", 144)  # STEP 2 Create Font

    #food anfangswert zuweisen
    food = []
    for e in range(5):
        random_food_position()

def has_eaten(position):
   #food gefunden
    global food
    print(f'{position} {food}')
    if position in food:
        food.remove(position)
        random_food_position()
        print(f'eaten')
        return True
    #food nicht gefunden
    return False

def random_food_position():
    x = randint(2, grid_size -2)
    y = randint(2, grid_size -2)

    food.append((x, y))

def draw():
    rect_mode(CENTER)
    background(100)
    draw_grid()
    global frame_number, snake, f
    draw_food()
    draw_snake()
    if not snake_Head.running:
        end_screen()
        return
    frame_number += 5
    if frame_number < frame_max:
        return
    frame_number = 0
    new_position = move_head(snake)
    if not snake_Head.running:

        return
    wachsen = has_eaten(new_position)
    snake = move_body(snake, new_position, wachsen)

def end_screen():
    text_font(f)
    text_align(CENTER, CENTER)
    fill(255)
    no_stroke()
    text("The End!", int(grid_in_pixel / 2), 100)


def draw_food():
    no_stroke()
    fill('red')
    for apple in food:
        circle(apple[0] * segment_size, apple[1] * segment_size, segment_size / 2)

def draw_border():
    no_fill()
    stroke(30)
    stroke_weight(60)
    rect_mode(CENTER)
    rect(450,450,900,900)

def draw_snake():
    no_stroke()
    segment_size = 20
    fill(100, 150, 60)
    rect(snake[0][0] * segment_size, snake[0][1] * segment_size, segment_size, segment_size)
    for segment in snake[1:]:
        fill(200, 250, 120)
        rect(segment[0] * segment_size, segment[1] * segment_size, segment_size, segment_size)

def draw_grid():
    stroke(30)
    stroke_weight(1)
    begin_shape()
    offset = int(segment_size / 2)
    for row in range(grid_size):
        line(0, offset + row * segment_size, grid_in_pixel, offset + row * segment_size)
    for col in range(grid_size):
        line(col * segment_size + offset, 0, col * segment_size + offset, grid_in_pixel)

    end_shape()

    no_fill()
    stroke(30)
    stroke_weight(60)
    rect(450, 450, 900, 900)


def print_snake():
    for segment in snake:
        print(segment)


def key_pressed():
    global key
    if key in ['w', 'd', 's', 'a'] and len(snake_Head.keys_pressed) < 3:
        snake_Head.keys_pressed.append(key)
    if not snake_Head.running and key == 'ENTER':
       reset_game()


run()

