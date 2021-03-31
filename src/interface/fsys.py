from userver.server import jsonify,parse_qs,start_response
def chdir(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.file import change_dir
        path=''
        if 'path' in qs:
            path=(qs['path'])
        yield from jsonify(response, change_dir(path))
    elif(request.method=='POST'or request.method=='PATCH'):
        yield from request.read_form_data()
        from controller.file import change_dir
        path=''
        if 'path' in request.form:
            path=(request.form['path'])
        yield from jsonify(response, change_dir(path))
    elif(request.method=='PUT'):
        yield from request.read_form_data()
        path=''
        from controller.file import change_dir
        if 'path' in request.form:
            change_dir(request.form['path'])
        yield from start_response(response)
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def mkdir(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.file import make_folder
        path=''
        if 'path' in qs:
            path=(qs['path'])
        yield from jsonify(response, make_folder(path))
    elif(request.method=='POST'or request.method=='PATCH'):
        yield from request.read_form_data()
        from controller.file import make_folder
        path=''
        if 'path' in request.form:
            path=(request.form['path'])
        yield from jsonify(response, make_folder(path))
    elif(request.method=='PUT'):
        yield from request.read_form_data()
        path=''
        from controller.file import make_folder
        if 'path' in request.form:
            make_folder(request.form['path'])
        yield from start_response(response)
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def rmdir(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.file import remove_folder
        path=''
        if 'path' in qs:
            path=(qs['path'])
        yield from jsonify(response, remove_folder(path))
    elif(request.method=='POST'or request.method=='PATCH' or request.method=='DELETE'):
        yield from request.read_form_data()
        from controller.file import remove_folder
        path=''
        if 'path' in request.form:
            path=(request.form['path'])
        yield from jsonify(response, remove_folder(path))
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def rm(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.file import rm
        path=''
        if 'path' in qs:
            path=(qs['path'])
        yield from jsonify(response, rm(path))
    elif(request.method=='POST'or request.method=='PATCH' or request.method=='DELETE'):
        yield from request.read_form_data()
        from controller.file import rm
        path=''
        if 'path' in request.form:
            path=(request.form['path'])
        yield from jsonify(response, rm(path))
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def ls(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.file import ls_file
        path=''
        if 'path' in qs:
            path=(qs['path'])
        yield from jsonify(response, ls_file(path))
    elif(request.method=='POST'or request.method=='PATCH'):
        yield from request.read_form_data()
        from controller.file import ls_file
        path=''
        if 'path' in request.form:
            path=(request.form['path'])
        yield from jsonify(response, ls_file(path))
    elif(request.method=='PUT'):
        yield from request.read_form_data()
        path=''
        from controller.file import ls_file
        if 'path' in request.form:
            ls_file(request.form['path'])
        yield from start_response(response)
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def read(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.file import readfile
        path=''
        if 'path' in qs:
            path=(qs['path'])
        yield from readfile(path,response)
    elif(request.method=='POST'or request.method=='PATCH'):
        yield from request.read_form_data()
        from controller.file import readfile
        path=''
        if 'path' in request.form:
            path=(request.form['path'])
        yield from readfile(path,response)
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def rename(request , response):
    if(request.method=='GET'):
        qs=parse_qs(request.qs)
        from controller.file import rename
        path=''
        newname=''
        if 'path' in qs:
            path=(qs['path'])
        if 'newname' in qs:
            newname=(qs['newname'])
        yield from jsonify(response, rename(path,newname))
    elif(request.method=='POST'or request.method=='PATCH'):
        yield from request.read_form_data()
        from controller.file import rename
        path=''
        newname=''
        if 'path' in request.form:
            path=(request.form['path'])
        if 'newname' in request.form:
            newname=(request.form['newname'])
        yield from jsonify(response, rename(path,newname))
    elif(request.method=='PUT'):
        yield from request.read_form_data()
        path=''
        from controller.file import rename
        if 'path' in request.form:
            path=(request.form['path'])
        if 'newname' in request.form:
            newname=(request.form['newname'])
        rename(path,newname)
        yield from start_response(response)
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))

def cwd(request , response):
    if(request.method=='GET'):
        from controller.file import get_cwd
        yield from jsonify(response, get_cwd())
    else:
        from controller.error import raise_error
        yield from jsonify(response, raise_error('ERR_ME_1'))




