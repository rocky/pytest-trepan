import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

trepan_version ='trepan3k'

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

def get_srcdir():
    filename = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
    return os.path.realpath(filename)

# version.py sets variable __version__.
__version__ = None
exec(open(os.path.join(get_srcdir(), 'pytest_trepan', 'version.py')).read())

setup(
    name="pytest-trepan",
    version=__version__,
    packages=['pytest_trepan'],
    entry_points={
        'pytest': ['trepan = pytest_trepan.plugin'],
    },
    install_requires=[
        'pytest<=4.6.3',  # Minimum version that removed pytest_namespace
        '%s>=1.0.0' % trepan_version
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Software Development :: Debuggers',
         "Framework :: Pytest",
    ],
    cmdclass={'test': PyTest},
)
