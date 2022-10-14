
import time
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object

i2c = board.I2C()
btn = DigitalInOut(board.D1)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
btn2 = DigitalInOut(board.D2)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
countval = 0
Btn_State = True
PrevBtn_State = True
Btn2_State = True
PrevBtn2_State = True
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

while True:
    while btn2.value == False:
        lcd.set_cursor_pos(0, 0)
        lcd.print("countval up")
        Btn_State = btn.value
        if Btn_State != PrevBtn_State:
            if not Btn_State:
                countval = countval + 1 
                lcd.clear()
                lcd.set_cursor_pos(0, 0)
                lcd.print(str(countval))
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(countval))
        PrevBtn_State = Btn_State
    else:
        lcd.set_cursor_pos(1,0)
        lcd.print("countval down")
        Btn2_State = btn2.value
        if Btn2_State != PrevBtn2_State:
            if not Btn2_State:
                    countval = countval - 1
                    lcd.clear()
                    lcd.set_cursor_pos(0,0)
                    lcd.print(str(countval))
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(countval))
        PrevBtn2_State = Btn2_State