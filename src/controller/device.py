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
        dev_data={'Board':'ESP8266EX','Arch':'Xtensa 32bit','Firmware':'MicroPython','RAM':'98,304','External-ROM':str(esp.flash_size())}
        return dev_data
    except Exception as e:
        print(e)
    finally:
        gc.collect()
