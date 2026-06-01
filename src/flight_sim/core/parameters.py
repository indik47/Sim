from dataclasses import dataclass


@dataclass
class SimulationParameters:
    gravity: float
    drag_coefficient: float
    thrust: float
    thrust_angle_deg: float
    burn_time: float
    dt: float
    max_time: float