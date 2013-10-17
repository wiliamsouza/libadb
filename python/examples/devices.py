from libadb import libadb


libadb.adb_trace_init()
print(libadb.adb_query('host:devices'))
