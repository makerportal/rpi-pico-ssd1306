# SSD1306 OLED with Raspberry Pi Pico
SSD1306 OLED display library for Raspberry Pi Pico using MicroPython. 

Get your 16-Pixel RGB LED Ring Light at: https://makersportal.com/shop/16-pixel-rgb-led-ring-light <br>
Follow Along with the full tutorial at: https://makersportal.com/blog/ws2812-ring-light-with-raspberry-pi-pico

### JUMP TO:
<a href="#start">- Wiring Diagram</a><br>
<a href="#state">- MicroPython State Machine</a><br>
<a href="#examples">- WS2812 Algorithm Examples </a><br>
<a href='#google'>- Google Home and Amazon Alexa LED Emulator </a><br>

The RPi Pico WS2812 library can be downloaded using git:

    git clone https://github.com/makerportal/rpi-pico-ws2812

<a id="start"></a>
# - Wiring Diagram -

The wiring between the Pico and SSD1306 OLED is given below:

| Pico | SSD1306 |
| --- | --- |
| 3V3 (Pin 36) | VDD |
| GND (Pin 38) | GND | 
| I2C1_SDA (GP26) | SDA |
| I2C1_SCL (GP27) | SCK |

![SSD1306 RPi Pico Wiring](/images/ssd1306_w_RPi_Pico_white.jpg)

