========================
Android Debug Bridge lib
========================

Python ctypes wrapper to adb library.

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

    $ cp adb_Makefile.am core/adb/
    $ cp core_Makefile.am core/
    $ cp libcutils_Makefile.am core/libcutils/
    $ cp libzipfile_Makefile.am core/libzipfile/

To build the lib run::

    $ autoreconf
    $ ./configure
    $ make

The above command will generate an libadb.so at build directory.

Running
=======

Export environment variable pointing to your recent build library location::

   export ADB_LIBRARY_PATH=src/libadb/.libs/libadb.so

Now you can call the follow command from the project root directory::

   $ python python/adblib/adb.py

It's an `adb` clone written in python using 17 lines of code. 

