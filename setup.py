import sys, re
from setuptools import setup
from setuptools.command.test import test as TestCommand


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


with open('pytest_trepan/__init__.py') as f:
    m = re.search("version = '(.*)'", f.read())
    assert m is not None
    version = m.group(1)

setup(
    name="pytest-trepan",
    version=version,
    packages=['pytest_trepan'],
    entry_points={
        'pytest11': ['pytest-qt = pytest_trepan.plugin'],
    },
    install_requires=[
        'pytest>=2.6.0',
        'trepan>=0.5.1'
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Debuggers',
    ],
    tests_requires=['pytest'],
    cmdclass={'test': PyTest},
)
