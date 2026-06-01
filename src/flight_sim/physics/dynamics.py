import numpy as np
from flight_sim.physics import forces
from flight_sim.models.state import State
from flight_sim.models.parameters import SimulationParameters


def compute_acceleration(state: State, params: SimulationParameters, time: float) -> np.ndarray:
    # Compute the net force acting on the object
    net_force = forces.net_force(state, params, time)

    acceleration = net_force / state.mass

    return acceleration