from __future__ import unicode_literals

import logging
import os
import sys

from ctypes import cdll
from ctypes import c_char_p
from ctypes.util import find_library


logging.basicConfig()
logger = logging.getLogger('adblib.adblib')

lib_names = ['libadb.so', 'libadb.so.0', 'libadb.so.0.0.0']

for lib_name in lib_names:
    lib_path = find_library(lib_name)
    if not lib_path is None:
        break
try:
    lib_path = os.environ['ADB_LIBRARY_PATH']
except KeyError:
    lib_path = None

if lib_path is None:
    raise Exception('Could not find the ADB library (tried "%s"). '
                    'Try setting ADB_LIBRARY_PATH variable.' %
                    '", "'.join(lib_names))

sys.argv.pop(0)
argc = len(sys.argv)
argv = (c_char_p * argc)()
for n in range(argc):
    argv[n] = sys.argv[n]

adblib = cdll.LoadLibrary(lib_path)
adblib.adb_trace_init()

adblib.adb_commandline(argc, argv)

connect = 'host:connect:192.168.1.2:5555'
fd = adblib.adb_query(connect)
print fd

# adb.h
print(adblib.local_init)
print(adblib.local_connect)
print(adblib.local_connect_arbitrary_ports)

print(adblib.usb_init)
