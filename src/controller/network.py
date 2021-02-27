import gc

def signal_strength(code):
    """
    returns text of strength rssi value
    """
    if code >= -5:
        return 'Amazing'
    if code >= -20:
        return 'Very Good'
    if code >= -50:
        return 'Good'
    if code >= -70:
        return 'Fair'
    if code >= -80:
        return 'Poor'
    if code >= -90:
        return 'Very Poor'
    else:
        return 'NA'

def wifi_mode(code):
    """
    returns text of mode code
    """
    if code==1:
        return 'IEEE 802.11b'
    if code==2:
        return 'IEEE 802.11g'
    if code==3:
        return 'IEEE 802.11n'
    else:
        return 'unknown'
def wifi_status(code):
    """
    returns text of status code
    """
    if code==0:
        return 'STAT_IDLE'
    if code==1:
        return 'STAT_CONNECTING'
    if code==2:
        return 'STAT_WRONG_PASSWORD'
    if code==3:
        return 'STAT_NO_AP_FOUND'
    if code==4:
        return 'STAT_CONNECT_FAIL'
    if code==5:
        return 'STAT_GOT_IP'
    else:
        return 'NA'
def ifconfig():
    """
    Return Ifconfig data
    """
    try:
        import network
        data=network.WLAN(network.STA_IF).ifconfig()
        ifco_data={'IP':data[0],'Mask':data[1],'Gateway':data[2],'DNS':data[3]}
        return ifco_data
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def rssi():
    """
    returns rssi value of network
    Received Signal Strength Indicator
    """
    try:
        import network
        data=network.WLAN(network.STA_IF).status('rssi')
        rssi_data={"rssi":data}
        return rssi_data
    except Exception as e:
        print(e)
    finally:
        gc.collect()

def net_status():
    """
    Retuurns some connection status
    """
    try:
        import network
        data=network.WLAN(network.STA_IF)
        net_stats={'connected':data.isconnected(),'active':data.active(),'status':wifi_status(data.status()),
                   'HW_protocol':wifi_mode(network.phy_mode()),'strength':signal_strength(data.status('rssi'))}
        return net_stats
    except Exception as e:
        print(e)
    finally:
        gc.collect()
def wifi_scan():
    """
    Scans for nearby local WiFi networks and returns list of them
    """
    try:
        import network
        data=network.WLAN(network.STA_IF)
        connections=data.scan()
        scan_data={'available-networks':connections,}
        return scan_data
    except Exception as e:
        print(e)
    finally:
        gc.collect()
