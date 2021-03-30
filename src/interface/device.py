from userver.server import jsonify,parse_qs,start_response

def software(request , response):
    if(request.method=='GET'):
        from controller.device import software_details
        yield from jsonify(response, software_details())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def hardware(request , response):
    if(request.method=='GET'):
        from controller.device import hardware_details
        yield from jsonify(response, hardware_details())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def uid(request , response):
    if(request.method=='GET'):
        from controller.device import unique_id
        yield from jsonify(response, unique_id())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def reset_dev(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.device import reset
        rset=''
        if 'reset' in qs:
            rset=(qs['reset'])
        if rset=='True':
            yield from reset(response)
    elif(request.method=='POST'or request.method=='PATCH'):
        yield from request.read_form_data()
        from controller.device import reset
        rset=''
        if 'reset' in request.form:
            rset=(request.form['reset'])
        if rset=='True':
            yield from reset(response)
    elif(request.method=='PUT'):
        yield from request.read_form_data()
        rset=''
        from controller.device import reset
        if 'reset' in request.form:
            rset=(request.form['reset'])
        if rset=='True':
            yield from reset(response)
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def webrepl_mode(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.device import webrepl
        rt=''
        if 'repl' in qs:
            rt=(qs['repl'])
        if rt=='True':
            yield from jsonify(response,webrepl(response))
    elif(request.method=='POST'or request.method=='PATCH'):
        yield from request.read_form_data()
        from controller.device import webrepl
        rt=''
        if 'repl' in request.form:
            rt=(request.form['repl'])
        if rt=='True':
            yield from jsonify(response,webrepl(response))
    elif(request.method=='PUT'):
        yield from request.read_form_data()
        rt=''
        from controller.device import webrepl
        if 'repl' in request.form:
            rt=(request.form['repl'])
        if rt=='True':
            webrepl(response)
            yield from start_response(response)
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))
        
def wc(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.device import webrepl_configs
        rt=''
        if 'password' in qs:
            rt=(qs['password'])
        yield from jsonify(response,webrepl_configs(rt,response))
    elif(request.method=='POST'or request.method=='PATCH'):
        yield from request.read_form_data()
        from controller.device import webrepl_configs
        rt=''
        if 'password' in request.form:
            rt=(request.form['password'])
        yield from jsonify(response,webrepl_configs(rt,response))
    elif(request.method=='PUT'):
        yield from request.read_form_data()
        rt=''
        from controller.device import webrepl_configs
        if 'password' in request.form:
            rt=(request.form['password'])
        if rt=='True':
            webrepl_configs(rt,response)
            yield from start_response(response)
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))
        


