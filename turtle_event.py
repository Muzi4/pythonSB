import turtle
import random

def screenLeftClick(x, y):
    global r, g, b
    global pSize

    r = random.random()
    g = random.random()
    b = random.random()
    pSize = random.randrange(1,10)

    turtle.shapesize(pSize)
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x, y)

pSize = 10
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이 그림그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick,1)


turtle.done()