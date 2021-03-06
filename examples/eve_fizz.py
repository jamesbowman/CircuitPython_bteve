import sys
import random
import bteve as eve

rr = random.randrange

gd = eve.Gameduino()
gd.init()

while True:
    gd.Clear()
    gd.VertexFormat(0)
    gd.Begin(eve.POINTS)
    for i in range(200):
        gd.ColorRGB(rr(256), rr(256), rr(256))
        gd.PointSize(rr(gd.w // 6))
        gd.Vertex2f(rr(gd.w), rr(gd.h))
    gd.swap()
