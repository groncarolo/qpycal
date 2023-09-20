import cmd
import logging
import os.path

from qjson import from_json_file
from qparser import parse_and_solve
from qvisualization import display_result

try:
    import readline
except ImportError:
    readline = None

history_file = os.path.expanduser('~/.qpycalc')
history_file_size = 1000


class QConsole(cmd.Cmd):
    intro = 'Welcome to the qpycal. order of gates is left -> bottom right -> top.\n'
    prompt = 'qpycal> '

    def preloop(self):
        '''
        if readline is enabled read history
        :return:
        '''
        if readline and os.path.exists(history_file):
            readline.read_history_file(history_file)

    def postloop(self):
        '''
        if readline is enabled save history
        :return:
        '''
        if readline:
            readline.set_history_length(history_file_size)
            readline.write_history_file(history_file)

    def do_json(self, arg):
        '''
        solve json defined circuit
        :param arg: json circuit
        :return:
        '''
        circuit, result = from_json_file(arg)
        ret, prob, in_len = parse_and_solve(circuit)
        display_result(ret, prob, in_len)

    def do_solve(self, arg):
        '''
        solve circuit
        :param arg: circuit
        :return:
        '''
        ret, prob, in_len = parse_and_solve(arg)
        display_result(ret, prob, in_len)

    def do_debug(self, arg):
        '''
        solve circuit showing all operations
        :param arg:
        :return:
        '''
        rootLogger = logging.getLogger()
        logFormatter = logging.Formatter("%(message)s")
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        consoleHandler.setLevel(logging.WARNING)
        rootLogger.addHandler(consoleHandler)
        self.do_solve(arg)
        rootLogger.removeHandler(consoleHandler)

    def do_help(self, arg):
        '''
        print help
        :param arg:
        :return:
        '''
        print("try typing")
        print("solve a circuit:")
        print("solve |0> X")
        print("")
        print("solve a circuit with comple liner algebra intermediary results:")
        print("debug |0> X")

    def do_EOF(self, args):
        return True
