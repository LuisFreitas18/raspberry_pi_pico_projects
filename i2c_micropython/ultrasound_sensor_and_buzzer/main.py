import machine
from machine import I2C, Pin, time_pulse_us, PWM
import utime

from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq = 400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

TRIG_PIN = Pin(2, Pin.OUT)
ECHO_PIN = Pin(3, Pin.IN)

BUZZER_PIN = Pin(4, Pin.OUT)
BUZZER_PIN.high()

def get_distance():
    TRIG_PIN.low()
    utime.sleep_us(2)
    TRIG_PIN.high()
    utime.sleep_us(10)
    TRIG_PIN.low()

    duration = time_pulse_us(ECHO_PIN, 1, 30000) # 30ms
    distance_cm = (duration * 0.343) / 2

    return distance_cm

while True:
    lcd.clear()
    distance = get_distance()
    print("Distance: ", distance)
    lcd.move_to(0,0)
    lcd.putstr("USSensorDistance :")
    lcd.move_to(0,1)
    lcd.putstr(str(distance))

    if distance < 150:
        print("WARNING. Object detected below 150mm")
        BUZZER_PIN.low()
    else:
        BUZZER_PIN.high()

    utime.sleep(0.5)
    lcd.clear()
