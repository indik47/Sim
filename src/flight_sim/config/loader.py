from pathlib import Path
import yaml

from flight_sim.models.parameters import SimulationParameters


def load_simulation_parameters(
    config_path: str | Path,) -> SimulationParameters:

    with open(config_path, "r") as f:
        data = yaml.safe_load(f)

    return SimulationParameters(**data)