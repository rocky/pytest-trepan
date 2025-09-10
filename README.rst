Abstract
========


A pytest plugin for running the `trepan debugger <https://pypi.python.org/pypi/trepan3k>`_


Using
=====

After installing, to set a breakpoint to enter the trepan debugger::

    from pytest_trepan import debug
    def test_function():
        ...
        debug()    # get thee into the debugger!
        x = 1
        ...

The above will look like it is stopped at the *pytest.trepan()*
call. This is most useful when this is the last statement of a
scope. If you want to stop instead before ``x = 1`` pass ``immediate=False`` or just ``False``::

    from  pytest
    def test_function():
        ...
        debug(immediate=False)
	x = 1
	...

You can also pass as keyword arguments any parameter accepted by *trepan.api.debug()*.

To have the debugger entered on error, use the ``-s`` option::

    $ pytest -s ...



Project Details
===============

- Project code + issue track on github - https://github.com/rocky/pytest-trepan
- PyPI - https://pypi.python.org/pypi/pytest-trepan
