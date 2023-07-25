import storage

storage.remount("/", readonly=False)

m = storage.getmount("/")
m.label = "HackyPi"    # put name which you want for your device

storage.remount("/", readonly=True)

storage.enable_usb_drive()

