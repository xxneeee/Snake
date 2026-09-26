from p5 import *

def move_body(snake, new_head, wachsen):
    #head
    snake.insert(0, new_head)

    #tail
    if wachsen ==False:
        snake.pop()
    return snake