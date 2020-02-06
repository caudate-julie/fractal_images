from PIL import Image, ImageDraw
from time import time

SIZE = 500
ITER = 10
BOTTOM = 30
X_SIZE = SIZE
Y_SIZE = int(SIZE*0.6)

catheta = [tuple((float(X_SIZE/2 + i*X_SIZE/16), float(Y_SIZE-BOTTOM))
                 for i in (-1, 1))]
hypotenuses = []

def DrawQuadr(((x1, y1), (x2, y2)), c=255):
    for i in range(3):
        v2, v1 = -(x2 - x1), (y2 - y1)
        x1, y1 = x2, y2
        x2, y2 = x2+v1, y2+v2
        draw.line(((x1, y1), (x2, y2)), c)
        if i == 1:
            hypotenuses.append(((x1, y1), (x2, y2)))
    return

def DrawTrian(((x1, y1), (x2, y2)), c=255):
    v1, v2 = (x2 - x1)/2, (y2 - y1)/2
    q = (x1 + v1 - v2, y1 + v2 + v1)
    draw.line(((x2, y2), q), c)
    catheta.append(((x2, y2), q))
    draw.line((q, (x1, y1)), c)
    catheta.append((q, (x1, y1)))
    return

ts = time()
im = Image.new("L", (X_SIZE, Y_SIZE), 10)
draw = ImageDraw.Draw(im)

draw.line(catheta[0], 255)
for i in range(ITER):
    for j in range(len(catheta)):
        q = catheta.pop(0)
        DrawQuadr(q)
    for j in range(len(hypotenuses)):
        q = hypotenuses.pop(0)
        DrawTrian(q)

im.save("Pythagorean tree.gif")
print "time: %.4lf" % (time() - ts)
