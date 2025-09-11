#!/bin/bash
GITHUB_DIR=pytest_trepan
PYMODULE_NAME=pytest_trepan

# FIXME put some of the below in a common routine
function finish {
  cd $make_dist_pytest_trepan_owd
}

make_dist_pytest_trepan_owd=$(pwd)
cd $(dirname ${BASH_SOURCE[0]})
trap finish EXIT

if ! source ./pyenv-newest-versions ; then
    exit $?
fi
if ! source ./setup-master.sh ; then
    exit $?
fi

cd ..
source $GITHUB_DIR/version.py
echo $__version__
pyenv local 3.13

rm -fr build
pip wheel --wheel-dir=dist .
python -m build --sdist
finish
