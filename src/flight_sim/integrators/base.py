from abc import ABC, abstractmethod


class Integrator(ABC):

    @abstractmethod
    def step(self, state, params, time):
        pass