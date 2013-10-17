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

    git clone https://github.com/wiliamsouza/libadb.git

It uses a git submodule, you must run this two commands:: 

    git submodule init
    git submodule update

Build
=====

Copy make files to android source code::

    cp src/core_Makefile.am src/core/Makefile.am
    cp src/adb_Makefile.am src/core/adb/Makefile.am
    cp src/libcutils_Makefile.am src/core/libcutils/Makefile.am
    cp src/libzipfile_Makefile.am src/core/libzipfile/Makefile.am

To build the lib run::

    autoreconf -vif
    ./configure
    make

The above command will generate an libadb.so at build directory.

Running
=======

Enable debug information::

    export ADB_TRACE=1

Python
------

Export environment variable pointing to your recent build library location::

    $ export ADB_LIBRARY_PATH=`pwd`/src/libadb/.libs/libadb.so

Set Python path to local copy o adblib python::

    $ export PYTHONPATH=`pwd`/python/:$PYTHONPATH

Now you can call the follow command from the project root directory::

    $ python python/examples/adb.py

It's an `adb` clone written in python using 3 lines of code. 

C
--

Export environment variable pointing to your recent build library location::

    export LD_LIBRARY_PATH=../`pwd`/src/libadb/.libs/:$LD_LIBRARY_PATH
    export LIBRARY_PATH=../`pwd`/src/libadb/.libs/:$LIBRARY_PATH

Compile::

    cd examples/
    gcc devices.c -I../include/ -ladb -L../src/libadb/.libs/ -o devices

Run::

    ./devices
