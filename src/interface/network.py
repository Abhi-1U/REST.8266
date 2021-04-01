from userver.server import jsonify,parse_qs,start_response

def ifconfig(request , response):
    if(request.method=='GET'):
        from controller.network import ifconfig
        yield from jsonify(response, ifconfig())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def scan(request , response):
    if(request.method=='GET'):
        from controller.network import wifi_scan
        yield from jsonify(response, wifi_scan())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def status(request , response):
    if(request.method=='GET'):
        from controller.network import net_status
        yield from jsonify(response, net_status())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def rssi(request , response):
    if(request.method=='GET'):
        from controller.network import rssi
        yield from jsonify(response, rssi())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))
