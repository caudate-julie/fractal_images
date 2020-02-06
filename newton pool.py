from PIL import Image
from time import time

SIZE = 300
ITER = 50

def p(x):
    return float(x)/SIZE*2 -1

def f_0(x):
    return x**5 - 1
def f_1(x):
    return 4*x**4

def z_next(z):
    if z == 0:
        return 0
    return z - f_0(z)/f_1(z)
ts = time()

im = Image.new("RGB", (SIZE, SIZE))
for x, y in ((a, b) for a in range(SIZE) for b in range(SIZE)):
    z = complex(p(x), p(y))
    for i in range(ITER):
        z = z_next(z)
    color = (z.real*255, (z.real+z.imag)/2*255, z.imag*255)
    im.putpixel((x, y), color)

im.save("newton pool.gif")
print "time: %.4f" % (time() - ts)
