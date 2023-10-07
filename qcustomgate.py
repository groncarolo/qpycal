from qgates import Identity, XGate, Ctrl, Gate, ACtrl


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

    custom_gates = {"cust": CustomGate([[XGate(), Ctrl(), Identity()],
                                        [XGate(), Identity(), Ctrl()]], "cust"),

                    "sum": CustomGate(
                        [[Identity(), Identity(), Identity(), Identity(), XGate(), Identity(), Ctrl(),
                          Identity()],
                         [Identity(), Identity(), Identity(), Identity(), XGate(), Ctrl(), Identity(),
                          Identity()],
                         [Identity(), Identity(), Identity(), XGate(), Ctrl(), Identity(), Identity(),
                          Identity()],
                         [Identity(), Identity(), Identity(), XGate(), Identity(), Identity(), Identity(),
                          Ctrl()],
                         [Identity(), Identity(), XGate(), Identity(), Identity(), Ctrl(), Ctrl(), Identity()],
                         [Identity(), XGate(), Identity(), Identity(), Ctrl(), Identity(), Identity(), Ctrl()],
                         [
                             XGate(), Identity(), Identity(), Identity(), Identity(), Identity(), Identity(),
                             Identity()],
                         [XGate(), ACtrl(), ACtrl(), Identity(), Identity(), Identity(), Identity(), Identity()],
                         [Identity(), XGate(), Identity(), Identity(), Ctrl(), Identity(), Identity(), Ctrl()],
                         [Identity(), Identity(), XGate(), Identity(), Identity(), Ctrl(), Ctrl(), Identity()],
                         [Identity(), Identity(), Identity(), Identity(), XGate(), Ctrl(), Identity(),
                          Identity()],
                         [
                             Identity(), Identity(), Identity(), Identity(), XGate(), Identity(), Ctrl(),
                             Identity()]],
                        "sum")}
    g = custom_gates.get(label)
    return g
