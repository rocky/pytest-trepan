# -*- coding: utf-8 -*-

class Option(object):
    def __init__(self, no_trepan=False):
        self.no_trepan = no_trepan

    @property
    def args(self):
        if self.no_trepan:
            l = ['--pdb']
        else:
            l = ['--trepan']
        return l


def test_post_mortem(testdir):
    testdir.makepyfile(
        """
        def test_func():
            assert 0
        """
    )

    testdir.runpytest()
