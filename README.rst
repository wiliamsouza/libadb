========================
Android Debug Bridge lib
========================

ADB build system and Python ctypes wrapper to libadb.

Requirements
============

On ubuntu::

    $ sudo apt-get install zlib1g-dev

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

    $ cp src/adb_Makefile.am core/adb/
    $ cp src/core_Makefile.am core/
    $ cp src/libcutils_Makefile.am core/libcutils/
    $ cp src/libzipfile_Makefile.am core/libzipfile/

To build the lib run::

    $ autoreconf
    $ ./configure
    $ make

The above command will generate an libadb.so at build directory.

Running
=======

Export environment variable pointing to your recent build library location::

    $ export ADB_LIBRARY_PATH=`pwd`/src/libadb/.libs/libadb.so

Set Python path to local copy o adblib python::

    $ export PYTHONPATH=`pwd`python/:$PYTHONPATH

Now you can call the follow command from the project root directory::

    $ python python/examples/adb.py

It's an `adb` clone written in python using 3 lines of code. 




