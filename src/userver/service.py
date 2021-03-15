import gc
import uasyncio as asyncio
from userver.server import WebServer,jsonify,parse_qs
router=WebServer()

#--Board LED Control
@router.route('/led/status', method='GET')
def led_status(request , response):
    """
    led status
    """
    from controller.led import led_toggle,led_value
    led_data=led_value()
    gc.collect()
    yield from jsonify(response, led_data)

@router.route('/led/config', method='POST')
def led_control_post(request , response):
    yield from request.read_form_data()
    from controller.led import led_toggle,led_value
    if 'led' in request.form:
        led_toggle(request.form['led'])
    data=led_value()
    gc.collect()
    yield from jsonify(response, data)

@router.route('/led/config', method='GET')
def led_control_get(request , response):
    qs=parse_qs(request.qs)
    from controller.led import led_toggle,led_value
    if 'led' in qs:
        led_toggle(qs['led'])
    data=led_value()
    gc.collect()
    yield from jsonify(response, data)

#--CPU Operations
@router.route('/cpu/status', method='GET')
def freq_status(request , response):
    """
    CPU Freq status
    """
    from controller.cpu import freq_value,freq_config
    freq_data=freq_value()
    gc.collect()
    yield from jsonify(response, freq_data)

@router.route('/cpu/config', method='POST')
def freq_control_post(request , response):
    yield from request.read_form_data()
    from controller.cpu import freq_value,freq_config
    if 'freq' in request.form:
        freq_config(request.form['freq'])
    data=freq_value()
    gc.collect()
    yield from jsonify(response, data)
    
@router.route('/cpu/config', method='GET')
def freq_control_get(request , response):
    qs=parse_qs(request.qs)
    from controller.cpu import freq_value,freq_config
    if 'freq' in qs:
        freq_config(qs['freq'])
    data=freq_value()
    gc.collect()
    yield from jsonify(response, data)

#-- Device Software details
@router.route('/device/software', method='GET')
def device_software(request , response):
    """
    Device Software version
    """
    from controller.device import software_details
    gc.collect()
    yield from jsonify(response, software_details())

#-- Device Hardware details 
@router.route('/device/hardware', method='GET')
def device_software(request , response):
    """
    Device Software version
    """
    from controller.device import hardware_details
    gc.collect()
    yield from jsonify(response, hardware_details())

#-- Device Unique ID
@router.route('/device/uid', method='GET')
def device_uid(request , response):
    """
    Device Unique ID
    """
    from controller.device import unique_id
    gc.collect()
    yield from jsonify(response, unique_id())
    
#-- Network Operations
@router.route('/network/ifconfig', method='GET')
def network_ifconfig(request , response):
    """
    Network ifconfig
    """
    from controller.network import ifconfig
    gc.collect()
    yield from jsonify(response, ifconfig())

@router.route('/network/rssi', method='GET')
def network_rssi(request , response):
    """
    Network rssi value
    """
    from controller.network import rssi
    gc.collect()
    yield from jsonify(response, rssi())

@router.route('/network/status', method='GET')
def network_status(request , response):
    """
    Network status
    """
    from controller.network import net_status
    gc.collect()
    yield from jsonify(response, net_status())

@router.route('/network/scan', method='GET')
def network_scan(request , response):
    """
    Wireless Scan
    """
    from controller.network import wifi_scan
    gc.collect()
    yield from jsonify(response, wifi_scan())

#-- GPIO control
@router.route('/gpio/readadc', method='GET')
def adc_level(request , response):
    """
    ADC A0 Level (0-1024)
    """
    from controller.gpio import adc_read
    gc.collect()
    yield from jsonify(response, adc_read())

@router.route('/gpio/config', method='POST')
def gpio_control_post(request , response):
    yield from request.read_form_data()
    from controller.gpio import gpio_config
    pin=None
    mode=None
    setup=None
    if 'pin' in request.form:
        pin=request.form['pin']
    if 'mode' in request.form:
        mode=request.form['mode']
    if 'setup' in request.form:
        setup=request.form['setup']
    data=gpio_config(pin,mode,setup)
    gc.collect()
    yield from jsonify(response, data)

@router.route('/gpio/config', method='GET')
def gpio_control_get(request , response):
    qs=parse_qs(request.qs)
    from controller.gpio import gpio_config
    pin=None
    mode=None
    setup=None
    if 'pin' in qs:
        pin=qs['pin']
    if 'mode' in qs:
        mode=qs['mode']
    if 'setup' in qs:
        setup=qs['setup']
    data=gpio_config(pin,mode,setup)
    gc.collect()
    yield from jsonify(response, data)


@router.route('/fsys/ls', method='GET')
def fsys_ls(request , response):
    """
    list fileSystem
    """
    qs=parse_qs(request.qs)
    from controller.file import ls_file
    if 'path' in qs:
        ls_data=ls_file(qs['path'])
    gc.collect()
    yield from jsonify(response, ls_data)

@router.route('/fsys/ls', method='POST')
def freq_control_post(request , response):
    yield from request.read_form_data()
    from controller.file import ls_file
    if 'path' in request.form:
        ls_data=ls_file(request.form['path'])
    #print("Query String")
    gc.collect()
    yield from jsonify(response, ls_data)

#--Clock Time of Server
@router.route('/clock/time', method='GET')
def network_scan(request , response):
    """
    Get Server Clock time
    """
    from controller.clocks import localtime
    gc.collect()
    yield from jsonify(response, localtime())
def main():
    loop = asyncio.get_event_loop()
    loop.create_task(asyncio.start_server(router.handle, '0.0.0.0', 80))
    gc.collect()
    loop.run_forever()
