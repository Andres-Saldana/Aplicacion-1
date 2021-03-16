
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
#<<<<<<< HEAD
    
#=======

    # aqui vamos a dibujar un rectangulo asi que 2 de sus lados deben ser mas grandes que los otros 2

    forward(end.x - start.x) #dibujamos el primer lado
    left(90) #damos un giro de 90 grados
    forward(end.x - start.x) #recorremos el doble para dibujar otro lado
#>>>>>>> 4d548f29d36927ea96074750b991d30c6dd908a3
    forward(end.x - start.x)
    left(90) # otro giro de 90
    forward(end.x - start.x) # se repite el proceso para terminar el rectangulo
    left(90)
    forward(end.x - start.x)
    forward(end.x - start.x)
    left(90)
    
    end_fill()
    
    pass  # TODO

# este es el comentario de Andres
# este es el comentario de Edgar

def triangle(x, y):
    "Draw triangle from start to end."
    import turtle
    raya=turtle.Turtle() #objeto
    raya.begin_fill()
    
    def triangulo(x,y): #Funcion para el trazo

        raya.penup()
        raya.goto(x, y)
        raya.pendown()

        for i in range(3): #realiza el trazo
            raya.forward(100) #distancia en x
            raya.left(120) #angulos que gira (120°)
            raya.forward(100) # continúa el trazo
            #se repite para terminar el triángulo
    
    turtle.onscreenclick(triangulo,1) #que de un trazo lo realize
    turtle.listen()
    raya.end_fill()
    turtle.done() #mantener el trazo
    
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