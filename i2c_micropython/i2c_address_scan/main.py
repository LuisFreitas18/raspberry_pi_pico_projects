from machine import I2C
i2c = I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq = 400000)
print(i2c.scan())
