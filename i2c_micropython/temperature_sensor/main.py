import machine
from machine import I2C, Pin
import utime

from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq = 400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.clear()

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706) / 0.001721, 2)
    print("Temperature = ", temperature)
    lcd.move_to(0,0)
    lcd.putstr("RPI-PICO Temp:")
    lcd.move_to(0,1)
    lcd.putstr(str(temperature))
    utime.sleep(0.5)
    lcd.clear()
