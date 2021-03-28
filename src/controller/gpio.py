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
    Config GPIO Pin
    """
    try:
        from machine import Pin
        from controller.success import success_code
        pin_no=int(pin_no)
        if pin_mode=='IN':
            if setup=='EPUR':
                pin=Pin(pin_no,Pin.IN,Pin.PULL_UP)
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
            if setup=='HIGH':
                pin=Pin(int(pin_no),Pin.OUT,value=1)
                return success_code('OK_IO_1')
            if setup=='LOW':
                pin=Pin(pin_no,Pin.OUT,value=0)
                return success_code('OK_IO_1')
            else:
                pin=Pin(pin_no,Pin.OUT,value=1)
                return success_code('OK_IO_1')
        return value
    except Exception as e:
        print(e)
    finally:
        gc.collect()
def pwm(pin,freq,duty_cycle):
    """
    Set Up PWM
    """
    try:
        from controller.success import success_code
        from machine import Pin, PWM
        pin=int(pin)
        freq=int(freq)
        duty_cycle=int(duty_cycle)
        check_pin(pin_no,mode='PWM')
        check_freq(freq)
        check_dc(duty_cycle)
        pwm2 = PWM(Pin(pin), freq=freq, duty=duty)
        return success_code('OK_IO_3')
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def deinit_pwm(pin):
    """
    De-init PWM
    """
    try:
        from controller.success import success_code
        from machine import Pin, PWM
        pin=int(pin)
        pwm2 = PWM(Pin(pin))
        pwm2.deinit()
        return success_code('OK_IO_4')
    except Exception as e:
        print(e)
    finally:
        gc.collect()
