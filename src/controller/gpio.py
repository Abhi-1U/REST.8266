import gc

def adc_read():
    """
    Read ADC0 value
    """
    try:
        from machine import ADC
        adc = ADC(0)
        data={'adc-level':adc.read()}
        return data
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def gpio_config(pin_no,pin_mode,setup):
    """
    Set Pin as GPIO IN/OUT
    """
    try:
        from machine import Pin
        pin_no=int(pin_no)
        if pin_mode=='IN':
            if setup=='EPUR':
                pin=Pin(int(pin_no),Pin.IN,Pin.PULL_UP)
                value={'P-val':pin.value()}
                return value
            if setup=='EPDR':
                pin=Pin(pin_no,Pin.IN,Pin.PULL_DOWN)
                value={'P-val':pin.value()}
                return value
            else:
                pin=Pin(pin_no,Pin.IN)
                value={'P-val':pin.value()}
                return value
        if pin_mode=='OUT':
            pass
        return value
    except Exception as e:
        print(e)
    finally:
        gc.collect()
