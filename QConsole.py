import cmd
import os.path

from qjson import from_json
from qparser import parse_and_calculate
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
        if readline and os.path.exists(history_file):
            readline.read_history_file(history_file)

    def postloop(self):
        if readline:
            readline.set_history_length(history_file_size)
            readline.write_history_file(history_file)

    def do_sim(self, arg):
        ret, in_len = parse_and_calculate(arg)
        display_result(ret, in_len)

    def do_simjson(self, arg):
        circuit, result = from_json(arg)
        ret, in_len = parse_and_calculate(circuit)
        display_result(ret, in_len)

    def do_help(self, arg):
        print("try sim |0> X")

    def do_EOF(self, args):
        return True
