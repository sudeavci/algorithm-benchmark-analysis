# ============================================
# algorithms/quick_sort.py
# Optimized Quick Sort (Hybrid + Tail Call Opt)
# ============================================

import random

def quick_sort(arr: list) -> list:
    """
    Optimize Edilmiş Quick Sort (Hybrid Yaklaşım)
    - Küçük parçalar (size < 10) için Insertion Sort kullanır.
    - Tail Call Optimization benzeri mantıkla Stack derinliğini korur.
    """
    # Orijinal veriyi korumak için kopya al
    arr_copy = arr.copy()
    _quick_sort_optimized(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

def _insertion_sort_range(arr: list, low: int, high: int):
    """Küçük alt diziler için Insertion Sort (Daha hızlıdır)"""
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def _quick_sort_optimized(arr: list, low: int, high: int):
    """
    Recursion derinliğini azaltmak için while döngüsü ve 
    Insertion Sort eşiği kullanan ana fonksiyon.
    """
    while low < high:
        # OPTİMİZASYON 1: Dizi boyutu 10'dan küçükse Insertion Sort kullan ve döngüden çık
        if high - low < 10:
            _insertion_sort_range(arr, low, high)
            break
        
        # Pivot seçimi
        pivot_index = _random_partition(arr, low, high)
        
        # OPTİMİZASYON 2: Stack derinliğini minimize et (Tail Call Optimization Simulation)
        # Önce küçük olan tarafı recursive çağır, büyük tarafı while döngüsüyle hallet.
        if pivot_index - low < high - pivot_index:
            _quick_sort_optimized(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            _quick_sort_optimized(arr, pivot_index + 1, high)
            high = pivot_index - 1

def _random_partition(arr: list, low: int, high: int) -> int:
    # Rastgele pivot seçimi (Worst-case O(n^2) ihtimalini düşürür)
    rand_idx = random.randint(low, high)
    arr[low], arr[rand_idx] = arr[rand_idx], arr[low]
    
    pivot = arr[low]
    i = low + 1
    j = high

    # Hoare Partition Scheme benzeri (Lomuto'dan daha az swap yapar)
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

# Manual test
if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", sample)
    print("Sorted:", quick_sort(sample))