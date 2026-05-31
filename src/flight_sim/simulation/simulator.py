class Simulator:

    def __init__(
        self,
        integrator,
        logger,
    ):
        self.integrator = integrator
        self.logger = logger

    def run(
        self,
        initial_state,
        params,
    ):
        pass