from qgates import Identity, XGate, Ctrl, Gate


class CustomGate(Gate):
    gates = []

    def get_len(self):
        '''
        get length of custom gate
        :return:
        '''
        return len(self.gates)

    def get_height(self):
        '''
        get height of custom gate
        :return:
        '''
        return len(self.gates[0])

    def __init__(self, gates, label):
        super().__init__(None, label, True)
        self.gates = gates


def get_custom_gate(label):
    '''
    retrieve a custom gate by name
    :param label: label of custom gate
    :return: custom gate if found
    '''
    # left bottom
    # right top
    custom_gates = {"sum": CustomGate([[XGate(), Ctrl(), Identity()],
                                       [XGate(), Identity(), Ctrl()]], "sum")}
    g = custom_gates.get(label)
    return g
