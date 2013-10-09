========================
Android Debug Bridge lib
========================

ADB build system and Python ctypes wrapper to libadb.

Requirements
============

On ubuntu::

    sudo apt-get install autoconf
    sudo apt-get install libtool
    sudo apt-get install zlib1g-dev
    sudo apt-get install libssl-dev

Cloning
=======

Just run::

    $ git clone https://github.com/wiliamsouza/adblib.git

It uses a git submodule, you must run this two commands:: 

    $ git submodule init
    $ git submodule update

Build
=====

Copy make files to android source code::

    cp src/core_Makefile.am src/core/Makefile.am
    cp src/adb_Makefile.am src/core/adb/Makefile.am
    cp src/libcutils_Makefile.am src/core/libcutils/Makefile.am
    cp src/libzipfile_Makefile.am src/core/libzipfile/Makefile.am
    cp src/core_Makefile.in src/core/Makefile.in
    cp src/adb_Makefile.in src/core/adb/Makefile.in
    cp src/libcutils_Makefile.in src/core/libcutils/Makefile.in
    cp src/libzipfile_Makefile.in src/core/libzipfile/Makefile.in

To build the lib run::

    $ aclocal
    $ autoconf
    $ autoreconf
    $ ./configure
    $ make

The above command will generate an libadb.so at build directory.

Running
=======

Export environment variable pointing to your recent build library location::

    $ export ADB_LIBRARY_PATH=`pwd`/src/libadb/.libs/libadb.so

Set Python path to local copy o adblib python::

    $ export PYTHONPATH=`pwd`/python/:$PYTHONPATH

Now you can call the follow command from the project root directory::

    $ python python/examples/adb.py

It's an `adb` clone written in python using 3 lines of code. 




