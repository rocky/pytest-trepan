#!/bin/bash
PACKAGE=pytest_trepan

# FIXME put some of the below in a common routine
function finish {
  cd $owd
}

owd=$(pwd)
cd $(dirname ${BASH_SOURCE[0]})
trap finish EXIT

if ! source ./pyenv-3.6-3.10-versions ; then
    exit $?
fi
if ! source ./setup-python-3.6.sh ; then
    exit $?
fi

./adm
cd ..
source $PACKAGE/version.py
echo $VERSION

for pyversion in $PYVERSIONS; do
    if ! pyenv local $pyversion ; then
	exit $?
    fi
    # pip bdist_egg create too-general wheels. So
    # we narrow that by moving the generated wheel.

    # Pick out first two number of version, e.g. 3.5.1 -> 35
    first_two=$(echo $pyversion | cut -d'.' -f 1-2 | sed -e 's/\.//')
    rm -fr build
    python setup.py bdist_egg bdist_wheel
    mv -v dist/${PACKAGE}-$VERSION-{py2.py3,py$first_two}-none-any.whl
done

python ./setup.py sdist
tarball=dist/${PYMODULE_NAME}-${__version__}.tar.gz
if [[ -f $tarball ]]; then
    mv -v $tarball dist/${PYMODULE_NAME}_36-${__version__}.tar.gz
fi
finish
