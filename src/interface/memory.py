from userver.server import jsonify,parse_qs,start_response

def collect(request , response):
    if(request.method=='GET'):
        from controller.memory import force_gc
        yield from jsonify(response, force_gc())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def stack(request , response):
    if(request.method=='GET'):
        from controller.memory import stack_status
        yield from jsonify(response, stack_status())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def heap(request , response):
    if(request.method=='GET'):
        from controller.memory import heap_status
        yield from jsonify(response, heap_status())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))
