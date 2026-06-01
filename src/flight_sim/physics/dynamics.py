import numpy as np
from flight_sim.physics import forces
from flight_sim.models.state import State
from flight_sim.models.parameters import SimulationParameters

def compute_acceleration(state: State, params: SimulationParameters,) -> np.ndarray:
    # Compute the net force acting on the object
    net_force = np.zeros(2)
    net_force = forces.gravity_force(state.mass, params.gravity)
    net_force += forces.drag_force(state.vx, state.vy, params.drag_coefficient)

    # Compute the acceleration using Newton's second law
    acceleration = net_force / state.mass

    return acceleration