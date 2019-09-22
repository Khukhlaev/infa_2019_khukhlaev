from graph import *
import math as m
from typing import Any

penSize(1)
windowSize(1000, 500)
canvasSize(1000, 500)
penColor("#279710")
brushColor("#279710")
rectangle(0, 250, 1000, 500)
brushColor("#17E0B5")
rectangle(0, 0, 1000, 250)
brushColor("#8B6914")
penColor("black")
rectangle(175, 220, 175 + 150, 220 + 130)
brushColor("#1E90FF")
penColor("#FF671E")
rectangle(250 - 30, 250, 250 + 30, 250 + 50)
penColor("black")
brushColor("#FF1E55")
polygon([[175, 220], [250, 150], [175 + 150, 220]])
penSize(25)
line(750, 240, 750, 350)
penSize(1)
brushColor("#225D15")
circle(750, 120 + 30, 30)
circle(720, 150 + 30, 30)
circle(780, 150 + 30, 30)
circle(750, 180 + 30, 30)
circle(720, 205 + 30, 30)
circle(780, 210 + 30, 30)
brushColor("white")
for i in range(4):
    circle(500 + (i) * 35, 100, 30)
circle(535, 100 - 27, 30)
circle(570, 100 - 27, 30)
brushColor("#ffc0cb")
x = []
y = []
x.append(850)
y.append(90 + 35)
phi = 0
r = 30
for i in range(1, 40, 1):
    phi += 2 * m.pi / 40
    if i % 2 != 0:
        x.append(x[0] - r * m.sin(phi))
        y.append(90 + r * m.cos(phi))
    else:
        x.append(x[0] - (r + 5) * m.sin(phi))
        y.append(90 + (r + 5) * m.cos(phi))
points = [(i, j) for i, j in zip(x, y)]
polygon(points)

run()
