#include <stdio.h>
#include <stdlib.h>

#include "libadb/libadb.h"

int main(int argc, char **argv) {
    const char *service = "host:devices";

    adb_trace_init();
    return adb_query(service);
}
