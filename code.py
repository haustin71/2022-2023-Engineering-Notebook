
from unittest.mock import MagicProxy
import board
import time
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import pwmio
import adafruit_motor.servo
servo = adafruit_motor.servo.Servo(pwm)
pwm = pwmio.PWMOut(board.D8, frequency=50)