
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [CircuitPython_Distance Sensor](#Distance_Sensor)
* [Onshape Unit 4](#Unit_4)
* [Onshape Swing Arm](#Swing_Arm)
* [Onshape Multi-Part Studio](#Multi-Part_Studio)

---

## Hello_CircuitPython

### Description & Code
We had to make the Neopixel on the metro board change colors.

Here's how you make code look like code:

```python
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

```


### Evidence



https://user-images.githubusercontent.com/71406907/197802759-367c34ee-6c49-40c0-af14-fa3392099f37.mp4


### Wiring


### Reflection
The two hardest parts of this assignment were, trying to import the libraries into my Virtual Studio from the library Folder and Figuring out how to onnect the NeoPixel so that the code would work on the built in NeoPixel. To fix the Import issue in VS, first you need to find the file you want to import in your library folder in CircuitP(D:). Next you want to go into the Windows(C:) in the Navigation panel in File explorer ad click on the users folder and find your username. Next click on your username and then click on the file named Virtual Studio and then click on the lib folder. Finally the last step is to copy the file you want from your circuit python lib folder, into your Virtual Studio lib folder. You'll know that it worked becasue you should see the file you wanted in the lib folder on the side panel when you're in Virtual Studio. The Next issue that I had was trying to bridge the connection between Virtual Studio and the Metro Board. The command I used was            dot = neopixel.NeoPixel(board.NEOPIXEL, 1). "dot" is a value that I set for the neopixel, board.neopixel tells th Metro board to use the built-in neopixel as the output, and the 1 is the port to use for the neopixel.




## CircuitPython_Servo

### Description & Code
I was tasked with making a servo sweep from 0 to 180 using Circuit Python. The Imports I used were Time, Board, PWMIO, and Servo.mpy. Servo.mpy allows the servo to move in two directions when you use the range function. I put the three important values for the range in the parenthesis, first the Minimum value, then the maximum value, and finally the number of degrees the servo will move each period of time.
```python

import time
import board
import pwmio
import servo

pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)


my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 10):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = 180
        time.sleep(0.08)
    for angle in range(180, 0, -10): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = 0
        time.sleep(0.08)

```

### Evidence
https://user-images.githubusercontent.com/71406907/197803297-9471980e-0907-41c7-9093-cd9c9b0be88d.mov

### Wiring
![Servo wiring](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Servo%20Wiring.jpg)

### Reflection

Overall this assignment went well, I would say the only problem that I had was that I used the wrong pin for the servo in my code. At first I read the assignmetnand it said "So when you start searching for servo code, make sure there is a PWM object, and it is attached to a PWM pin, like D2-13, not A2!" and I thought that that meant that we shouldn't use the A pins so I connected the servo to D7 and I changed the pin where A1 is in this line of code. 
```python 
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
``` 
So I ran the code and the servo didnt move and so I was confused becasue it said to not use the A pins. After like 10 minutes of trying to figure out what was wrong, I went back and read the instructions again and I realized that it said to just not use the A2 pin, so I swapped the pin on the board and changed the code and it worked.

## CircuitPython_LCD

### Description & Code
I was tasked with making an LCD screen show a counter and wire to inputs to the lcd screen so that when one input is pressed the variable counts up and if the other input is pressed, the variable would count down. The two inputs that I used were push buttons.

```python
# Credit to Jack H. and Robel G. for the code
import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object
i2c = board.I2C()
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
cur_state = True
prev_state = True
cur_state2 = True
prev_state2 = True
buttonPress = 0

while True:
    while btn2.value == False:
        lcd.set_cursor_pos(1,0)
        lcd.print("UP  ")
        cur_state = btn.value
        if cur_state != prev_state:
            if not cur_state:
                buttonPress = buttonPress + 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state = cur_state
    else:
        lcd.set_cursor_pos(1,0)
        lcd.print("DOWN")
        cur_state2 = btn.value
        if cur_state2 != prev_state2:
            if not cur_state2:
                buttonPress = buttonPress - 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state2 = cur_state2

```

### Evidence and Wiring


https://user-images.githubusercontent.com/71406907/197800787-38db0131-d6d9-48df-8e73-7363c4fc47f9.mp4





### Reflection
Overall this assignment was really hard because I had to try and figure out how to not only make an lcd work, I also had to figure out how a button works in circuit python. I kept running into trouble when I was trying to get the buttons to work because only one button would work and then when I tried to program the other button, it would break the lcd screen and cause it to flash the text.




## Distance Sensor

### Description & Code
I was tasked with making an ultrasonic sensor read the distance from an object and change colors when certain distances are reached.

```python
import time
#Credit to Kattni Rembor for the Adafruit Tutorial code for the ultrasonic sensor

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

```

### Evidence and Wiring

### Reflection
Overall, this assignment wasn't that difficult, the only difficult part was trying to get the green color to match up with the values. I fixed the missing color by adding this else, ```python
else:
        dot.fill((0,255,0))
       ``` this made every other value over 20 make the neopixel turn green.




## Unit_4

### Description

### CAD

### Reflection


## Swing Arm

### Description

### CAD

### Reflection


## Multi-Part Studio

### Description

### CAD

### Reflection
