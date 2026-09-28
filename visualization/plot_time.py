# ============================================
# visualization/plot_time.py
# Time performance plots
# ============================================

import pandas as pd
import matplotlib.pyplot as plt


def plot_time_by_size(data_type: str):
    """
    Plots execution time vs data size for each algorithm
    for a given data type.
    """
    df = pd.read_csv("results/time_results.csv")
    df = df[df["Data Type"] == data_type]

    plt.figure()
    for algo in df["Algorithm"].unique():
        subset = df[df["Algorithm"] == algo]
        plt.plot(subset["Data Size"], subset["Time (ms)"], marker="o", label=algo)

    plt.xlabel("Data Size")
    plt.ylabel("Time (ms)")
    plt.title(f"Time Performance ({data_type.capitalize()} Data)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_time_by_size("reverse")

