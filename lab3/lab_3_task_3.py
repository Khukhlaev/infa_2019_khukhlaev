from graph import *
import math as m
from typing import Any

#def clouds (first_x, first_y, radius):

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

brushColor("#8B6914")
penColor("black")
rectangle(650, 220, 650 + 100, 220 + 80)
brushColor("#1E90FF")
penColor("#FF671E")
rectangle(700 - 18, 240, 700 + 18, 240 + 30)
penColor("black")
brushColor("#FF1E55")
polygon([[650, 220], [700, 180], [650 + 100, 220]])

penSize(25)
line(400, 240, 400, 350)

penSize(12)
line(800, 220, 800, 220 + 70)

penSize(1)
brushColor("#225D15")
circle(400, 120 + 30, 30)
circle(370, 150 + 30, 30)
circle(430, 150 + 30, 30)
circle(400, 180 + 30, 30)
circle(370, 205 + 30, 30)
circle(430, 210 + 30, 30)

circle(800, 160 + 20, 20)
circle(780, 180 + 20, 20)
circle(820, 180 + 20, 20)
circle(800, 200 + 20, 20)
circle(780, 217 + 20, 20)
circle(820, 220 + 20, 20)

brushColor("white")
for i in range(4):
    circle(800 + (i) * 35, 100, 30)
circle(785 + 50, 100 - 27, 30)
circle(820 + 50, 100 - 27, 30)

for i in range(4):
    circle(150 + (i) * 35, 80, 30)
circle(135 + 50, 80 - 27, 30)
circle(170 + 50, 80 - 27, 30)

for i in range(4):
    circle(450  +50 + (i) * 25, 120, 20)
circle(440 + 50 + 30, 120 - 17, 20)
circle(470 + 50 + 30, 120 - 17, 20)

brushColor("#ffc0cb")
x = []
y = []
x.append(60)
y.append(60 + 35)
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

run()
