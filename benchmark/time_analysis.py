# ============================================
# benchmark/time_analysis.py
# Time measurement utilities
# ============================================

import time


def measure_time(sort_function, data: list, runs: int = 3) -> float:
    """
    Measures average execution time of a sorting function.

    :param sort_function: sorting function reference
    :param data: input list
    :param runs: number of repetitions
    :return: average time in milliseconds
    """
    total_time = 0.0

    for _ in range(runs):
        data_copy = data.copy()
        start = time.perf_counter()
        sort_function(data_copy)
        end = time.perf_counter()
        total_time += (end - start)

    avg_time_ms = (total_time / runs) * 1000
    return avg_time_ms
