
import time
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
countval = 0
# get and i2c object

i2c = board.I2C()
btn = DigitalInOut(board.D1)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
btn2 = DigitalInOut(board.D2)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

while True:
       if not btn2.value:
        if not btn.value:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("countval")
            lcd.set_cursor_pos(0,13)
            countval = countval + 1
            lcd.print(str(countval))
        else:
            pass
    
        if not btn2.value:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("countval")
            countval = countval - 1
            lcd.set_cursor_pos(0,13)
            lcd.print(str(countval))
        else:
            pass
            time.sleep(0.1) # sleep for debounce