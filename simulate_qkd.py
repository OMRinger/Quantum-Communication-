
from quantum_comm.simulation import QuantumCommunicationSimulator
from quantum_comm.analysis import analyze_security

def simulate_qkd_example():
    simulator = QuantumCommunicationSimulator()
    entangled_pair = simulator.simulate_qkd()
    print("QKD Simulation complete.")

    security_analysis = analyze_security(entangled_pair)
    print("Security Analysis:", security_analysis)

if __name__ == "__main__":
    simulate_qkd_example()
