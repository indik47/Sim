import matplotlib.pyplot as plt


def plot_trajectory(df):

    plt.figure(figsize=(10, 6))

    plt.plot(df["x"], df["y"])

    plt.xlabel("Horizontal distance (m)")
    plt.ylabel("Altitude (m)")
    plt.grid(True)

    plt.axis("equal")

    plt.show()


def plot_multiple_trajectories(results):
    plt.figure(figsize=(10, 6))

    while len(results) > 15:
        #plot every 5th trajectory to avoid clutter
        results = results[::5]

    for result in results:
        angle = result.parameters.thrust_angle_deg

        plt.plot(
            result.trajectory["x"],
            result.trajectory["y"],
            label=f"{angle}°",
        )

    plt.xlabel("Horizontal distance (m)")
    plt.ylabel("Altitude (m)")
    plt.title("Trajectory Comparison")

    plt.grid(True)
    plt.legend()
    plt.show()