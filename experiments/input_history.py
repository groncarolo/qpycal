import cmd
import os.path
try:
    import readline
except ImportError:
    readline = None

histfile = os.path.expanduser('~/.qpycalc')
histfile_size = 1000

class QConsole(cmd.Cmd):
    def preloop(self):
        if readline and os.path.exists(histfile):
            readline.read_history_file(histfile)

    def postloop(self):
        print("postloop")
        if readline:
            readline.set_history_length(histfile_size)
            readline.write_history_file(histfile)

    def do_sim(self, arg):
        print("'" + arg + "'")

    def do_simjson(self, arg):
        print("'" + arg + "'")

    def do_EOF(self, args):
        return True



console = QConsole()
try:
    console.cmdloop()
except KeyboardInterrupt:
    print("")
