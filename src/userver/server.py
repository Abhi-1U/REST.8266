# Forked Web Server
# Micropython Runtime
import ure as re
import uerrno


def unquote_plus(string):
    string = string.replace('+', ' ')
    arr = string.split('%')
    arr2 = [chr(int(part[:2], 16)) + part[2:] for part in arr[1:]]
    return arr[0] + ''.join(arr2)


def parse_qs(string):
    params = {}
    if string:
        pairs = string.split('&')
        for pair in pairs:
            values = [unquote_plus(part) for part in pair.split('=', 1)]
            if len(values) == 1:
                values.append(True)
            if values[0] in params:
                if not isinstance(params[values[0]], list):
                    params[values[0]] = [params[values[0]]]
                params[values[0]].append(values[1])
            else:
                params[values[0]] = values[1]
    return params


def get_mime_type(fname):
    if fname.endswith('.html'):
        return 'text/html'
    if fname.endswith('.css'):
        return 'text/css'
    if fname.endswith('.svg'):
        return 'image/svg+xml'
    if fname.endswith('.png'):
        return 'image/png'
    if fname.endswith('.jpg'):
        return 'image/jpeg'
    if fname.endswith('.txt') or fname.endswith('.csv') or fname.endswith('.py') :
        return 'text/plain'
    return 'application/octet-stream'


def sendstream(writer, file_):
    buf = bytearray(64)
    while True:
        line = file_.readinto(buf)
        if not line:
            break
        yield from writer.awrite(buf, 0, line)


def jsonify(writer, pydict):
    import ujson
    yield from start_response(writer, 'application/json')
    yield from writer.awrite(ujson.dumps(pydict))


def start_response(writer, content_type='text/html', status='200', headers=None):
    yield from writer.awrite('HTTP/1.1 %s OK\r\n' % status)
    yield from writer.awrite('Server: REST.8266\n')
    yield from writer.awrite('Content-Type: ')
    yield from writer.awrite(content_type)
    yield from writer.awrite('\nAccess-Control-Allow-Origin: *\n')
    yield from writer.awrite('Connection: close\n\n')
    yield from writer.awrite('\r\n')

def http_error(writer, status):
    yield from start_response(writer, status=status)
    yield from writer.awrite(status)


class HTTPRequest(object):

    def read_form_data(self):
        size = int(self.headers[b'Content-Length'])
        print(size)
        data = yield from self.reader.read(size)
        form = parse_qs(data.decode())
        print(form)
        self.form = form

    def parse_qs(self):
        form = parse_qs(self.qs)
        self.form = form


class WebServer(object):

    def __init__(self):
        self.url_map = []
        self.templates_dir = '/templates'
        self.static_dir = '/static'
        self.headers_mode = 'parse'

    def parse_headers(self, reader):
        headers = {}
        while True:
            line = yield from reader.readline()
            if line == b'\r\n':
                break
            key, value = line.split(b':', 1)
            headers[key] = value.strip()
        return headers

    def handle(self, reader, writer):
        close = True #for closing connections
        try: 
            request_line = yield from reader.readline() #reads request line
            if request_line == b'': # Empty Request rejected
                yield from writer.aclose()
                return
            req = HTTPRequest()# object created
            request_line = request_line.decode()
            method, path, proto = request_line.split()# split into method,path,protocol
            if(method=='HEAD'):
               yield from start_response(writer)
            path = path.split('?', 1)# for GET query strings.
            qs = ''
            if len(path) > 1:
                qs = path[1] # Split of Query string part
            path = path[0] # split of path
            found = False # finding the uri in map
            for e in self.url_map:
                pattern = e[0] # Path
                handler = e[1] # Function
                extra = {} # Extra like methods
                if len(e) > 2:
                    extra = e[2] 

                if path == pattern:
                    found = True
                    break
                elif not isinstance(pattern, str):
                    m = pattern.match(path)
                    if m:
                        req.url_match = m
                        found = True
                        break

            if not found:
                headers_mode = 'skip'
            else:
                headers_mode = extra.get('headers', self.headers_mode)

            if headers_mode == 'skip':
                while True:
                    line = yield from reader.readline()
                    if line == b'\r\n':
                        break
            elif headers_mode == 'parse':
                req.headers = yield from self.parse_headers(reader)
            else:
                assert headers_mode == 'leave'

            if found:
                req.method = method
                req.path = path
                req.qs = qs
                req.reader = reader
                close = yield from handler(req, writer)
            else:
                yield from self.abort(writer, '404')
        except Exception as e:
            print('Exception',e)

        if close is not False: #Force Fully Closing unresolved uri's
            yield from writer.aclose()

    def abort(self, writer, status):
        yield from start_response(writer, status=status)
        yield from writer.awrite(status + '\r\n')

    def route(self, url, **kwargs):
        def _route(f):
            self.url_map.append((url, f))
            return f
        return _route

    def add_url_rule(self, url, func, **kwargs):
        self.url_map.append((url, func))



    

