from dataclasses import dataclass
import pandas as pd
from flight_sim.analysis.metrics import SimulationMetrics


@dataclass
class SimulationResult:
    trajectory: pd.DataFrame
    metrics: SimulationMetrics