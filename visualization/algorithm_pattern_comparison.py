# ============================================
# visualization/algorithm_pattern_comparison.py
# Bonus: Algorithm vs Data Pattern comparison
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_PATH = "results/time_results.csv"
OUTPUT_DIR = "report/figures"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_algorithm_pattern_comparison(data_size=10000):
    df = pd.read_csv(CSV_PATH)

    df = df[df["Data Size"] == data_size]

    algorithms = df["Algorithm"].unique()
    patterns = ["random", "partial", "reverse"]

    plt.figure(figsize=(10, 6))

    for algo in algorithms:
        algo_df = df[df["Algorithm"] == algo]
        times = [
            algo_df[algo_df["Data Type"] == p]["Time (ms)"].values[0]
            for p in patterns
        ]
        plt.plot(patterns, times, marker="o", label=algo)

    plt.title(f"Algorithm vs Data Pattern Comparison (n={data_size})")
    plt.xlabel("Data Pattern")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.grid(True)

    output_path = f"{OUTPUT_DIR}/algorithm_pattern_comparison_{data_size}.png"
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"[✓] Bonus pattern comparison plot saved: {output_path}")


if __name__ == "__main__":
    plot_algorithm_pattern_comparison(10000)
