from p5 import *
running = True

keys_pressed = []

position_head = (0,0)

direction_head = (1,0)

def set_start():
    global position_head, direction_head
    position_head = (22,22)
    direction_head = (1,0)


def move_head(snake):
    print('move head')
    global position_head, running, direction_head, keys_pressed
    if len(keys_pressed) > 0:
        key = keys_pressed.pop(0)
        turn_head(key)
    position_head = (position_head[0] + direction_head[0], position_head[1] + direction_head[1])


    if position_head[0] <= 1 or position_head[0] >= 44 or position_head[1] <= 1 or position_head[1] >= 44:
        running = False
        print("STOP")

    if position_head in snake:
        running = False
        print('AAAAAAA')

    return position_head

def turn_head(key):
    global direction_head
    #Nord
    if (key == 'w' and direction_head != (0,1)):
        direction_head = (0,-1)

    #Ost
    elif key == 'd' and direction_head != (-1,0):
        direction_head = (1,0)

    #süd
    elif key == 's' and direction_head != (0,-1):
        direction_head = (0,1)

    elif key == 'a' and direction_head != (1,0):
        direction_head = (-1,0)







