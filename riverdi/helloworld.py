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

def helloworld(gd):
    gd.ClearColorRGB(0, 60, 0)
    gd.Clear()
    gd.cmd_text(gd.w // 2, gd.h // 2, 31, eve.OPT_CENTER, "Hello world")
    gd.swap()

gd = Riverdi()
gd.panel_800x480()
helloworld(gd)
