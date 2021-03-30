from userver.server import jsonify,parse_qs,start_response

def status(request , response):
    if(request.method=='GET'):
        from controller.cpu import freq_value,freq_config
        yield from jsonify(response, freq_value())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def config(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.cpu import freq_value,freq_config
        if 'freq' in qs:
            freq_config(qs['freq'])
        yield from jsonify(response, freq_value())
    elif(request.method=='POST' or request.method=='PATCH'):
        yield from request.read_form_data()
        from controller.cpu import freq_value,freq_config
        if 'freq' in request.form:
            freq_config(request.form['freq'])
        yield from jsonify(response, freq_value())

    elif(request.method=='PUT'):
        yield from request.read_form_data()
        from controller.cpu import freq_value,freq_config
        if 'cpu' in request.form:
            freq_config(request.form['cpu'])
        yield from start_response(response)
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))
