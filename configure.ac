AC_PREREQ([2.68])
AC_INIT([adblib], [0.1], [wiliamsouza83@gmail.com])
AM_INIT_AUTOMAKE
LT_PREREQ([2.2])
LT_INIT([dlopen])
AC_PROG_CC
AC_PROG_INSTALL
AC_CONFIG_MACRO_DIR([m4])
AC_SEARCH_LIBS([pthread])
AC_CHECK_HEADERS([pthread.h])
AC_CONFIG_FILES([Makefile
		src/Makefile
		src/adblib/Makefile
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
Libs: '${LIBS}'

--------------------------------------------------"

