'''`pytest-trepan` is a pytest_ plugin running the `trepan debugger
<https://pypi.python.org/pypi?:action=display&name=trepan>`_.

After installing, to set a breakpoint to enter the trepan debugger::

    import pytest
    def test_function():
        ...
         pytest.trepan()    # invoke
	 x = 1
	 ...

To have the debugger entered on error, use the `--trepan` option::

    $ py.test --trepan ...

'''

__docformat__ = 'restructuredtext'

version = '1.0.0'
__version__ = version
