import sys, re
from setuptools import setup
from setuptools.command.test import test as TestCommand

PYTHON3 = (sys.version_info >= (3, 0))
if PYTHON3:
    trepan_version ='trepan3k'
else:
    trepan_version = 'trepan2'

class PyTest(TestCommand):
    """
    Overrides setup "test" command, taken from here:
    http://pytest.org/latest/goodpractises.html
    """

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main([])
        sys.exit(errno)

import os
def get_srcdir():
    filename = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
    return os.path.realpath(filename)

# version.py sets variable VERSION.
VERSION = None
exec(open(os.path.join(get_srcdir(), 'pytest_trepan', 'version.py')).read())

setup(
    name="pytest-trepan",
    version=VERSION,
    packages=['pytest_trepan'],
    entry_points={
        'pytest11': ['pytest-qt = pytest_trepan.plugin'],
    },
    install_requires=[
        'pytest>=3.3.0',
        '%s>=0.8.7' % trepan_version
    ],
    zip_safe=False,

    # metadata for upload to PyPI
    author = 'Rocky Bernstein',
    author_email = 'rocky@gnu.org',
    description = 'Pytest plugin for trepan debugger.',
    long_description=open('README.rst').read(),
    keywords="debugger pytest trepan",
    url="http://github.com/rocky/pytest-trepan",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Debuggers',
    ],
    cmdclass={'test': PyTest},
)
