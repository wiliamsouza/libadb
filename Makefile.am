all:
	make -C src
	mv src/core/adb/*.o build/
	mv src/libadb/*.o build/
	mv src/core/libcutils/*.o build/
	mv src/core/libzipfile/*.o build/
	make -C build

clean:
	make -C src clean
	make -C build clean
