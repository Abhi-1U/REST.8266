import gc
def software_details():
    """
    returns software details
    """
    try:
        import os
        lists=[]
        for value in os.uname():
            lists.append(value)
        sw_data={'sysname':lists[0],'nodename':lists[1],'release':lists[2],'version':lists[3],'machine':lists[4]}
        return sw_data
    except Exception as e:
        print(e)
    finally:
        gc.collect()
        
def hardware_details():
    """
    returns hardware details
    """
    try:
        import esp
        dev_data={'Board':'ESP8266EX','Arch':'Xtensa 32bit','Firmware':'MicroPython','RAM':98304,'External-ROM':esp.flash_size()}
        return dev_data
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def unique_id():
    """
    Returns Unique ID for the Hardware
    """
    try:
        import binascii,machine
        data={'Unique ID':binascii.hexlify(machine.unique_id())}
        return data
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def webrepl(response):
    """
    Initiate WebREPL
    """
    try:
        from controller.success import success_code
        import webrepl
        webrepl.start()
        return success_code('OK_WR_1')
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def webrepl_configs(password,response):
    """
    Configure WebREPL Password
    """
    try:
        import os
        from controller.success import success_code
        os.remove('/webrepl_cfg.py')
        code="PASS='"+str(password)+"'"
        with open('/webrepl_cfg.py','w') as f:
            f.write(code)
        return success_code('OK_WR_2')
    except Exception as e:
        print(e)
    finally:
        gc.collect()
def reset(response):
    """
    Hard Reset Device
    """
    try:
        yield from response.aclose()
        yield from response.aclose()
        yield from response.aclose()
        import machine
        machine.reset()
    except Exception as e:
        print(e)
    finally:
        machine.reset()
        gc.collect() 
       
