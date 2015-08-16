Abstract
========


A pytest plugin for running the `trepan debugger <https://pypi.python.org/pypi?:action=display&name=trepan>`_


Using
=====

After installing, to set a breakpoint to enter the trepan debugger::

    import pytest
    def test_function():
        ...
         pytest.trepan()    # invoke
	 x = 1
	 ...


To have the debugger entered on error, use the `--trepan` option::

    $ py.test --trepan ...



Project Details
===============

- Project code + issue track on github - https://github.com/rocky/pytest-trepan
- PyPI - https://pypi.python.org/pypi/pytest-trepan
