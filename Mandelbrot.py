from PIL import Image
from time import time

SIZE = 300
ITER = 50
SCL = 20

def Color((x, y)):
    x = float(x-SIZE)/SIZE*2
    y = float(y-SIZE/2)/SIZE*2
    zx = zy = 0.0
    for i in range(ITER):
        zx, zy = zx**2 - zy**2 + x, 2*zx*zy + y
        if zx**2 + zy**2 > 4:
            return (i*SCL, 0, 0)
    return (0, 0, 0)

ts = time()
im = Image.new("RGB", (int(SIZE*1.5), SIZE))
for p in ((x, y) for x in range(int(SIZE*1.5)) for y in range(SIZE)):
    im.putpixel(p, Color(p))
im.save("Mandelbrot.gif")
print "time: %.4lf" % (time() - ts)
