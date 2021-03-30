from userver.server import jsonify,parse_qs,start_response

def status(request , response):
    if(request.method=='GET'):
        from controller.led import led_toggle,led_value
        yield from jsonify(response, led_value())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def control(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.led import led_toggle,led_value
        if 'led' in qs:
            led_toggle(qs['led'])
        yield from jsonify(response, led_value())
    elif(request.method=='POST'or request.method=='PATCH'):
        yield from request.read_form_data()
        from controller.led import led_toggle,led_value
        if 'led' in request.form:
            led_toggle(request.form['led'])
        yield from jsonify(response, led_value())
    elif(request.method=='PUT'):
        yield from request.read_form_data()
        from controller.led import led_toggle,led_value
        if 'led' in request.form:
            led_toggle(request.form['led'])
        yield from start_response(response)
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))
