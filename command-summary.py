import logging
import os
from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.command-summary')

class CommandSummary(Plugin):
    """
    Will print the commands necessary to rerun just the failing/erroring tests at end of printout.
    """
    name = 'command-summary'
    enabled = False

    def options(self, parser, env=os.environ):
        super(CommandSummary, self).options(parser, env=env)

    def configure(self, options, conf):
        super(CommandSummary, self).configure(options, conf)
        if not self.enabled:
            return
        self._error_command_summary = []
        self._fail_command_summary = []

    def addError(self, test, err):
        self._error_command_summary.append(test.address())

    def addFailure(self, test, err):
        self._fail_command_summary.append(test.address())

    def report(self, stream):
        if not self.enabled:
            return
        stream.writeln("Commands for tests with errors:")
        for test_command in self._error_command_summary:
            stream.writeln(test_command)
        stream.writeln("Commands for tests with failed assertions:")
        for test_command in self._fail_command_summary:
            stream.writeln(test_command)

