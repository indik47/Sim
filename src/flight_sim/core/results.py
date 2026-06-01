from dataclasses import dataclass
import pandas as pd
from flight_sim.analysis.metrics import SimulationMetrics
from flight_sim.core.parameters import SimulationParameters


@dataclass
class SimulationResult:
    parameters: SimulationParameters
    trajectory: pd.DataFrame
    metrics: SimulationMetrics