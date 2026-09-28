# ============================================
# visualization/time_comparison.py
# Time performance comparison visualization
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_PATH = "results/time_results.csv"
OUTPUT_DIR = "report/figures"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_time_comparison(data_size=10000, data_type="random"):
    df = pd.read_csv(CSV_PATH)

    df = df[
        (df["Data Size"] == data_size) &
        (df["Data Type"] == data_type)
    ]

    plt.figure(figsize=(10, 6))

    for algo in df["Algorithm"].unique():
        algo_df = df[df["Algorithm"] == algo]
        plt.plot(
            [algo],              # tek nokta ama karşılaştırma için yeterli
            algo_df["Time (ms)"],
            marker="o",
            label=algo
        )

    plt.title(f"Time Comparison ({data_type.capitalize()} data, n={data_size})")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.grid(True)

    output_path = f"{OUTPUT_DIR}/time_comparison_{data_type}_{data_size}.png"
    plt.savefig(output_path)
    plt.close()

    print(f"[✓] Time comparison plot saved: {output_path}")


if __name__ == "__main__":
    plot_time_comparison(10000, "random")
