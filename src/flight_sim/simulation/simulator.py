from copy import deepcopy
from flight_sim.analysis.metrics import compute_metrics
from flight_sim.core.results import SimulationResult


class Simulator:
    def __init__(self, integrator, logger):
        self.integrator = integrator
        self.logger = logger

    def run(self, initial_state, params)-> SimulationResult:
        state = deepcopy(initial_state)
        time = 0.0

        while (time < params.max_time and state.y >= 0.0):
            self.logger.record(time, state)
            self.integrator.step(state, params, time)
            time += params.dt
        
        trajectory = self.logger.to_dataframe()
        metrics = compute_metrics(trajectory)

        return SimulationResult(trajectory=trajectory, metrics=metrics,)