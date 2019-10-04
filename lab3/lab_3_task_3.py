
from graph import *
import math as m
from typing import Any


#________________________________________________________

# Sun Function

def sun(h, v):
    penColor("yellow")
    brushColor("Yellow")
    x = []
    y = []
    x.append(h)
    y.append(v)
    phi = 0
    r = 30
    for i in range(1, 40, 1):
        phi += 2 * m.pi / 40
        if i % 2 != 0:
            x.append(x[0] - r * m.sin(phi))
            y.append(60 + r * m.cos(phi))
        else:
            x.append(x[0] - (r + 5) * m.sin(phi))
            y.append(60 + (r + 5) * m.cos(phi))
    points = [(i, j) for i, j in zip(x, y)]
    polygon(points)

#________________________________________________________

# Cloud Function

def cloud(x, y, r):
    penSize(1)
    brushColor("white")
    penColor("White")
    for i in range(4):
        circle(x + (i) * r, y, r)
    circle(x-r/2 + 1.5*r, y - r, r)
    circle(x+r/2 + 1.5*r, y - r, r)

#________________________________________________________

# House Function

def house(x1, y1, x2, y2):
    brushColor("#8B6914")
    penColor("black")
    rectangle(x1, y1, x2, y2)
    brushColor("#1E90FF")
    penColor("black")
    rectangle(x1+0.34*(y2-y1), y1+0.23*(y2-y1), x2-0.34*(y2-y1), y2-0.38*(y2-y1))
    brushColor("#FF1E55")
    polygon([[x1, y1], [(x1+x2)/2, y1-(y2-y1)/2], [x2, y1]])

#________________________________________________________

# Tree Function

def tree(x, y, h, r):
    penColor("Black")
    penSize(r*7/8)
    line(x, y, x, y*h)
    penSize(1)
    brushColor("#225D15")
    circle(x, y-3*r, r)
    circle(x-r, y-2*r, r)
    circle(x+r, y-2*r, r)
    circle(x, y-r, r)
    circle(x - r, y-r/6, r)
    circle(x + r, y, r)

#________________________________________________________
#________________________________________________________

# MAIN

penSize(1)
windowSize(1000, 500)
canvasSize(1000, 500)

# Drawing sky
penColor("#279710")
brushColor("#279710")
rectangle(0, 250, 1000, 500)

# Drawing grass
penColor("#17E0B5")
brushColor("#17E0B5")
rectangle(0, 0, 1000, 250)

# Drawing sun
sun(60, 95)

# Drawing clouds
cloud(800, 100, 30)
cloud(150, 80, 30)
cloud(450, 120, 20)

# Drawing houses
house(175, 220, 325, 350)
house(650, 220, 750, 300)

# Drawing trees
tree(400, 240, 1.5, 30)
tree(800, 220, 1.32, 20)

# Animating clouds

k = 800

def moveleft():
    global k
    k = k - 5
    if k < -100:
        k = 2000
        for i in range(18):
            moveObjectBy(i+4, 2000, 0)
    for i in range(18):
        moveObjectBy(i+4, -5, 0)

onTimer(moveleft, 50)

# ToDo

run()
