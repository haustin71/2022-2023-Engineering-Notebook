
from unittest.mock import MagicProxy
import board
import time
from analogio import AnalogIn
import pwmio
from adafruit_motorkit import MotorKit
kit = MotorKit(pwm)
pwm = pwmio.PWMOut(board.D8, frequency=50)
potentiometer = AnalogIn(board.A1)  

while True:

    print((potentiometer.value,))    

    time.sleep(0.25)      