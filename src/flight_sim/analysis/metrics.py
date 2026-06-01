import pandas as pd
import numpy as np
from dataclasses import dataclass

@dataclass
class SimulationMetrics:
    flight_time: float
    max_altitude: float
    max_speed: float
    horizontal_range: float


def compute_metrics(df: pd.DataFrame) -> SimulationMetrics:

    speed = np.sqrt(
        df["vx"] ** 2 +
        df["vy"] ** 2
    )

    return SimulationMetrics(
        flight_time=float(df["time"].max()),
        max_altitude=float(df["y"].max()),
        max_speed=float(speed.max()),
        horizontal_range=float(df["x"].max()),
    )