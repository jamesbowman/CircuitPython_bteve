import random
import math
import bteve as eve

def helloworld(gd):
    gd.ClearColorRGB(0, 60, 0)
    gd.Clear()
    gd.cmd_text(gd.w // 2, gd.h // 2, 31, eve.OPT_CENTER, "Hello world")
    gd.swap()

def fizz(gd):
  rr = random.randrange
  while True:
      gd.VertexFormat(2)
      gd.Clear()
      gd.Begin(eve.POINTS)
      for i in range(100):
          gd.ColorRGB(rr(256), rr(256), rr(256))
          gd.PointSize(rr(gd.w // 6))
          gd.Vertex2f(rr(gd.w), rr(gd.h))
      gd.swap()

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

def testcard(gd):
    gd.cmd_testcard()
    gd.finish()
