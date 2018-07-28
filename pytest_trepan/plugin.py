""" interactive debugging with the Trepan Python Debugger. """
from __future__ import absolute_import
from trepan.api import debug as trepan_debug
from trepan.post_mortem import post_mortem as trepan_post_mortem
import sys

def pytest_addoption(parser):
    """Adds option --trepan to py.test"""
    group = parser.getgroup("general")
    group._addoption('--trepan',
                     action="store_true", dest="usetrepan", default=False,
                     help="start the trepan Python debugger on errors.")


def pytest_namespace():
    """Allows user code to insert pytest.trepan() to enter the trepan
    debugger.
    """
    return {'trepan': pytestTrepan().debug}


def pytest_configure(config):
    """Called to configure pytest when "pytest --trepan ... " is invoked"""
    if config.getvalue("usetrepan"):
        # 'pdbinvoke' is a magic name?
        config.pluginmanager.register(TrepanInvoke(), 'pdbinvoke')

    old = pytestTrepan._pluginmanager

    def fin():
        pytestTrepan._pluginmanager = old
        pytestTrepan._config = None
    pytestTrepan._pluginmanager = config.pluginmanager
    pytestTrepan._config = config
    config._cleanup.append(fin)


class pytestTrepan:
    """Pseudo Trepan that defers to the real trepan."""
    _pluginmanager = None
    _config = None

    def debug(self, immediate=False, *args, **kwargs):
        """invoke Trepan debugging, dropping any I/O capturing.
        If you want to stop at the call before the next statement, set
        immediate=True. Set immediate=False will stop just before the subsequent
        statement which sometimes might be in another scope.

        You can also pass trepan.debug options. In particular
        immediate=True is the the same as arguments: level=1, step_count=0,
        and will override setting those; immediate=False sets level=0,
        step_count=2
        """
        import _pytest.config
        capman = None
        if self._pluginmanager is not None:
            capman = self._pluginmanager.getplugin("capturemanager")
            if capman:
                capman.suspend_global_capture(in_=True)
            tw = _pytest.config.create_terminal_writer(self._config)
            tw.line()
            tw.sep(">", "Trepan set_trace (IO-capturing turned off)")
            self._pluginmanager.hook.pytest_enter_pdb()
        if immediate:
            kwargs['level'] = 1
            kwargs['step_ignore'] = 0
        else:
            if not 'level' in kwargs:
                kwargs['level'] = 0
            if not 'step_ignore' in kwargs:
                kwargs['step_ignore'] = 2
        trepan_debug(*args, **kwargs)


class TrepanInvoke:
    def pytest_exception_interact(self, node, call, report):
        capman = node.config.pluginmanager.getplugin("capturemanager")
        if capman:
            capman.suspend_global_capture(in_=True)
        _enter_trepan(node, call.excinfo, report)

    def pytest_internalerror(self, excrepr, excinfo):
        for line in str(excrepr).split("\n"):
            sys.stderr.write("INTERNALERROR> %s\n" % line)
            sys.stderr.flush()
        tb = _postmortem_traceback(excinfo)
        post_mortem(tb)


def _enter_trepan(node, excinfo, rep):
    # XXX we re-use the TerminalReporter's terminalwriter
    # because this seems to avoid some encoding related troubles
    # for not completely clear reasons.
    tw = node.config.pluginmanager.getplugin("terminalreporter")._tw
    tw.line()
    tw.sep(">", "traceback")
    rep.toterminal(tw)
    tw.sep(">", "entering Trepan")
    post_mortem(_postmortem_traceback(excinfo))
    rep._pdbshown = True
    return rep


def _postmortem_traceback(excinfo):
    # A doctest.UnexpectedException is not useful for post_mortem.
    # Use the underlying exception instead:
    from doctest import UnexpectedException
    if isinstance(excinfo.value, UnexpectedException):
        return excinfo.value.exc_info
    else:
        return excinfo._excinfo


def post_mortem(e):
    trepan_post_mortem(e)
