
from quantum_comm.simulation import QuantumCommunicationSimulator
from quantum_comm.analysis import analyze_efficiency, analyze_security, compare_to_classical
from quantum_comm.hybrid_protocol import HybridCommunicationProtocol

def main():
    print("Quantum Communication Project Simulation")
    
    # Initialize the simulator
    simulator = QuantumCommunicationSimulator()
    
    # Simulate quantum key distribution (QKD)
    print("\nSimulating QKD...")
    qkd_result = simulator.simulate_qkd()
    print("QKD simulation completed.")

    # Analyze the simulation results
    print("\nAnalyzing simulation results...")
    efficiency = analyze_efficiency(qkd_result)
    security = analyze_security(qkd_result)
    print(f"Efficiency: {efficiency}, Security: {security}")

    # Compare quantum communication with classical communication
    print("\nComparing to classical communication...")
    classical_results = {'efficiency': 0.8, 'security': 0.6}  # Placeholder values
    comparison = compare_to_classical(qkd_result, classical_results)
    print(f"Comparison: {comparison}")

    # Demonstrate hybrid communication protocol
    print("\nDemonstrating hybrid protocol...")
    hybrid_protocol = HybridCommunicationProtocol()
    hybrid_protocol.convert_quantum_to_classical('quantum_data')  # Placeholder data
    print("Hybrid protocol demonstrated.")

if __name__ == '__main__':
    main()
