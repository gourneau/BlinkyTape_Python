"""Simple animation example using BlinkyTape.py"""

from BlinkyTape import BlinkyTape
from time import sleep
import optparse
import itertools

import webcolors
from colour import Color

red = Color("#ff0000")
yellow = Color("#ffff00")
green = Color("#00ff00")
colors1 = red.range_to(yellow,10)
colors2 = yellow.range_to(green,10)
dead = 20
bc = [Color("#000000")] * dead

f = []
for c in itertools.chain(bc,colors1,colors2, bc):
    w = webcolors.hex_to_rgb(c.get_hex())
    f.append((w.red, w.green, w.blue))

parser = optparse.OptionParser()
parser.add_option("-p", "--port", dest="portname",
                  help="serial port (ex: /dev/ttyUSB0)", default=None)
parser.add_option("-c", "--count", dest="ledcount",
                  help="LED count", default=60, type=int)
parser.add_option("-s", "--size", dest="size",
                  help="Size of the light wave", default=60, type=int)
(options, args) = parser.parse_args()

if options.portname is not None:
    port = options.portname
else:
    print("Usage: python scanline.py -p <port name>")
    print("(ex.: python scanline.py -p /dev/ttypACM0)")
    exit()

blinky = BlinkyTape(port, options.ledcount)

while True:
    for position in range(options.ledcount):
        print(position)
        for led in range(options.ledcount):
            if position < led:
                blinky.sendPixel(0,0,0)
            else:
                print(led)
                print(f[led])
                blinky.sendPixel(*f[led])

        blinky.show()
        if position < dead or position > (options.ledcount - dead):
            pass
        else:
            sleep(.2)
