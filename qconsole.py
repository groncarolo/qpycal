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
HISTORY_FILE_SIZE = 1000


class Qconsole(cmd.Cmd):
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
            readline.set_history_length(HISTORY_FILE_SIZE)
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
        ret, prob, labels, in_len, = parse_and_solve(arg)
        display_result(ret, prob, labels, in_len)

    def do_debug(self, arg):
        '''
        solve circuit showing all operations
        :param arg:
        :return:
        '''
        root_logger = logging.getLogger()
        log_formatter = logging.Formatter("%(message)s")
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        console_handler.setLevel(logging.WARNING)
        root_logger.addHandler(console_handler)
        self.do_solve(arg)
        root_logger.removeHandler(console_handler)

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
