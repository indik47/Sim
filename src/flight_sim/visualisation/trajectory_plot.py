import matplotlib.pyplot as plt


def plot_trajectory(df):

    plt.figure(figsize=(10, 6))

    plt.plot(
        df["x"],
        df["y"],
    )

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.grid(True)

    plt.show()