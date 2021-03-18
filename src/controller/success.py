import gc

def success_code(succcode):
    succcodes={
        'OK_FS_1':'Resource Folder Created Successfully',
        'OK_FS_2':'Resource Folder Removed Successfully',
        'OK_GC_1':'Garbage Collector Initiated Successfully'
    }
    data={succcode:succcodes[succcode]}
    return data
