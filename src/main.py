from pathlib import Path
from flight_sim.models.state import State
from flight_sim.models.parameters import SimulationParameters
from flight_sim.config import load_simulation_parameters


def main():

    state = State(
        x=0.0,
        y=0.0,
        vx=100.0,
        vy=100.0,
        mass=10.0,
    )


    params = load_simulation_parameters(Path("configs/baseline.yaml"))


    print(state)
    print(params)


if __name__ == "__main__":
    main()