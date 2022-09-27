
import time
import board 
import adafruit_hcsr04
import neopixel
import simpleio
distance = 0
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5
while True:
    try:
        distance = sonar.distance
        print((distance))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    if distance >= 5 and distance <= 20:
        simpleio.map_range(distance,5,20,0,255)
        dot.fill((0, 0, 255))
    else:
        dot.fill((0,255,0))
        if distance <=5 and distance >=0:
            simpleio.map_range(distance,5,0,255,0)
            dot.fill((255, 0, 0))
