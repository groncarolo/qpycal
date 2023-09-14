def display_circuit(states, gates):
    for i in reversed(range(len(states))):
        print(states[i].label, end="")
        print(" ", end="")
        for j in reversed(range(len(gates))):
            print(gates[j][i].label, end="")
            print(" ", end="")
        print("")
