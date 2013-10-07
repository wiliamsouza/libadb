AC_PREREQ([2.68])
LT_PREREQ([2.2])

AC_INIT([adblib], [0.1], [wiliamsouza83@gmail.com])
AM_INIT_AUTOMAKE
LT_INIT([dlopen])

AC_CONFIG_SRCDIR([src/libadb/libadb.c])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_CC
AC_PROG_INSTALL
AM_PROG_CC_C_O

AC_CONFIG_MACRO_DIR([m4])
AC_CHECK_HEADERS([])

# Checks for libraries.
# FIXME: Replace `main' with a function in `-lcrypto':
#AC_CHECK_LIB([crypto], [main])
# FIXME: Replace `main' with a function in `-ldl':
#AC_CHECK_LIB([dl], [main])
# FIXME: Replace `main' with a function in `-lpthread':
#AC_CHECK_LIB([pthread], [main])
# FIXME: Replace `main' with a function in `-lrt':
#AC_CHECK_LIB([rt], [main])


# Checks for header files.
#AC_CHECK_HEADERS([pthread.h
#		fcntl.h
#		inttypes.h
#		limits.h
#		malloc.h
#		netdb.h
#		netinet/in.h
#		stddef.h
#		stdint.h
#		stdlib.h
#		string.h
#		sys/ioctl.h
#		sys/mount.h
#		sys/socket.h
#		sys/time.h
#		termios.h
#		unistd.h])

AC_CONFIG_FILES([Makefile
		include/Makefile
		include/libadb/Makefile
		src/Makefile
		src/libadb/Makefile
		src/core/Makefile
		src/core/adb/Makefile
		src/core/libcutils/Makefile
		src/core/libzipfile/Makefile])
AC_OUTPUT

echo \
"-------------------------------------------------
${PACKAGE_NAME} Version ${PACKAGE_VERSION}
Prefix: '${prefix}'.
Compiler: '${CC} ${CFLAGS} ${CPPFLAGS}'
--------------------------------------------------"

