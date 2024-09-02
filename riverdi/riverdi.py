import board
import bteve as eve
import examples

class Riverdi(eve.EVE):
    def __init__(self):
        self.setup_spi(
            sck  = board.GP10,
            mosi = board.GP11,
            miso = board.GP12,
            cs   = board.GP9,
            pd   = board.GP8
        )

gd = Riverdi()
gd.panel_800x480()

examples.testcard(gd)
