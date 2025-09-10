"""
This is an example showing the use of the pytest_trepan modules
"""
import pytest


def test_function():
    pytest.trepan()    # get thee into the debugger!
    x = 1
    assert x == 1
