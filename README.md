
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
I was tasked with making the Neopixel on the adafruit metro board change colors.


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


### Evidence & Wiring
The Video for my neopixel got deleted and so I don't currently have a video of my neopixel flashing, but here is a image of where the built in neopixel is


![Neopixel](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Neopixel.PNG)



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
https://user-images.githubusercontent.com/71406907/197802759-367c34ee-6c49-40c0-af14-fa3392099f37.mp4
### Reflection
Overall, this assignment wasn't that difficult, the only difficult part was trying to get the green color to match up with the values. I fixed the missing color by adding this else, ```python
else:
        dot.fill((0,255,0))
       ``` this made every other value over 20 make the neopixel turn green.




## Unit_4

### Description
This Assignment was Broken into 4 Parts and was split between myself and my partner Grant. Each Partner was tasked with creating two parts each and at the end we would put all of our parts in an asssembly and see if they matched up. I was tasked with making the Spinner and the Prop for the Pull Copter.
### CAD

![Spinner](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Spinner.PNG)
![Prop](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Prop.PNG)
![Assembly 1](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Assembly%201.PNG)
![Assembly 2](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Assembly%202.PNG)
[Grant and Holden Onshape Document](https://cvilleschools.onshape.com/documents/17cfa26e36de454af07126e5/w/881d18355baad003fe7f630b/e/dea2b9ea183a5f7648c690ea?renderMode=0&uiState=6359c85a21769a153df12894)
### Reflection
Overall, this assignment was pretty easy, even though I got the hard part. I think that the instructions were very clear and detailed and I also think that It served as a good refresher for going back into Onshape. From this assignment I learned some of the usefull shortcuts and I also learned how to correctly use the helix feature and I learned how to animate an assembly. 

## Swing Arm

### Description
I was tasked with making a swing arm going off of the drawings that were given on the document. This Assignment is practice for when we take the Onshape certification exam. I was given two steps of instructions and each instruction changed 3 different variables.
### CAD
![Part 1](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Swing%20Arm%201.PNG)
![Part 2](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Swing%20Arm%202.PNG)
![Part 3](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Swing%20Arm%20step%202.PNG)
![Part 4](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Swing%20Arm%20step%203.PNG)
[Holden A Swing Arm Onshape Document](https://cvilleschools.onshape.com/documents/3d028f81ae540185a3d04085/w/7465647970d0ff93aa4679b3/e/d53119136accd6e31c6e04b0?renderMode=0&uiState=6359cdee38fff70f91ddb090)
### Reflection
This Assignment was harder than the previous assignment. I had the most trouble trying to figure out how to create the curved shape in the middle. From this assignment, I learned how to look at different drawings and recreate the part using the given values. I also learned that its a lot easier sometimes to use constraints firt instead of going straight into dimensioning.

## Multi-Part Studio

### Description
This Assignment was very similar to the Swing Arm because I was tasked with designing multiple parts from the drawings that were given in the document. Instead of just making one part, we had to make multiple parts in the same studio.
### CAD
This is the Cylinder Assembly for question 1
![Q1](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Multi-part%201.PNG)
![Q1.1](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Multi-part%202.PNG)

This is the Cylinder Assembly for question 2

![Q2](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Multi-part%203.PNG)

This is the Cylinder Assembly for questions 3 and 4

![Q3&4](https://raw.githubusercontent.com/haustin71/Circuit-Python/master/Multi-part%204.PNG)

[Holden A Multi-Part Studio Document](https://cvilleschools.onshape.com/documents/cc8d8824d0cb3cc32b86f00c/w/83e26c2c310fc5a85afd3479/e/99d8d6019cf8e8d9a5570a31?renderMode=0&uiState=6359d2b7b7948a2d7b607883)
### Reflection
Overall I enjoyed this asignment because it was really good practice for the Onshape Certification Test. I didn't have much trouble when I was creating the parts, the only two problems that I had were, creating the revolve cut around the ring on the top cap and trying to get the weight to be exact. To create the correct revolve cut, I needed to switch the plane of the sketch so that it was on the top cap instead of above the top cap. Once I did that, I could then revolve the ring with the cut around the hole where the plunger went. As for the weight, I went back and checked all of my changed measurements for the questions and I realised that I forgot to change 1 or 2 dimesions which slightly changed the weight. From completing this assignment, I learned how to better read drawings and find the connection between them.
