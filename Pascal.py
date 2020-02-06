from PIL import Image
from time import time

SIZE = 125

def Color((x, y)):
    if x == 0 or y == 0:
        return 255
    return ((im.getpixel((x-1, y))+im.getpixel((x, y-1)))%2)*255

ts = time()
im = Image.new("L", (SIZE, SIZE))
for p in ((x, y) for x in range(SIZE) for y in range(SIZE)):
    im.putpixel(p, Color(p))

im.save("Pascal.gif")
print "time: %.4lf" % (time() - ts)
