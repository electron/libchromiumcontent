#!/bin/bash

usage() {
    echo "Usage:" 1>&2
    echo "  $0 -o output.a input1.a [input2.a [...]]"
    exit
}

if [ "$1" != "-o" ]; then usage; fi
shift
DEST="$1"
shift
if [ $# = 0 ]; then usage; fi

SCRATCH="ar-combine.$$"
mkdir "$SCRATCH"

for LIB in "$@"; do
    if [ "`head -c7 "$LIB"`" = "!<thin>" ]; then
        ar t "$LIB" | while read OBJ; do
            cp "$OBJ" "$SCRATCH"
        done
    else
        LIB="`readlink -e "$LIB"`"
        (cd "$SCRATCH" ; ar x "$LIB")
    fi
done

ar rcs "$DEST" "$SCRATCH"/* > /dev/null 2>&1
rm -r "$SCRATCH"
