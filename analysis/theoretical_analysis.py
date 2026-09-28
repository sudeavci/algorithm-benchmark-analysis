# ============================================
# analysis/theoretical_analysis.py
# --------------------------------------------
# This module contains ONLY theoretical
# (textbook-based) information about sorting
# algorithms. It is independent from benchmarking
# and execution.
# ============================================


# ------------------------------------------------
# Theoretical Time & Space Complexity Definitions
# ------------------------------------------------

THEORETICAL_INFO = {
    "Quick Sort": {
        "best_case": "O(n log n)",
        "average_case": "O(n log n)",
        "worst_case": "O(n^2)",
        "space_complexity": "In-place (O(log n) recursive stack)",
        "notes": (
            "Quick Sort performs best when the pivot divides the array "
            "into two nearly equal halves. Its worst case occurs when "
            "the pivot is consistently chosen as the smallest or largest element."
        )
    },

    "Merge Sort": {
        "best_case": "O(n log n)",
        "average_case": "O(n log n)",
        "worst_case": "O(n log n)",
        "space_complexity": "Extra memory O(n)",
        "notes": (
            "Merge Sort has stable and predictable performance because "
            "it always divides the array into equal halves, regardless "
            "of input order."
        )
    },

    "Heap Sort": {
        "best_case": "O(n log n)",
        "average_case": "O(n log n)",
        "worst_case": "O(n log n)",
        "space_complexity": "In-place O(1)",
        "notes": (
            "Heap Sort maintains its time complexity in all cases due "
            "to heap restructuring, but it does not preserve input order."
        )
    },

    "Shell Sort": {
        "best_case": "O(n log n)",
        "average_case": "O(n^1.5) (gap dependent)",
        "worst_case": "O(n^2)",
        "space_complexity": "In-place O(1)",
        "notes": (
            "Shell Sort's performance heavily depends on the gap sequence. "
            "With good gap choices, it significantly outperforms simple quadratic algorithms."
        )
    },

    "Radix Sort": {
        "best_case": "O(nk)",
        "average_case": "O(nk)",
        "worst_case": "O(nk)",
        "space_complexity": "Extra memory O(n + k)",
        "notes": (
            "Radix Sort is a non-comparison-based algorithm. Its performance "
            "depends on the number of digits (k) rather than direct element comparisons."
        )
    }
}


# ------------------------------------------------
# Helper Functions (Optional but Useful)
# ------------------------------------------------

def get_algorithm_names():
    """
    Returns a list of all available algorithm names.
    """
    return list(THEORETICAL_INFO.keys())


def get_theoretical_info(algorithm_name):
    """
    Returns theoretical information for a given algorithm.

    Parameters:
        algorithm_name (str): Name of the algorithm

    Returns:
        dict or None
    """
    return THEORETICAL_INFO.get(algorithm_name)


def format_theoretical_text(algorithm_name):
    """
    Formats theoretical information into a readable text block
    for GUI display.

    Parameters:
        algorithm_name (str): Name of the algorithm

    Returns:
        str
    """
    info = get_theoretical_info(algorithm_name)
    if not info:
        return "No theoretical information available."

    return (
        f"Algorithm: {algorithm_name}\n\n"
        f"Best Case:    {info['best_case']}\n"
        f"Average Case: {info['average_case']}\n"
        f"Worst Case:   {info['worst_case']}\n\n"
        f"Space Complexity:\n"
        f"{info['space_complexity']}\n\n"
        f"Notes:\n"
        f"{info['notes']}"
    )
