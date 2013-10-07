SUBDIRS = src include

ACLOCAL_AMFLAGS = -I m4

Makefile: Makefile.am config.status
	./config.status $@

config.status: configure
	./config.status --recheck
