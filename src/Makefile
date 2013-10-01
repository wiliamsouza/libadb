all:
	cp core_Makefile core/Makefile
	cp adb_Makefile core/adb/Makefile
	cp libcutils_Makefile core/libcutils/Makefile
	cp libzipfile_Makefile core/libzipfile/Makefile
	make -C libadb
	make -C core 

clean:
	make -C libadb clean
	make -C core clean
	rm core/Makefile
	rm core/adb/Makefile
	rm core/libcutils/Makefile
	rm core/libzipfile/Makefile
