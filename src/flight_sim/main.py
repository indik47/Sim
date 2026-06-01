from pathlib import Path
from flight_sim.analysis import metrics
from flight_sim.integrators.euler import EulerIntegrator
from flight_sim.models.state import State
from flight_sim.config import load_simulation_parameters
from flight_sim.simulation.logger import SimulationLogger
from flight_sim.simulation.simulator import Simulator
from flight_sim.visualisation.trajectory_plot import plot_trajectory
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

    logger = SimulationLogger()

    simulator = Simulator(EulerIntegrator(), logger)
    simulator.run(state, params)

    logger.save_csv("trajectory.csv")

    df = logger.to_dataframe()
    print(df.tail())

    metrics = compute_metrics(df)
    print(metrics)

    plot_trajectory(df)


if __name__ == "__main__":
    main()