import time
import board
import math
import busio
import terminalio
import displayio
import adafruit_imageload
from adafruit_st7789 import ST7789
import os
import adafruit_sdcard
import digitalio
import storage

spi = busio.SPI(board.GP18, board.GP19, board.GP16)
cs = digitalio.DigitalInOut(board.GP17)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

tft_bl = board.GP13
led = digitalio.DigitalInOut(tft_bl)
led.direction = digitalio.Direction.OUTPUT
led.value=True
# Release any resources currently in use for the displays
displayio.release_displays()

tft_clk = board.GP10 # must be a SPI CLK
tft_mosi= board.GP11 # must be a SPI TX
tft_rst = board.GP12
tft_dc  = board.GP8
tft_cs  = board.GP9
tft_bl  = board.GP13
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)

    
# Make the displayio SPI bus
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = ST7789(display_bus, rotation=180, width=135, height=240, rowstart=40, colstart=53)

# Make the main display context
main = displayio.Group()
display.show(main)

bmpfiles = sorted("/sd/images/" + fn for fn in os.listdir("/sd/images/") if fn.lower().endswith("bmp")) 

while True:
    if len(bmpfiles) == 0:
        print("N0, BMP Files")
        break

    for filename in bmpfiles:
        print("showing bmp image", filename)

        bitmap_file = open(filename, "rb")
        bitmap = displayio.OnDiskBitmap(bitmap_file)
        tile_grid = displayio.TileGrid(bitmap,pixel_shader=getattr(bitmap, 'pixel_shader', displayio.ColorConverter()))

        group = displayio.Group()
        group.append(tile_grid)
        display.show(group)

        time.sleep(2)# Show the image for 2 seconds
    time.sleep(0.01)