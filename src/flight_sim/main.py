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


def main():
    state = State(
        x=0.0,
        y=0.0,
        vx=100.0,
        vy=100.0,
        mass=10.0,
    )

    params = load_simulation_parameters(Path("configs/baseline.yaml"))
    angles = [i for i in range (15,80, 1)]
    parameter_sets = generate_angle_sweep(params,angles,)

    simulator = Simulator(EulerIntegrator())
    runner = BatchRunner(simulator)

    #result = simulator.run(state, params) #TODO: use returned results

    results = runner.run(state, parameter_sets)
    result = results[0] #TODO: loop through results

    #single run example
    # result.trajectory.save_csv(result.trajectory, "trajectory.csv")

    print(result.trajectory.tail())
    print(result.metrics)
    # plot_trajectory(result.trajectory)
    plot_multiple_trajectories(results)

    summary = create_summary(results)
    print(summary)
    # plot_range_vs_angle(summary)

    summary.to_csv(
        "batch_results.csv",
        index=False,
    )

if __name__ == "__main__":
    main()