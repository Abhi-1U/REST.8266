import gc
def freq_value():
    """
    Read CPU frequency in Hz
    """
    try:
        from machine import freq
        freq_data={'freq':freq()}
        return freq_data
    except Exception as e:
        print(e)
    finally:
        gc.collect()
def freq_config(string):
    """
    Set CPU frequency 
    OC = 160MHz
    PS = 80MHz
    """
    try:
        from machine import freq
        if string=='OC':
            freq(160000000)
        if string=='PS':
            freq(80000000)
        gc.collect()
    except Exception as e:
        print('toggle Exception',e)
    finally:
        gc.collect()
