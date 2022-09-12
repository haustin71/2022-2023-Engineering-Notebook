
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it Blue!")

while True:
    dot.fill((255, 0, 0))
    time.sleep(1.0)
    dot.fill((0, 255, 0))
    time.sleep(1.0)
    dot.fill((0, 0, 255))
    time.sleep(1.0)
   