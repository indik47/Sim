from copy import deepcopy
from flight_sim.core.results import SimulationResult


def generate_angle_sweep(base_params, angles,) -> list:
    parameter_sets = []

    for angle in angles:
        params = deepcopy(base_params)
        params.thrust_angle_deg = angle
        parameter_sets.append(params)

    return parameter_sets


class BatchRunner:
    def __init__(self, simulator):
        self.simulator = simulator

    def run(self, initial_state, parameter_sets,) -> list[SimulationResult]:
        results = []

        for params in parameter_sets:
            result = self.simulator.run(
                initial_state,
                params,
            )

            results.append(result)

        return results