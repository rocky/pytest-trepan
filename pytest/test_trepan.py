# -*- coding: utf-8 -*-
import pytest_trepan

pytest_plugins = "pytester"


class Option:
    def __init__(self, no_trepan=False):
        self.no_trepan = no_trepan

    @property
    def args(self) -> list:
        return ["--pdb"] if self.no_trepan else ["--trepan"]


def test_trepan_namespace_available():
    """Test that pytest.trepan is available after plugin loads"""
    assert hasattr(pytest, "trepan"), "pytest.trepan should be available"


def test_post_mortem(testdir):
    testdir.makepyfile(
        """
        def test_func():
            assert 0
        """
    )

    testdir.runpytest()
