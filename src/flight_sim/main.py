from pathlib import Path
from flight_sim.analysis import metrics
from flight_sim.analysis.comparison import create_summary
from flight_sim.batch.runner import BatchRunner, generate_angle_sweep
from flight_sim.integrators.euler import EulerIntegrator
from flight_sim.core.state import State
from flight_sim.config import load_simulation_parameters
from flight_sim.simulation.logger import SimulationLogger
from flight_sim.simulation.simulator import Simulator
from flight_sim.visualisation.metrics_plot import plot_range_vs_angle
from flight_sim.visualisation.trajectory_plot import plot_multiple_trajectories, plot_trajectory
from flight_sim.analysis.metrics import compute_metrics
from flight_sim.optimization.optimizer import RangeOptimizer


def run_single(simulator, state, params):
    result = simulator.run(state, params)
    print(result.metrics)

    result.trajectory.to_csv("trajectory.csv", index=False)
    plot_trajectory(result.trajectory)


def run_batch(simulator, state, params):
    angles = range(15, 80)
    parameter_sets = generate_angle_sweep(params, angles)

    runner = BatchRunner(simulator)

    results = runner.run(state, parameter_sets)
    summary = create_summary(results)
    print(summary)

    summary.to_csv("batch_results.csv", index=False)

    plot_range_vs_angle(summary)
    plot_multiple_trajectories(results)


def run_optimization(simulator, state, params):
    optimizer = RangeOptimizer(
        simulator,
        state,
        params,
        target_range=1200.0,
    )

    result = optimizer.optimize()
    print(result)                                           

def main():
    state = State(
        x=0.0,
        y=0.0,
        vx=100.0,
        vy=100.0,
        mass=10.0,
    )

    params = load_simulation_parameters(Path("configs/baseline.yaml"))
    simulator = Simulator(EulerIntegrator())

    run_batch(simulator, state, params)

if __name__ == "__main__":
    main()