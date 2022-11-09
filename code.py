
from unittest.mock import MagicProxy
import board
import time
from analogio import AnalogIn
from analogio import AnalogOut
from adafruit_motor import motor as motor

motor = AnalogOut(board.A0)
potentiometer = AnalogIn(board.A2)  # potentiometer connected to A1, power & ground

while True:
    motor.val = potentiometer.value
    motor.value = motorVal
    print(motorVal)
    time.sleep(0.05)
