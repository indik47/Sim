from copy import deepcopy
from flight_sim.analysis.metrics import compute_metrics
from flight_sim.core.results import SimulationResult
from flight_sim.simulation.logger import SimulationLogger


class Simulator:
    def __init__(self, integrator):
        self.integrator = integrator

    def run(self, initial_state, params)-> SimulationResult:
        logger = SimulationLogger()
        state = deepcopy(initial_state)
        time = 0.0

        while (time < params.max_time and state.y >= 0.0):
            logger.record(time, state)
            self.integrator.step(state, params, time)
            time += params.dt
        
        trajectory = logger.to_dataframe()
        metrics = compute_metrics(trajectory)

        return SimulationResult(parameters=params, trajectory=trajectory, metrics=metrics,)