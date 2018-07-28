<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Get latest sources:](#get-latest-sources)
- [Change version in pytest/__init__.py:](#change-version-in-pytestinitpy)
- [Update ChangeLog:](#update-changelog)
- [Update NEWS from ChangeLog:](#update-news-from-changelog)
- [Make sure pyenv is running and check newer versions](#make-sure-pyenv-is-running-and-check-newer-versions)
- [Check RST](#check-rst)
- [Make packages and tag](#make-packages-and-tag)
- [Upload single package and look at Rst Formating](#upload-single-package-and-look-at-rst-formating)
- [Upload rest of versions](#upload-rest-of-versions)
- [Push tags:](#push-tags)

<!-- markdown-toc end -->
# Get latest sources:

    $ git pull

# Change version in pytest/__init__.py:

    $ emacs pytest_trepan/version.py
    $ source pytest_trepan/version.py
    $ echo $VERSION
    $ git commit -m"Get ready for release $VERSION" .

# Update ChangeLog:

    $ make ChangeLog

#  Update NEWS from ChangeLog:

    $ make check
    $ git commit --amend .
    $ git push # get CI testing going early

# Make sure pyenv is running and check newer versions

    $ pyenv local && source admin-tools/check-versions.sh

# Check RST

     http://rst.ninjs.org

# Make packages and tag

    $ . ./admin-tools/make-dist.sh
    $ git tag release-$VERSION


# Upload single package and look at Rst Formating

    $ twine upload dist/pytest_trepan-${VERSION}-py3.4.egg

# Upload rest of versions

    $ twine upload dist/pytest_trepan-${VERSION}*

# Push tags:

    $ git push --tags
