import gc

def success_code(succcode):
    succcodes={
        'OK_FS_1':'Resource Folder Created',
        'OK_FS_2':'Resource Folder Removed',
        'OK_FS_3': 'Working Directory Changed',
        'OK_FS_4': 'File/Folder Renamed',
        'OK_FS_5': 'File Removed',
        'OK_GC_1':'Garbage Collector Initiated'
    }
    data={succcode:succcodes[succcode]}
    return data
