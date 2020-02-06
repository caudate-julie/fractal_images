from PIL import Image, ImageDraw
from time import time
from random import random

SIZE = 300
n = input("Enter number of points:\n> ")

ts = time()
points = []
for i in range(n):
    x = int(random()*SIZE)
    y = int(random()*SIZE)
    points.append((x, y))

neighbours = {}
for (x, y) in points:
    neighbours[(x, y)] = []
im = Image.new("RGB", (SIZE, SIZE))
draw = ImageDraw.Draw(im)
im.save("Voronoy diagram.gif")
print "time: %.4lf" % (time() - ts)
