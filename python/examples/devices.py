from ctypes import create_string_buffer

from libadb import libadb


libadb.adb_trace_init()
print(libadb.adb_query(create_string_buffer(b'host:devices')))
