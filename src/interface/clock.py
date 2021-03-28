from userver.server import jsonify,parse_qs,start_response

def ntp_time(request , response):
    from controller.clocks import ntpsync
    gc.collect()
    yield from jsonify(response, ntpsync())

def time(request , response):
    from controller.clocks import localtime
    gc.collect()
    yield from jsonify(response, localtime())
