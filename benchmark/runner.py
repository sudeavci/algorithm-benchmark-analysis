# ============================================
# benchmark/runner.py
# Benchmark runner for sorting algorithms
# ============================================

import csv
import copy
from data.generator import generate_dataset
from benchmark.time_analysis import measure_time
from benchmark.memory_analysis import measure_memory

from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort
from algorithms.heap_sort import heap_sort
from algorithms.shell_sort import shell_sort
from algorithms.radix_sort import radix_sort


ALGORITHMS = {
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
    "Shell Sort": shell_sort,
    "Radix Sort": radix_sort,
}

DATA_SIZES = [1000, 10000, 100000]
DATA_TYPES = ["random", "partial", "reverse"]


def run_benchmark():
    time_results = []
    memory_results = []

    for size in DATA_SIZES:
        for data_type in DATA_TYPES:
            base_data = generate_dataset(size, data_type)

            for algo_name, algo_func in ALGORITHMS.items():

                # Radix Sort safety check
                if algo_name == "Radix Sort" and min(base_data) < 0:
                    continue

                data_for_time = copy.deepcopy(base_data)
                data_for_memory = copy.deepcopy(base_data)

                time_ms = measure_time(algo_func, data_for_time, runs=3)
                memory_kb = measure_memory(algo_func, data_for_memory)

                time_results.append([
                    algo_name,
                    size,
                    data_type,
                    round(time_ms, 4)
                ])

                memory_results.append([
                    algo_name,
                    size,
                    data_type,
                    round(memory_kb, 2)
                ])

                print(
                    f"{algo_name} | size={size} | type={data_type} | "
                    f"{time_ms:.2f} ms | {memory_kb:.2f} KB"
                )

    save_time_results(time_results)
    save_memory_results(memory_results)


def save_time_results(results):
    results_dir = os.path.join(os.path.dirname(__file__), "../results")
    os.makedirs(results_dir, exist_ok=True)
    with open(os.path.join(results_dir, "time_results.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Data Size", "Data Type", "Time (ms)"])
        writer.writerows(results)


def save_memory_results(results):
    results_dir = os.path.join(os.path.dirname(__file__), "../results")
    os.makedirs(results_dir, exist_ok=True)
    with open(os.path.join(results_dir, "memory_results.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Data Size", "Data Type", "Memory (KB)"])
        writer.writerows(results)
