import numpy as np


def gravity_force(mass: float, g: float) -> np.ndarray:
    return np.array([0.0, -mass * g])


def drag_force(vx: float, vy: float, drag_coeff: float) -> np.ndarray:
    velocity = np.array([vx, vy])

    speed = np.linalg.norm(velocity)

    if speed < 1e-8:
        return np.zeros(2)

    return -drag_coeff * speed * velocity


def thrust_force(params):
    angle = np.radians(params.thrust_angle_deg)

    return np.array([
        params.thrust * np.cos(angle),
        params.thrust * np.sin(angle),
    ])