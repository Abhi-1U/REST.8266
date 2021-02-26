import gc
def led_toggle(string):
    """
    Set the LED value ON/OFF
    """
    try:
        from machine import Pin
        led = Pin(2, Pin.OUT)
        if string=='ON':
            led.value(0)
        if string=='OFF':
            led.value(1)
        gc.collect()
    except Exception as e:
        print('toggle Exception',e)
def led_value():
    """
    Fetch The LED Value ON/OFF
    """
    try:
        from machine import Pin
        led = Pin(2, Pin.OUT)
        if led.value() == 0:
            led_data={'LED':'ON'}
        if led.value() == 1:
            led_data={'LED':'OFF'}
        return led_data
    except Exception as e:
        print(e)
    finally:
        gc.collect()
