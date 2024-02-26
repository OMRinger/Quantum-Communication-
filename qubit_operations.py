
from qiskit import QuantumCircuit

def create_entangled_pair():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    return circuit
