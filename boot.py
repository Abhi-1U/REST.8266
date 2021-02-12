#REST.8266 V0.1.2
try:
    import gc
    import usocket as socket
except:
    import socket

from machine import Pin,freq,RTC,ADC
import network
import utime
import esp
import os
esp.osdebug(None)

gc.collect()

ssid = 'YourWiFiSSID'
password = ':)'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

#RTC
rtc=RTC()

# LED
led = Pin(2, Pin.OUT)
