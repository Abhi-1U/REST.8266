# This file is executed on every boot (including wake-boot from deepsleep)
try:
  import usocket as socket
except:
  import socket


import network
import utime
import esp
import os
esp.osdebug(None)

import gc
gc.collect()

ssid = 'SSID'
password = 'passcode'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
led = Pin(2, Pin.OUT)
#import webrepl
#webrepl.start()
