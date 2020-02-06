# -*- coding: windows-1251 -*-

from PIL import Image, ImageDraw
from time import time
from math import sin, cos
from cmath import pi

SIZE = 300
ITER = 10
BOTTOM = 10
X_SIZE = SIZE
Y_SIZE = int(SIZE*0.8)
LEN = SIZE/4.5

def GetLine((x, y), length, a):
    return ((x, y),(x+cos(a)*length, y+sin(a)*length))

def DrawBranch((p, a), c=255):
    for delta in (-pi/5, pi/7):
        q, r = GetLine(p, LEN, a+delta)
        draw.line((q, r), c)
        branches.append((r, a+delta))
    return

ts = time()
im = Image.new("L", (X_SIZE, Y_SIZE), 10)
draw = ImageDraw.Draw(im)

x_a, y_a, x_b, y_b = float(X_SIZE/2), float(Y_SIZE - BOTTOM), \
                     float(X_SIZE/2), float(Y_SIZE - BOTTOM - LEN)
draw.line(((x_a, y_a), (x_b, y_b)), 255)
branches = [((x_b, y_b), -pi/2)]

for i in range(ITER):
    LEN *= 0.7
    for j in range(len(branches)):
        DrawBranch(branches.pop(0));

im.save("Shred tree.gif")
print "time: %.4lf" % (time() - ts)
