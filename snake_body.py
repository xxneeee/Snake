from p5 import *

def move_body(snake, richtung, wachsen):
    #head
    head=snake[0]
    new_head=head
    x= 0
    y= 1
    if richtung == "Nord":
        new_head=(head[x], head[y] -1)
        print('Norden')
    elif richtung == "Süd":
        new_head=(head[x], head[y] +1)
        print('Süd')
    elif richtung == "West":
        new_head=(head[x]-1, head[y])
        print('West')
    elif richtung == "Ost":
        new_head=(head[x]+1, head[y])
        print('Ost')
    else:
        print('error')

    snake.insert(0, new_head)

    #tail
    if wachsen ==False:
        snake.pop()
    return snake