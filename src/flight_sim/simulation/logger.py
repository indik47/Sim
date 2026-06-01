import pandas as pd


class SimulationLogger:
    def __init__(self):
        self.rows = []

    def record(self, time, state):
        self.rows.append(
            {
                "time": time,
                "x": state.x,
                "y": state.y,
                "vx": state.vx,
                "vy": state.vy,
            }
        )

    def to_dataframe(self):
        return pd.DataFrame(self.rows)
    
    def save_csv(self, path):
        self.to_dataframe().to_csv(path, index=False)