from qgates import Identity, XGate, Ctrl, Gate


class CustomGate(Gate):
    gates = []

    def get_len(self):
        return len(self.gates)

    def get_height(self):
        return len(self.gates[0])

    def __init__(self, gates, label):
        self.gates = gates
        self.label = label
        self.is_custom = True


def get_custom_gate(label):
    # left bottom
    # right top
    custom_gates = {"sum": CustomGate([[XGate(), Ctrl(), Identity()], [XGate(), Identity(), Ctrl()]], "sum")}
    g = custom_gates.get(label)
    return g
