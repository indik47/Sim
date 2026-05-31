from .base import Integrator


class EulerIntegrator(Integrator):

    def step(self, state, params, time):
        raise NotImplementedError