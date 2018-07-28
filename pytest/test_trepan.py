# -*- coding: utf-8 -*-

pytest_plugins = "pytester"


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


def pytest_generate_tests(metafunc):
    if "option" in metafunc.fixturenames:
        metafunc.addcall(id="default",
                         funcargs={'option': Option(no_trepan=False)})
        metafunc.addcall(id="no_trepan",
                         funcargs={'option': Option(no_trepan=True)})


def test_post_mortem(testdir, option):
    testdir.makepyfile(
        """
        def test_func():
            assert 0
        """
    )

    result = testdir.runpytest(*option.args)

    if option.no_trepan:
        print(result)
    else:
        print(result)
