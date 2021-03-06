# SSD1306 OLED with Raspberry Pi Pico
SSD1306 OLED display library for Raspberry Pi Pico using MicroPython. 

Get your 16-Pixel RGB LED Ring Light at: https://makersportal.com/shop/16-pixel-rgb-led-ring-light <br>
Follow Along with the full tutorial at: https://makersportal.com/blog/ws2812-ring-light-with-raspberry-pi-pico

### JUMP TO:
<a href="#wiring">- Wiring Diagram</a><br>
<a href="#lib">- MicroPython SSD1306 Library</a><br>
<a href="#examples">- SSD1306 Examples with Pico</a><br>

The RPi Pico WS2812 library can be downloaded using git:

    git clone https://github.com/makerportal/rpi-pico-ssd1306

<a id="wiring"></a>
# - Wiring Diagram -

The wiring between the Pico and SSD1306 OLED is given below:

| Pico | SSD1306 |
| --- | --- |
| 3V3 (Pin 36) | VDD |
| GND (Pin 38) | GND | 
| I2C1_SDA (GP26) | SDA |
| I2C1_SCL (GP27) | SCK |

![SSD1306 RPi Pico Wiring](/images/ssd1306_w_RPi_Pico_white.jpg)

The SSD1306 OLED is wired to the RPi Pico via the I2C port. On the Pico, there are two different I2C ports I2C0, I2C1. We are wiring to the I2C1 port via GPIO pins 26/27 (physical pins 31/32).

<a id="lib"></a>
# - MicroPython SSD1306 Library -
Library...

<a id="examples"></a>
# - SSD1306 Examples with Pico -
Testing...
