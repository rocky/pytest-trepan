#!/bin/bash
# Check out master branch and dependent development master branches
PYTHON_VERSION=3.12

bs=${BASH_SOURCE[0]}
if [[ $0 == $bs ]] ; then
    echo "This script should be *sourced* rather than run directly through bash"
    exit 1
fi

mydir=$(dirname $bs)
pytest_trepan_owd=$(pwd)
cd $mydir
. ./checkout_common.sh
(cd $mydir/../../../Trepan-Debuggers && \
     setup_version python3-trepan master
)
checkout_finish master
