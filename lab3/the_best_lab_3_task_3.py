from graph import *
import math as m


# ________________________________________________________

# Sun Function

def sun(x_0, y_0, r):
    """(x_0, y_0) - coordinates of centre of the sun, r - radius of the sun, function returns list of reference to sun
    object and (x_0, y_0)"""
    penColor("yellow")
    brushColor("Yellow")
    x = []
    y = []
    x.append(x_0)
    y.append(y_0 + r + 5)
    phi = 0
    for i in range(1, 40, 1):
        phi += 2 * m.pi / 40
        if i % 2 != 0:
            x.append(x[0] - r * m.sin(phi))
            y.append(60 + r * m.cos(phi))
        else:
            x.append(x[0] - (r + 5) * m.sin(phi))
            y.append(60 + (r + 5) * m.cos(phi))
    points = [(i, j) for i, j in zip(x, y)]
    return [polygon(points), x_0, y_0]


# ________________________________________________________

# Cloud Function

def cloud(x, y, r):
    """(x, y) - coordinates of the left circle, r - radius of circles, function returns list of list of references to
    all circles and coordinate of right circle"""
    penSize(1)
    brushColor("white")
    penColor("White")
    cloud_circle = []
    for i in range(4):
        cloud_circle.append(circle(x + (i) * r, y, r))
    cloud_circle.append(circle(x - r / 2 + 1.5 * r, y - r, r))
    cloud_circle.append(circle(x + r / 2 + 1.5 * r, y - r, r))
    return [cloud_circle, x + 3 * r]


# ________________________________________________________

# House Function

def house(x1, y1, x2, y2):
    """(x1, y1) - coordinates of left top angle of the main rectangle, (x2, y2) - right bottom angle"""
    brushColor("#8B6914")
    penColor("black")
    rectangle(x1, y1, x2, y2)
    brushColor("#1E90FF")
    penColor("black")
    rectangle(x1 + 0.34 * (y2 - y1), y1 + 0.23 * (y2 - y1), x2 - 0.34 * (y2 - y1), y2 - 0.38 * (y2 - y1))
    brushColor("#FF1E55")
    polygon([[x1, y1], [(x1 + x2) / 2, y1 - (y2 - y1) / 2], [x2, y1]])


# ________________________________________________________

# Tree Function

def tree(x, y, h, r):
    """(x, y) - coordinates of top of the tree trunk, h - size of tree trunk, r - radius of the circle of the leaves"""
    penColor("Black")
    penSize(r * 7 / 8)
    line(x, y, x, y * h)
    penSize(1)
    brushColor("#225D15")
    circle(x, y - 3 * r, r)
    circle(x - r, y - 2 * r, r)
    circle(x + r, y - 2 * r, r)
    circle(x, y - r, r)
    circle(x - r, y - r / 6, r)
    circle(x + r, y, r)


# ________________________________________________________
# ________________________________________________________

# MAIN

penSize(1)
windowSize(1000, 500)
canvasSize(1000, 500)

# Drawing sky
penColor("deep sky blue")
brushColor("deep sky blue")
sky = rectangle(0, 0, 1000, 250)

# Drawing sun
Sun = [sun(60, 60, 30)]

# Drawing grass
penColor("green")
brushColor("green")
rectangle(0, 250, 1000, 500)

# Drawing clouds
clouds = [cloud(800, 100, 30), cloud(150, 80, 30), cloud(450, 120, 20)]

# Drawing houses
house(175, 220, 325, 350)
house(650, 220, 750, 300)

# Drawing trees
tree(400, 240, 1.5, 30)
tree(800, 220, 1.32, 20)


# Animating clouds
def moveClouds_left():
    """clouds - list of the all clouds, clouds[i][1] - x coordinate of the left circle of each cloud, cloud[i][0][j] -
    reference to each circle in the cloud"""
    global clouds
    for i in range(3):
        if clouds[i][1] < -50:
            dx = 1200
            clouds[i][1] += dx
        else:
            dx = -5
            clouds[i][1] += dx
        for j in range(6):
            moveObjectBy(clouds[i][0][j], dx, 0)


# Animating Sun
direction = ""
x = Sun[0][1]
y = Sun[0][2]


def move_Sun():
    global Sun
    global x, y
    # x, y - coordinates of the centre of the Sun
    dx = -3
    dy = 0
    if x < -40:
        dx = 1070
    global direction
    if y <= 60:
        direction = "Down"
    if y >= 440:
        direction = "Up"
    if direction == "Down":
        dy = 2
    if direction == "Up":
        dy = -2
    # Change color of the sky:
    color = ""
    if y > 350:
        color = "midnight blue"
    elif y > 290:
        color = "RoyalBlue4"
    elif y > 240:
        color = "RoyalBlue3"
    elif y > 190:
        color = "RoyalBlue2"
    else:
        color = "deep sky blue"
    changeFillColor(sky, color)
    # move Sun
    moveObjectBy(Sun[0][0], dx, dy)
    x += dx
    y += dy


def move():
    move_Sun()
    moveClouds_left()


# Move
onTimer(move, 50)

run()
