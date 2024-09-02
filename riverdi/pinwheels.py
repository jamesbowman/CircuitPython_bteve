import board
import math
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

def pinwheels(gd):
    def wheel(i, r, npoints):
        r = r * gd.h / 480
        step = 2 * math.pi * 17 / npoints
        theta = i / r
        gd.Begin(eve.LINE_STRIP)
        for i in range(npoints + 1):
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            gd.Vertex2f(x, y)
            theta += step
    print("Frequency", gd.rd32(eve.REG_FREQUENCY))
    for i in range(9999999):
        gd.Clear()
        gd.LineWidth(1.25)
        gd.VertexTranslateX(gd.w // 2)
        gd.VertexTranslateY(gd.h // 2)

        gd.ColorRGB(0xc0, 0xff, 0xc0)
        wheel(i, 30, 30)
        gd.ColorRGB(0xff, 0xff, 0xc0)
        wheel(i, 48, 20)
        gd.ColorRGB(0xff, 0xc0, 0xc0)
        wheel(i, 110, 13)
        gd.ColorRGB(0xc0, 0xc0, 0xff)
        wheel(i, 230, 52)
        gd.swap()

gd = Riverdi()
gd.panel_800x480()
pinwheels(gd)
