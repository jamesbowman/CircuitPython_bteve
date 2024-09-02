import random
import board
import bteve as eve

class Riverdi(eve.EVE):
    def __init__(self):
        self.setup_spi(
            sck  = board.GP10,
            mosi = board.GP11,
            miso = board.GP12,
            cs   = board.GP9,
            pd   = board.GP8
        )


rr = random.randrange

gd = Riverdi()
gd.panel_800x480()

while True:
    gd.VertexFormat(2)
    gd.Clear()
    gd.Begin(eve.POINTS)
    for i in range(100):
        gd.ColorRGB(rr(256), rr(256), rr(256))
        gd.PointSize(rr(gd.w // 6))
        gd.Vertex2f(rr(gd.w), rr(gd.h))
    gd.swap()
