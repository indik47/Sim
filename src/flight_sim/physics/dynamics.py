import numpy as np
from flight_sim.physics import forces
from flight_sim.models.state import State
from flight_sim.models.parameters import SimulationParameters

def compute_acceleration(state: State, params: SimulationParameters, time: float) -> np.ndarray:
    # Compute the net force acting on the object
    net_force = np.zeros(2)
    net_force = forces.gravity_force(state.mass, params.gravity)
    net_force += forces.drag_force(state.vx, state.vy, params.drag_coefficient)

    if time < params.burn_time:
        # Apply random thrust direction every 2 seconds
        #if (time // 2 == 0):  
        #    params.thrust_angle_deg = np.random.uniform(0, 90)

        net_force += forces.thrust_force(params)

    # Compute the acceleration using Newton's second law
    acceleration = net_force / state.mass

    return acceleration