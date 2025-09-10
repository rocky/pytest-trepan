"""
This is an example showing the use of the pytest_trepan modules
"""
from pytest_trepan import debug

def test_function():
    debug()    # get thee into the debugger!
    x = 1
    assert x == 1
