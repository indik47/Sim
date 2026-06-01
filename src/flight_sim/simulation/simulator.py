from copy import deepcopy


class Simulator:
    def __init__(self, integrator, logger):
        self.integrator = integrator
        self.logger = logger

    def run(self, initial_state, params):
        state = deepcopy(initial_state)
        time = 0.0

        while (time < params.max_time and state.y >= 0.0):
            self.logger.record(time, state)
            self.integrator.step(state, params, time)
            time += params.dt