import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'r') as fp:
    README_TEXT = fp.read()

setup(
    name = "pytest-trepan",
    version = '1.0.0',
    description = 'Pytest plugin for trepan debugger.',
    author = 'Rocky Bernstein',
    author_email = 'rocky@gnu.org',

    keywords=[
        'debugger', 'pytest', 'py.test', 'trepan',
    ],
    install_requires=[
        'pytest>=2.6.0',
        'trepan>=0.5.1'
    ],
    # the following makes a plugin available to pytest
    entry_points = {
        'pytest11': ['pytest_trepan = pytest_trepan'],
    },
    long_description = README_TEXT,
    zip_safe=False,
)
