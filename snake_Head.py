from p5 import *
running = True

keys_blocked = False

position_head = (0,0)

direction_head = (1,0)

def set_start():
    global position_head, direction_head
    position_head = (22,22)
    direction_head = (1,0)


def move_head():
    print('move head')
    global position_head, running, direction_head, keys_blocked
    position_head = (position_head[0] + direction_head[0], position_head[1] + direction_head[1])
    keys_blocked = False

    if position_head[0] <= 1 or position_head[0] >= 44 or position_head[1] <= 1 or position_head[1] >= 44:
        running = False
        print("STOP")

    return position_head

def key_pressed():
    global key,direction_head,keys_blocked
    if keys_blocked:
        return
    #Nord
    if (key == 'w' and direction_head != (0,1)):
        direction_head = (0,-1)
        keys_blocked = True
    #Ost
    elif key == 'd' and direction_head != (-1,0):
        direction_head = (1,0)
        keys_blocked = True
    #süd
    elif key == 's' and direction_head != (0,-1):
        direction_head = (0,1)
        keys_blocked = True
    elif key == 'a' and direction_head != (1,0):
        direction_head = (-1,0)
        keys_blocked = True
