import random
import turtle


def screenLeftClick(x,y):
    tsize = random.randrange(2,10)
    turtle.shapesize(tsize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r, g, b))
    tAngle = random.randrange(0, 360)

    turtle.penup()
    turtle.goto(x,y)
    turtle.left(tAngle)
    turtle.stamp()

tSize, tAngle = 0, 0
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이 도장 찍기')
turtle.shape('turtle')

turtle.onscreenclick(screenLeftClick,1)

turtle.done()