from qiskit import QuantumCircuit


# number of qubits = 2
qc = QuantumCircuit(2, 2)

# hadamard gate
qc.h(0)
qc.cx(0, 1)

# measurement
qc.measure_all()