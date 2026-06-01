import matplotlib.pyplot as plt


def plot_range_vs_angle(summary_df):
    plt.figure(figsize=(8, 5))

    plt.plot(
        summary_df["angle"],
        summary_df["range"],
        marker="o",
    )

    plt.xlabel("Thrust angle (deg)")
    plt.ylabel("Range (m)")
    plt.grid(True)

    plt.show()