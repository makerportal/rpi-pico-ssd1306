# SSD1306 OLED with Raspberry Pi Pico
SSD1306 OLED display library for Raspberry Pi Pico using MicroPython. 

Get your SSD1306 OLED Display and Frame: https://makersportal.com/shop/arduino-display-oled-ssd1306-i2c-display <br>
Follow along with the full tutorial: https://makersportal.com/blog/raspberry-pi-pico-oled-display

### JUMP TO:
<a href="#wiring">- Wiring Diagram</a><br>
<a href="#examples">- SSD1306 Examples with Pico</a><br>
<a href="#mapping">- Image Mapping with Python3</a><br>

The RPi Pico WS2812 library can be downloaded using git:

    git clone https://github.com/makerportal/rpi-pico-ssd1306

<a id="wiring"></a>
# - Wiring Diagram -

The wiring between the Pico and SSD1306 OLED is given below:
![SSD1306 RPi Pico Wiring](/images/ssd1306_w_RPi_Pico_white.jpg)
| Pico | SSD1306 |
| --- | --- |
| 3V3 (Pin 36) | VDD |
| GND (Pin 38) | GND | 
| I2C1_SDA (GP26) | SDA |
| I2C1_SCL (GP27) | SCK |

The SSD1306 OLED is wired to the RPi Pico via the I2C port. On the Pico, there are two different I2C ports I2C0, I2C1. We are wiring to the I2C1 port via GPIO pins 26/27 (physical pins 31/32).

<a id="examples"></a>
# - SSD1306 Examples with Pico -
The 'micropython' subfolder houses the actual codes to be uploaded to the Pico microcontroller via Thonny. 

Each example contains the ssd1306.py library, which should be uploaded as a separate file to the Pico microcontroller. The main.py file should be uploaded to the Pico and will act as the primary script, which runs after every boot. Thus, both files are required when testing each example. Additionally, if displaying an image, the 'imgfile.py' should also be saved locally on the Pico. 

<a id="mapping"></a>
# - Image Mapping with Python3 -
The Python3 folder houses a script that must be run with Python3 rather than MicroPython. The reason being - an image needs to be stored locally, which will then be converted to an array of bytes. This array of bytes is then stored in the 'imgfile.py' file. The 'imgfile.py' is what the SSD1306 reads and prints as the logo or image upon running the logo_display example.
