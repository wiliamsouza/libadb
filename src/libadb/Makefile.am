lib_LTLIBRARIES = libadb.la
libadb_la_SOURCES = libadb.c
libadb_la_CPPFLAGS = -I$(top_srcdir)/include \
		-I../core/include \
		-I../core/adb
libadb_la_LIBADD = ../core/adb/libadblib.a \
		../core/libcutils/libcutils.a \
		../core/libzipfile/libzipfile.a
