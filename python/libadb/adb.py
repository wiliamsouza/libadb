from __future__ import unicode_literals

import sys

from ctypes import cdll
from ctypes import c_char_p

sys.argv.pop(0)
argc = len(sys.argv)
argv = (c_char_p * argc)()
for n in range(argc):
    argv[n] = sys.argv[n]

adblib = cdll.LoadLibrary('../../src/libadb/.libs/libadb.so')
adblib.adb_trace_init()
adblib.adb_commandline(argc, argv)
