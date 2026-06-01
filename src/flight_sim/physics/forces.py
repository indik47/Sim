import numpy as np
from flight_sim.models.parameters import SimulationParameters
from flight_sim.models.state import State


def gravity_force(mass: float, g: float) -> np.ndarray:
    return np.array([0.0, -mass * g])


def drag_force(vx: float, vy: float, drag_coeff: float) -> np.ndarray:
    velocity = np.array([vx, vy])

    speed = np.linalg.norm(velocity)

    if speed < 1e-8:
        return np.zeros(2)

    return -drag_coeff * speed * velocity


def thrust_force(params: SimulationParameters) -> np.ndarray:
    angle = np.radians(params.thrust_angle_deg)

    return np.array([
        params.thrust * np.cos(angle),
        params.thrust * np.sin(angle),
    ])


def net_force(state: State, params: SimulationParameters, time: float,) -> np.ndarray:
    force = np.zeros(2)

    force += gravity_force(
        state.mass,
        params.gravity,
    )

    force += drag_force(
        state.vx,
        state.vy,
        params.drag_coefficient,
    )

    if time < params.burn_time:
        force += thrust_force(params)

    return force