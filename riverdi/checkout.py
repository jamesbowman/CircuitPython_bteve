import time
import struct
import bteve as eve
import riverdi


def checkout(gd):
    print(f"Using bteve version {eve.__version__}")

    gd.cmd_testcard()
    gd.flush()

    f0 = gd.rd32(eve.REG_FRAMES)
    c0 = gd.rd32(eve.REG_CLOCK)
    time.sleep(1)
    f1 = gd.rd32(eve.REG_FRAMES)
    c1 = gd.rd32(eve.REG_CLOCK)

    print(f"System clock   {(c1 - c0) / 1e6:.0f} MHz")
    print(f"Frame rate     {f1 - f0} Hz")

    while 0:
        (sy,sx) = struct.unpack("HH", gd.rd(eve.REG_TOUCH_SCREEN_XY, 4))
        print(sx, sy)

riverdi.run(checkout)
