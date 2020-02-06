from PIL import Image, ImageDraw
from time import time
from string import replace

SIZE = 700
ITER = 15
L = 5

def p(x):
    return x + SIZE/2

#ITER = input("Number of iterations: ")
ts = time()
im = Image.new("L", (SIZE, SIZE), 10)
draw = ImageDraw.Draw(im)

def newline((u, v),(w, t), clr):
    for z in (u, v, w, t):
        if z<0 or z>=SIZE:
            return
    draw.line(((u, v),(w, t)), clr)
    return

for u, v, clr in ((L, 0, 255), (0, L, 100), (-L, 0, 200), (0, -L, 50)):
    x, y = 0, 0
    s = "L"
    for i in range(ITER):
        s1 = replace(s, 'R', 'S')
        s1 = replace(s1, 'L', 'R')
        s1 = replace(s1, 'S', 'L')
        s1 = s1[::-1]
        s = s + 'L' + s1
    for c in s:
        newline((p(x), p(y)), (p(x+u), p(y+v)), clr)
        x, y = x+u, y+v
        if c == "L":
            u, v = -v, u
        else:
            u, v = v, -u

im.save("Dragon.gif")
print "time: %.4lf" % (time() - ts)
