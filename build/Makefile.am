LD=gcc
LDFLAGS=-static
LIBS=-lcrypto -lz -ldl -lrt -lpthread

all: adb libadb

libadb:
	gcc -o libadb.so *.o -shared -Wl,-soname,libadb.so $(LIBS)

adb:
	mv libadb.o libadb.obj
	$(LD) -o $@ $(LDFLAGS) *.o $(LIBS)
	mv libadb.obj libadb.o

clean:
	rm adb *.o *.so
