import gc

def raise_error(errorcode):
    errorcodes={
        'ERR_FS_1':'File Path Not Valid'
    }
    data={errorcode:errorcodes[errorcode]}
    return data
