import Lcd
from time import *

lcd = Lcd.Lcd()
lcd.lcd_clear()

sleep(5)
lcd.lcd_backlight("off")
sleep(5)
lcd.lcd_backlight("on")

lcd.mprint("Es Klappt Teil 2", 1)
