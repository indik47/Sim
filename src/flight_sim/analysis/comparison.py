import pandas as pd

from flight_sim.visualisation.trajectory_plot import plot_trajectory


def create_summary(results):
    rows = []

    for result in results:

        rows.append(
            {
                "angle": result.parameters.thrust_angle_deg,
                "range": result.metrics.horizontal_range,
                "altitude": result.metrics.max_altitude,
                "flight_time": result.metrics.flight_time,
            }
        )
        # overlay trajectories for visual comparison
        # plot_trajectory(result.trajectory)
        

    return pd.DataFrame(rows)