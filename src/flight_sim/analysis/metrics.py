import pandas as pd


def max_altitude(df: pd.DataFrame) -> float:
    return float(df["y"].max())


def max_speed(df: pd.DataFrame) -> float:
    speed = (df["vx"]**2 + df["vy"]**2) ** 0.5
    return float(speed.max())