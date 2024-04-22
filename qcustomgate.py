from qgates import QGate, identity_gate, xgate, ctrl_gate, actrl_gate


class QCustomGate(QGate):
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
    pass

    custom_gates = {"cust": QCustomGate([[xgate(), ctrl_gate(), identity_gate()],
                                    [xgate(), identity_gate(), ctrl_gate()]], "cust"),

                "sum": QCustomGate(
                    [[identity_gate(), identity_gate(), identity_gate(), identity_gate(), xgate(), identity_gate(), ctrl_gate(), identity_gate()],
                     [identity_gate(), identity_gate(), identity_gate(), identity_gate(), xgate(), ctrl_gate(), identity_gate(), identity_gate()],
                     [identity_gate(), identity_gate(), identity_gate(), xgate(), ctrl_gate(), identity_gate(), identity_gate(), identity_gate()],
                     [identity_gate(), identity_gate(), identity_gate(), xgate(), identity_gate(), identity_gate(), identity_gate(), ctrl_gate()],
                     [identity_gate(), identity_gate(), xgate(), identity_gate(), identity_gate(), ctrl_gate(), ctrl_gate(), identity_gate()],
                     [identity_gate(), xgate(), identity_gate(), identity_gate(), ctrl_gate(), identity_gate(), identity_gate(), ctrl_gate()],
                     [ xgate(), identity_gate(), identity_gate(), identity_gate(), identity_gate(), identity_gate(), identity_gate(), identity_gate()],
                     [xgate(), actrl_gate(), actrl_gate(), identity_gate(), identity_gate(), identity_gate(), identity_gate(), identity_gate()],
                     [identity_gate(), xgate(), identity_gate(), identity_gate(), ctrl_gate(), identity_gate(), identity_gate(), ctrl_gate()],
                     [identity_gate(), identity_gate(), xgate(), identity_gate(), identity_gate(), ctrl_gate(), ctrl_gate(), identity_gate()],
                     [identity_gate(), identity_gate(), identity_gate(), identity_gate(), xgate(), ctrl_gate(), identity_gate(), identity_gate()],
                     [ identity_gate(), identity_gate(), identity_gate(), identity_gate(), xgate(), identity_gate(), ctrl_gate(), identity_gate()]],
                    "sum")}
    g = custom_gates.get(label)
    return g