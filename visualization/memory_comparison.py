# ============================================
# visualization/memory_comparison.py
# Memory usage comparison visualization
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_PATH = "results/memory_results.csv"
OUTPUT_DIR = "report/figures"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def plot_memory_comparison(data_size=10000, data_type="random"):
    df = pd.read_csv(CSV_PATH)

    # Filter data
    df = df[
        (df["Data Size"] == data_size) &
        (df["Data Type"] == data_type)
    ]

    algorithms = df["Algorithm"]
    memory_values = df["Memory (KB)"]

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, memory_values)

    plt.title(f"Memory Usage Comparison ({data_type.capitalize()} data, n={data_size})")
    plt.xlabel("Algorithm")
    plt.ylabel("Memory Usage (KB)")
    plt.xticks(rotation=20)
    plt.grid(axis="y")

    output_path = f"{OUTPUT_DIR}/memory_comparison_{data_type}_{data_size}.png"
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"[✓] Memory comparison plot saved: {output_path}")


if __name__ == "__main__":
    plot_memory_comparison(10000, "random")
