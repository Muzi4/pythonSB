import random
import turtle as t

t.shape('turtle')
t.pensize(10)
t.speed(3)

def drawCircle(x, y):
    t.penup()
    t.pencolor('blue')
    t.goto(x, y)
    t.pendown()
    t.circle(50)

def randomDrawCircle(x, y):
    # rX = random.randrange(1, 200)
    # rY = random.randrange(1, 200)
    # print('x = ', rX, 'y = ', rY)
    t.color('red')
    for i in range(0,50):
        rX = random.randrange(-600, 600)
        rY = random.randrange(-600, 600)
        t.penup()
        t.goto(rX, rY)
        t.pendown()
        t.circle(50)
        if (-sWidth / 2 <= rX and rX <= sWidth / 2) and (-sHeight / 2 <= rY and rY <= sHeight / 2):
            pass
        else:
            t.penup()
            t.goto(0, 0)
            t.color('blue')
            t.pendown()

# t.onscreenclick(drawCircle, 1)
t.onscreenclick(randomDrawCircle, 1)

t.done()