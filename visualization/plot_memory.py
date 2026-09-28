# ============================================
# visualization/plot_memory.py
# Memory usage plots
# ============================================

import pandas as pd
import matplotlib.pyplot as plt


def plot_memory_by_algorithm(data_size: int, data_type: str):
    df = pd.read_csv("results/memory_results.csv")
    df = df[
        (df["Data Size"] == data_size) &
        (df["Data Type"] == data_type)
    ]

    # In-place bilgisini ekle
    inplace_algorithms = ["Quick Sort", "Heap Sort", "Shell Sort"]
    colors = [
        "green" if algo in inplace_algorithms else "red"
        for algo in df["Algorithm"]
    ]

    plt.figure()
    plt.bar(df["Algorithm"], df["Memory (KB)"], color=colors)

    plt.xlabel("Algorithm")
    plt.ylabel("Memory Usage (KB)")
    plt.title(
        f"Memory Usage Comparison (In-place vs Non-in-place)\n"
        f"{data_size} elements, {data_type.capitalize()} data"
    )

    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show(block=True)


if __name__ == "__main__":
    plot_memory_by_algorithm(100000, "random")


