git pull

Check numversion in pytest/__init__.py
VERSION=1.0.0
git commit -m"Get ready for release $VERSION" .

Update ChangeLog:
  make ChangeLog

Update NEWS from ChangeLog
make check-short
git commit --amend .

Make sure pyenv is running
# Pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"


PYVERSIONS='3.3.5 3.4.1 3.4.2'

Test all python versions:
   for version in $PYVERSIONS; do pyenv local $version && make clean && make check-short; done

python setup.py register

for version in $PYVERSIONS; do pyenv local $version && make dist && python setup.py bdist_egg bdist_wheel upload; done

git tag release-$VERSION
git push --tags

bump version in trepan/VERSION.py - add '_01'
