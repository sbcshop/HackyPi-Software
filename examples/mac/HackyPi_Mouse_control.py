# This program demonstrate how HackyPi can works as Mouse to move cursor and do right/left clicks 
# Code also display some text on TFT screen
# This code tested and works for Windows/MAC/Linux
import time
import os
import usb_hid
import digitalio
import board
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_hid.mouse import Mouse
from adafruit_st7789 import ST7789
import random

# Declare some parameters used to adjust style of text and graphics
BORDER = 12
FONTSCALE = 3
BACKGROUND_COLOR = 0xFF0000  # red
FOREGROUND_COLOR = 0xFFFF00  # Purple
TEXT_COLOR = 0x0000ff

# Release any resources currently in use for the displays
displayio.release_displays()

tft_clk = board.GP10 # must be a SPI CLK
tft_mosi= board.GP11 # must be a SPI TX
tft_rst = board.GP12
tft_dc  = board.GP8
tft_cs  = board.GP9
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)

# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7789(display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

tft_bl  = board.GP13
led = digitalio.DigitalInOut(tft_bl)
led.direction = digitalio.Direction.OUTPUT
led.value=True

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# This function creates colorful rectangular box 
def inner_rectangle():
    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(display.width - BORDER * 2, display.height - BORDER * 2, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = FOREGROUND_COLOR
    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
    splash.append(inner_sprite)
    
#Function to print data on TFT
def print_onTFT(text, x_pos, y_pos): 
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_group = displayio.Group(scale=FONTSCALE,x=x_pos,y=y_pos,)
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)
    
inner_rectangle()
print_onTFT("Welcome to", 30, 40)
print_onTFT("HackyPi", 50, 80)

time.sleep(3)
x = random.randint(-20, 10)
y = random.randint(-20, 10)

try:
    #Creat instance for mouse
    mouse = Mouse(usb_hid.devices)
    
    #Display text on TFT
    inner_rectangle()
    print_onTFT("Cursor", 40, 40)
    print_onTFT("Move...", 40, 80)
    
    time.sleep(2)  # Debounce delay
    
    #procedure for random movement of cursor 
    for i in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-300, 700)
        strData = 'x= ' + str(x) + '\ny= ' + str(y)
        print(strData) #prints current cursor position on terminal
        
        inner_rectangle()
        print_onTFT(strData, 40, 40)
        
        mouse.move(x)
        mouse.move(y)
        time.sleep(2)  # wait few second
        
        mouse.click(mouse.RIGHT_BUTTON)
        
        inner_rectangle()
        print_onTFT("Right", 40, 40)
        print_onTFT("Click!", 40, 80)
        time.sleep(1) # wait for few time before another move
    
    inner_rectangle()
    print_onTFT("Thank", 40, 40)
    print_onTFT("You!", 40, 80)
    time.sleep(1) # wait for few time before another move
    
except Exception as ex:
    raise ex
