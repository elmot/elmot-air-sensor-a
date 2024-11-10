# MicroPython application for ESP32 which displays text on an SSD1306 OLED display connected with SPI
# Further examples in Rust with board configuration of ESP-Buddy is available at https://github.com/georgik/esp32-buddy-rs
import machine
from ssd1306 import SSD1306_I2C
from time import sleep


# ESP32 Pin assignment
i2c = machine.I2C(0, scl=machine.Pin(23), sda=machine.Pin(18))
oled = SSD1306_I2C(128, 32, i2c)

oled.rotate(0)


# Clear the oled display in case it has junk on it.
oled.fill(0)
oled.show()

# Write some text.
oled.text('Hello FEKT!', 0, 0)
oled.show()
sleep(2)

oled.text('ESP32', 0, 16)
oled.show()
sleep(2)

for i in range(0, 32):
    oled.scroll(0, -1)
    oled.show()
    sleep(0.1)

oled.text('Enjoy workshop!', 0, 0)
oled.show()

# Note: Neopixel is at GPIO 25, but it has inverted signal

import network
network.WLAN(network.STA_IF)