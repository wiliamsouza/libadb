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
AC_CHECK_LIB([crypto], [EVP_CIPHER_CTX_init])
AC_CHECK_LIB([ssl], [SSL_CTX_new])
AC_CHECK_LIB([dl], [dlopen])
AC_CHECK_LIB([pthread], [pthread_create])
AC_CHECK_LIB([rt], [clock_gettime])


# Checks for header files.
AC_CHECK_HEADERS([pthread.h openssl/evp.h openssl/ssl.h fcntl.h inttypes.h limits.h malloc.h netdb.h netinet/in.h stddef.h stdint.h stdlib.h string.h sys/ioctl.h sys/mount.h sys/socket.h sys/time.h termios.h unistd.h])

AC_CONFIG_FILES([Makefile:Makefile.in
		include/Makefile:include/Makefile.in
		include/libadb/Makefile:include/libadb/Makefile.in
		src/Makefile:src/Makefile.in
		src/libadb/Makefile:src/libadb/Makefile.in
		src/core/Makefile:src/core/Makefile.in
		src/core/adb/Makefile:src/core/adb/Makefile.in
		src/core/libcutils/Makefile:src/core/libcutils/Makefile.in
		src/core/libzipfile/Makefile:src/core/libzipfile/Makefile.in])
AC_OUTPUT

echo \
"-------------------------------------------------
${PACKAGE_NAME} Version ${PACKAGE_VERSION}
Prefix: '${prefix}'.
Compiler: '${CC} ${CFLAGS} ${CPPFLAGS}'
--------------------------------------------------"

