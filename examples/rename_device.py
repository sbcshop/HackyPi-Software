''' 
This script rename you device from default circuitpython to your favorite name,
Just save this script as code.py in HackyPi, then remove and re-insert.
'''
import storage

storage.remount("/", readonly=False)

m = storage.getmount("/")
m.label = "HackyPi"    # replace name which you are interested for your device

storage.remount("/", readonly=True)

storage.enable_usb_drive()

