from copy import deepcopy
from scipy.optimize import minimize_scalar


class RangeOptimizer:
    def __init__(
        self,
        simulator,
        initial_state,
        base_params,
        target_range,
    ):
        self.simulator = simulator
        self.initial_state = initial_state
        self.base_params = base_params
        self.target_range = target_range


    def objective(self, angle_deg,):
        params = deepcopy(self.base_params)

        params.thrust_angle_deg = float(angle_deg)
        result = self.simulator.run(self.initial_state, params)

        error = abs(result.metrics.horizontal_range - self.target_range)

        return error
    
    def optimize(self):
        result = minimize_scalar(self.objective, bounds=(0.0, 90.0), method="bounded",)
        return result

    