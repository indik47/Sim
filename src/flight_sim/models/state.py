from dataclasses import dataclass


@dataclass
class State:
    x: float
    y: float

    vx: float
    vy: float

    mass: float