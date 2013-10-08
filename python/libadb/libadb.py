from __future__ import unicode_literals

import logging
import os

from ctypes import cdll
from ctypes.util import find_library


logger = logging.getLogger('libadb.libadb')

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

libadb = cdll.LoadLibrary(lib_path)
