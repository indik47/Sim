from .base import Integrator
from flight_sim.models.state import State
from flight_sim.models.parameters import SimulationParameters
from flight_sim.physics.dynamics import compute_acceleration


class EulerIntegrator(Integrator):

    def step(self, state: State, params: SimulationParameters, time: float) -> State:
        dt = params.dt

        acc = compute_acceleration(state, params, time)

        state.x += state.vx * dt
        state.y += state.vy * dt

        state.vx += acc[0] * dt
        state.vy += acc[1] * dt

        return state