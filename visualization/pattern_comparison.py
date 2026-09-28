# ============================================
# visualization/pattern_comparison.py
# Data pattern comparison visualization
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_PATH = "results/time_results.csv"
OUTPUT_DIR = "report/figures"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_pattern_comparison(algorithm="Quick Sort", data_size=10000):
    df = pd.read_csv(CSV_PATH)

    df = df[
        (df["Algorithm"] == algorithm) &
        (df["Data Size"] == data_size)
    ]

    patterns = df["Data Type"]
    times = df["Time (ms)"]

    plt.figure(figsize=(8, 5))
    plt.plot(patterns, times, marker="o")

    plt.title(f"{algorithm} - Data Pattern Comparison (n={data_size})")
    plt.xlabel("Data Pattern")
    plt.ylabel("Time (ms)")
    plt.grid(True)

    output_path = f"{OUTPUT_DIR}/pattern_comparison_{algorithm.replace(' ', '_')}_{data_size}.png"
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"[✓] Pattern comparison plot saved: {output_path}")


if __name__ == "__main__":
    plot_pattern_comparison("Quick Sort", 10000)
