
"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from freegames import vector
import turtle
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    pass  # TODO

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    forward(end.x - start.x)
    left(90)
    forward(end.x - start.x)
    forward(end.x - start.x)
    left(90)
    forward(end.x - start.x)
    left(90)
    forward(end.x - start.x)
    forward(end.x - start.x)
    left(90)
    
    end_fill()
    
    pass  # TODO

# este es el comentario de Andres
# este es el comentario de Edgar

def triangle(start, end):
    "Draw triangle from start to end."
    import turtle
    
    raya=turtle.Turtle()
    
    def triangulo(x,y):
        raya.penup()
        raya.goto(x, y)
        raya.pendown()
        
        for i in range(3):
            raya.forward(100)
            raya.left(120)
            raya.forward(100)
    
        
        
    turtle.onscreenclick(triangulo,1)
    turtle.listen()
    turtle.done()
    
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()