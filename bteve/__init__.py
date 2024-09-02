__version__ = '0.1.5'

import busio
import digitalio

from .registers import *
from .eve import BaseEVE, align4, MoviePlayer

def spilock(f):
    def wrapper(*args, **kwargs):
        spi = args[0].sp
        while not spi.try_lock():
            pass
        r = f(*args, **kwargs)
        spi.unlock()
        return r
    return wrapper

def pin(p):
    r = digitalio.DigitalInOut(p)
    r.direction = digitalio.Direction.OUTPUT
    r.value = True
    return r

class EVE(BaseEVE):
    """ Drives a BaseEVE using CircuitPython: RP2040, ESP-32 etc. """

    def setup_spi(self, *, sck, mosi, miso, cs, pd, speed = 6_000_000):
        self.cs = pin(cs)
        self.sp = busio.SPI(sck, mosi, miso)
        self.pd = pin(pd)

        self.configure_spi(speed)
        self.boot()

    @spilock
    def configure_spi(self, speed):
        self.sp.configure(baudrate = speed, phase=0, polarity=0)

    @spilock
    def transfer(self, wr, rd = 0):
        self.cs.value = False
        self.sp.write(wr)
        r = None
        if rd != 0:
            r = bytearray(rd)
            self.sp.readinto(r)
        self.cs.value = True
        return r
