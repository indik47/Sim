import matplotlib.pyplot as plt


def plot_trajectory(df):

    plt.figure(figsize=(10, 6))

    plt.plot(df["x"], df["y"])

    plt.xlabel("Horizontal distance (m)")
    plt.ylabel("Altitude (m)")
    plt.grid(True)

    plt.axis("equal")

    plt.show()