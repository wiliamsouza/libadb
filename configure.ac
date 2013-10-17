AC_PREREQ([2.68])
LT_PREREQ([2.2])

AC_INIT([adblib], [0.1], [wiliamsouza83@gmail.com])
AM_INIT_AUTOMAKE
LT_INIT([dlopen])

AC_CONFIG_SRCDIR([config.h.in])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_CXX
AC_PROG_AWK
AC_PROG_CC
AM_PROG_CC_C_O
AC_PROG_CPP
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AC_PROG_RANLIB
AC_CONFIG_MACRO_DIR([m4])
AC_CHECK_HEADERS([])

# Checks for libraries.
AC_CHECK_LIB([crypto], [EVP_CIPHER_CTX_init])
AC_CHECK_LIB([ssl], [SSL_CTX_new])
AC_CHECK_LIB([dl], [dlopen])
AC_CHECK_LIB([pthread], [pthread_create])
AC_CHECK_LIB([rt], [clock_gettime])


# Checks for header files.
AC_HEADER_RESOLV
AC_CHECK_HEADERS([arpa/inet.h fcntl.h inttypes.h limits.h memory.h netdb.h netinet/in.h stddef.h stdint.h stdlib.h string.h strings.h sys/ioctl.h sys/mount.h sys/socket.h sys/time.h termios.h unistd.h utime.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_HEADER_STDBOOL
AC_TYPE_UID_T
AC_C_INLINE
AC_TYPE_INT32_T
AC_TYPE_INT64_T
AC_TYPE_MODE_T
AC_TYPE_OFF_T
AC_TYPE_PID_T
AC_TYPE_SIZE_T
AC_TYPE_SSIZE_T
AC_CHECK_MEMBERS([struct stat.st_rdev])
AC_TYPE_UINT16_T
AC_TYPE_UINT32_T
AC_TYPE_UINT64_T
AC_TYPE_UINT8_T
AC_CHECK_TYPES([ptrdiff_t])

# Checks for library functions.
AC_FUNC_ALLOCA
AC_FUNC_CHOWN
AC_FUNC_FORK
AC_FUNC_FSEEKO
AC_FUNC_LSTAT_FOLLOWS_SLASHED_SYMLINK
AC_HEADER_MAJOR
AC_FUNC_MALLOC
AC_FUNC_REALLOC
AC_CHECK_FUNCS([atexit bzero clock_gettime dup2 ftruncate getcwd gethostbyname gethostname gettimeofday localtime_r memmove memset mkdir putenv select setenv socket strchr strdup strerror strndup strpbrk strrchr strstr strtol strtoul strtoull tzset utime])

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

