import Lcd
from time import *

lcd = Lcd.Lcd()
lcd.clear()

sleep(5)
lcd.backlight("off")
sleep(5)
lcd.backlight("on")

lcd.write_line1("Es Klappt Teil 2")
