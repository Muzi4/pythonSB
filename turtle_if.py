import turtle as t
import random

t.shape('turtle')
t.pensize(1)
t.speed(10)

for i in range(0, 100, 1):
    r = random.random()
    g = random.random()
    b = random.random()

    t.circle(i)
    t.pencolor((r, g, b))

t.done()