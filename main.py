#REST.8266 V0.1.2
def request_handler(conn, request):
    if request.find('/favicon.ico') == 6:
        fav_handler(conn)
        return False
    if request.find('/?led=on') == 6:
        led.value(0)
        response(conn, 'LED', 'ON')
        return True
    if request.find('/?led=off') == 6:
        led.value(1)
        response(conn, 'LED', 'OFF')
        return True
    if request.find('/freq/') == 6:
        response(conn, 'frequency', freq())
        return True
    if request.find('/ifconfig/') == 6:
        data = network.WLAN(network.STA_IF).ifconfig()
        keys = ('IP', 'Mask', 'Gateway', 'DNS')
        response_loop(conn, 'ifconfig', keys, data)
        return True
    if request.find('/?freq=OC') == 6:
        freq(160000000)
        response(conn, 'frequency', freq())
        return True
    if request.find('/?freq=PS') == 6:
        freq(80000000)
        response(conn, 'frequency', freq())
        return True
    else:
        conn.close()
        return False


def response_loop(conn, root, keys, data):
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Server: REST.8266 V0.1.2\n')
    conn.send('Content-Type: application/json\n')
    conn.send('Access-Control-Allow-Origin: *\n')
    conn.send('Connection: close\n\n')
    conn.send('{'+str(root)+':')
    for i in range(0, len(keys)):
        conn.send('{'+str(keys[i])+':'+str(data[i])+'},\n')
    conn.send('}')


def response(conn, key, data):
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Server: REST.8266\n')
    conn.send('Content-Type: application/json\n')
    conn.send('Access-Control-Allow-Origin: *\n')
    conn.send('Connection: close\n\n')
    conn.send('{'+str(key)+':'+str(data)+'}')


def fav_handler(conn):
    conn.send('HTTP/1.1 204 OK\n')
    conn.send('Server: REST.8266\n')
    conn.send('Connection: close\n\n')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print(request)
    request_handler(conn, request)
    conn.close()
    gc.collect()
