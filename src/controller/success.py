import gc

def success_code(succcode):
    succcodes={
        'OK_FS_1':'Resource Folder Created',
        'OK_FS_2':'Resource Folder Removed',
        'OK_FS_3': 'Working Directory Changed',
        'OK_FS_4': 'File/Folder Renamed',
        'OK_FS_5': 'File Removed',
        'OK_GC_1':'Garbage Collector Initiated',
        'OK_IO_1':'GPIO Pin Initialized',
        'OK_IO_3':'PWM Initialized',
        'OK_IO_4':'PWM Deinitalized',
        'OK_WR_1':'WebREPL Initialized',
        'OK_WR_2':'WebREPL Code Changed'
    }
    data={succcode:succcodes[succcode]}
    return data
