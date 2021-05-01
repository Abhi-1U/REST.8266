import gc
import uasyncio as asyncio
from userver.server import WebServer,jsonify,parse_qs,start_response
router=WebServer()
#--Board LED Status
@router.route('/led/status')
def led_status(request , response):
    from interface.led import status
    yield from status(request,response)
#--Board LED Control
@router.route('/led/config')
def led_control(request , response):
    from interface.led import control
    yield from control(request,response)
#-- Cpu freq status
@router.route('/cpu/status')
def cpu_status(request , response):
    from interface.cpu import status
    yield from status(request,response)
#-- Cpu freq control
@router.route('/cpu/config')
def freq_control(request , response):
    from interface.cpu import config
    yield from config(request,response)
#-- Heap Memory status
@router.route('/heap/status')
def heap_status(request , response):
    from interface.memory import heap
    yield from heap(request,response)
#-- Stack Memory status
@router.route('/stack/status')
def stack_status(request , response):
    from interface.memory import stack
    yield from stack(request,response)

#-- Garbage Collector
@router.route('/garbage/collect')
def garbage_collect(request , response):
    from interface.memory import collect
    yield from collect(request,response)

#-- Device Software Details
@router.route('/device/software')
def dev_soft(request , response):
    from interface.device import software
    yield from software(request,response)

#-- Device Hardware Details
@router.route('/device/hardware')
def dev_hard(request , response):
    from interface.device import hardware
    yield from hardware(request,response)

#-- Device UID
@router.route('/device/uid')
def dev_uid(request , response):
    from interface.device import uid
    yield from uid(request,response)

#-- Network IfConfig
@router.route('/network/ifconfig')
def net_if(request , response):
    from interface.network import ifconfig
    yield from ifconfig(request,response)

#-- Network scan
@router.route('/network/scan')
def net_scan(request , response):
    from interface.network import scan
    yield from scan(request,response)

#-- Network status
@router.route('/network/status')
def net_stat(request , response):
    from interface.network import status
    yield from status(request,response)

#-- Network rssi
@router.route('/network/rssi')
def net_rssi(request , response):
    from interface.network import rssi
    yield from rssi(request,response)

#-- GPIO ReadADC
@router.route('/gpio/readadc')
def gpio_adc(request , response):
    from interface.gpio import adc
    yield from adc(request,response)
#--File System ls
@router.route('/fsys/ls')
def fsys_ls(request , response):
    from interface.fsys import ls
    yield from ls(request,response)
#-- Get cwd
@router.route('/fsys/getcwd')
def fsys_cwd(request , response):
    from interface.fsys import cwd
    yield from cwd(request,response)

#--File System chdir
@router.route('/fsys/chdir')
def fsys_chdir(request , response):
    from interface.fsys import chdir
    yield from chdir(request,response)

#--reset
@router.route('/device/reset')
def dev_reset(request , response):
    from interface.device import reset_dev
    yield from reset_dev(request,response)
#--web repl
@router.route('/device/webrepl')
def dev_webrepl(request , response):
    from interface.device import webrepl_mode
    yield from webrepl_mode(request,response)

#--clock time
@router.route('/clock/time')
def clock_time(request , response):
    from interface.clock import time
    yield from time(request,response)
#--clock ntpsync
@router.route('/clock/ntpsync')
def clock_ntpsync(request , response):
    from interface.clock import ntp_time
    yield from ntp_time(request,response)


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(asyncio.start_server(router.handle, '0.0.0.0', 80))
    gc.collect()
    loop.run_forever()

