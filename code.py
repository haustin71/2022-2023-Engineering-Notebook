
import time
import board 
import adafruit_hcsr04
import neopixel
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5
distance = sonar.distance
while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    if sonar.distance < 5:
     dot.fill((255, 0, 0))