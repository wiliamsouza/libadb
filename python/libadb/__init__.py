from __future__ import unicode_literals

import logging

from ctypes import c_char_p

from libadb import libadb

logger = logging.getLogger('libadb')


def parse_argc_argv(sys_argv):
    ''' Transform a python argv in a c argc argv. '''
    sys_argv.pop(0)
    argc = len(sys_argv)
    argv = (c_char_p * argc)()
    for n in range(argc):
        argv[n] = sys_argv[n]
    return argc, argv


def adb(sys_argv):
    argc, argv = parse_argc_argv(sys_argv)
    libadb.adb_trace_init()
    libadb.adb_commandline(argc, argv)
