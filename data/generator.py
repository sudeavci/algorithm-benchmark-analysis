# ============================================
# data/generator.py
# Dataset generator for sorting algorithms
# ============================================

import random
import numpy as np


def generate_random(size: int) -> list:
    """
    Generates randomly ordered data.
    """
    return [random.randint(0, size * 10) for _ in range(size)]


def generate_reverse(size: int) -> list:
    """
    Generates reverse ordered data.
    """
    return list(range(size, 0, -1))


def generate_partially_sorted(size: int, sorted_ratio: float = 0.7) -> list:
    """
    Generates partially sorted data.
    sorted_ratio: percentage of the array that is already sorted
    """
    if not 0 < sorted_ratio < 1:
        raise ValueError("sorted_ratio must be between 0 and 1")

    sorted_part_size = int(size * sorted_ratio)
    sorted_part = list(range(sorted_part_size))
    random_part = [random.randint(0, size * 10) for _ in range(size - sorted_part_size)]

    return sorted_part + random_part


def generate_dataset(size: int, data_type: str) -> list:
    """
    Main dataset generator function.
    data_type: 'random', 'reverse', 'partial'
    """
    if data_type == "random":
        return generate_random(size)
    elif data_type == "reverse":
        return generate_reverse(size)
    elif data_type == "partial":
        return generate_partially_sorted(size)
    else:
        raise ValueError("Invalid data_type. Choose from: random, reverse, partial")

def generate_best_case(size: int):
    return list(range(size))

# Manual test
if __name__ == "__main__":
    print("Random:", generate_dataset(10, "random"))
    print("Reverse:", generate_dataset(10, "reverse"))
    print("Partial:", generate_dataset(10, "partial"))
