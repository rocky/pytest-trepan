#!/bin/bash
# Check out 3.6-to-3.10 branch and dependent development branches
PYTHON_VERSION=3.6

bs=${BASH_SOURCE[0]}
if [[ $0 == $bs ]] ; then
    echo "This script should be *sourced* rather than run directly through bash"
    exit 1
fi

export PATH=$HOME/.pyenv/bin/pyenv:$PATH
pytest_trepan_owd=$(pwd)
mydir=$(dirname $bs)
cd $mydir
. ./checkout_common.sh
(cd $mydir/../../../Trepan-Debuggers && \
     setup_version python3-trepan python-3.6
)

checkout_finish python-3.6-to-3.10
