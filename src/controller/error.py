import gc

def raise_error(errorcode):
    errorcodes={
        'ERR_FS_1':'File Path Not Valid'
        'ERR_FS_2':'Access Denied',
        'ERR_ME_1':'Unsupported HTTP Method' 
    }
    data={errorcode:errorcodes[errorcode]}
    return data
