# Theoretical vs Practical Performance Analysis

## Quick Sort
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²)

**Practical Observation:**  
Experimental results show that Quick Sort performs efficiently on partially sorted and reverse ordered data in the current implementation. This indicates that pivot selection strategy significantly affects real-world performance.

---

## Merge Sort
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

**Practical Observation:**  
Merge Sort demonstrates stable performance across all data patterns, consistent with its theoretical complexity. However, its higher memory usage was observed due to auxiliary array allocation.

---

## Heap Sort
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

**Practical Observation:**  
Heap Sort maintains consistent execution time across different data patterns but generally performs slower than Quick Sort due to higher constant factors.

---

## Shell Sort
- Best Case: O(n log n) (depends on gap sequence)
- Average Case: O(n^1.25) (approx.)
- Worst Case: O(n²)

**Practical Observation:**  
Shell Sort performs efficiently on partially sorted data, benefiting from reduced number of element movements.

---

## Radix Sort
- Best Case: O(nk)
- Average Case: O(nk)
- Worst Case: O(nk)

**Practical Observation:**  
Radix Sort shows competitive performance for integer datasets, though it requires additional memory for bucket-based processing.
