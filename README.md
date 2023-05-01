# HackyPi-Software
HackyPi is a compact and versatile USB device powered by the RP2040 microcontroller. It is a powerful tool for both ethical hacking and learning programming, compatible with all major operating systems. You can program using python language. Its sleek and modern design, combined with a user-friendly interface, makes it easy to use for beginners and experts alike. HackyPi is highly portable.

<img src = "https://cdn.shopify.com/s/files/1/1217/2104/files/HackyPI2copy.jpg?v=1681998205"/>

## Setup HackyPi
1. Download and Install Thonny IDE for your respective OS from Link [Download Thonny](https://thonny.org/)
   
   <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img.JPG" />
   
2. Adding **CircuitPython** bootloader in HackyPi 

     For this first you need to *Press and Hold* the boot button on HackyPi, without releasing the button connect it to USB port of PC/laptop. 
Then you see a new device named "RPI-RP2" drag file ["firmware.uf2"](https://github.com/sbcshop/HackyPi-Software/blob/main/firmware.uf2) available in this repository to the device as shown in figure, or you can download from Circuitpython official website [click here](https://circuitpython.org/board/raspberry_pi_pico/)
     
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" /> 
     <img src= "https://github.com/sbcshop/HackyPi-Software/blob/main/images/HackyPi_bootloader_install.gif" />
After downloading just copy and paste firmware file to "RPI-RP2" folder and then remove the device.
Now at this step bootloader installed properly inside Pico of Hackypi. To verify remove device and re-insert into PC/Laptop, no need to press boot button. 
This time you will see a new device as shown in the below image:-
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />

**Running First Code in HackyPi**
1. Start Thonny IDE application, after this go to run->select interpreter, choose device and suitable com port
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img18.png" />
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img19.png" />
    Write simple python code and click on green run button
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img20.png" />
    <img src= "https://github.com/sbcshop/HackyPi-Software/blob/main/images/sample_hello_program.png" />

2. Now you are ready to try out your own codes. Even you can try some of below Example codes provided, for that just copy all the files (library files) from [```lib```](https://github.com/sbcshop/HackyPi-Software/tree/main/lib) folder of this repository and paste inside the HackyPi ```lib``` folder

## Examples Codes  
This example folder in repository includes ready to use and experimental code with HackyPi 
  * [Windows](https://github.com/sbcshop/HackyPi-Software/tree/main/examples/mac) - This directory includes examples of HackyPi for Windows OS, for example
    - Example 1: [To Access Camera](https://github.com/sbcshop/HackyPi-Software/blob/main/examples/windows/HackyPi_AccessCamera.py)
    - Example 2: [Make Cool Fake Hacking with Friends laptop](https://github.com/sbcshop/HackyPi-Software/blob/main/examples/windows/HackyPi_CoolFake_Hacking.py) 
    - Example 3: [Just connect HackyPi and your System will Shutdown](https://github.com/sbcshop/HackyPi-Software/blob/main/examples/windows/HackyPi_PC_shutdown.py) and Many more...
  * [Mac](https://github.com/sbcshop/HackyPi-Software/tree/main/examples/windows) - This directory includes examples of HackyPi Use in Mac OS
    - Example 1: [Delete Browsing History](https://github.com/sbcshop/HackyPi-Software/blob/main/examples/mac/HackyPi_DeleteBrowsing_History.py)
    - Example 2: [Control Mouse](https://github.com/sbcshop/HackyPi-Software/blob/main/examples/mac/HackyPi_Mouse_control.py) 
    - Example 3: [Open website](https://github.com/sbcshop/HackyPi-Software/blob/main/examples/mac/HackyPi_openWebsite.py) and Many more...

Play with it and create your own, **Happy Coding!** 

## Documentation

* [HackyPi Hardware](https://github.com/sbcshop/HackyPi-Hardware) 
* [HackyPi Schematic](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Design%20Data/SCH.pdf) 
* [CircuitPython getting started](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython)
* [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)
* [HackyPi Hardware Design](https://github.com/sbcshop/HackyPi-Hardware/tree/main/Design%20Data)


## Related Products

* [SquaryFi](https://shop.sb-components.co.uk/collections/raspberry-pi-pico/products/squary?variant=40443840921683) - ESP8266-12E version of SquaryPi

 ![SquaryFi](https://cdn.shopify.com/s/files/1/1217/2104/products/2_12d19ffa-bcda-47bf-8ea9-bb76fc40aee3.png?v=1670307456&width=300)
 
 * [Roundy](https://shop.sb-components.co.uk/products/roundy?variant=39785171681363) - 1.28" Round LCD version based on ESP8266 and RP2040
 
 ![Roundy](https://cdn.shopify.com/s/files/1/1217/2104/products/roundypi.png?v=1650457581&width=300)

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
