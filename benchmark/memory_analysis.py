# ============================================
# benchmark/memory_analysis.py
# Memory usage measurement utilities
# ============================================

import tracemalloc


def measure_memory(sort_function, data: list) -> float:
    """
    Measures peak memory usage of a sorting function.

    :param sort_function: sorting function reference
    :param data: input list
    :return: peak memory usage in KB
    """
    data_copy = data.copy()

    tracemalloc.start()
    sort_function(data_copy)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Convert bytes to KB
    peak_kb = peak / 1024
    return peak_kb
