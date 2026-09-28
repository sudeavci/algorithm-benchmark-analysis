# ============================================
# algorithms/heap_sort.py
# Optimized Iterative Heap Sort implementation
# ============================================

def heap_sort(arr: list) -> list:
    """
    Optimize Edilmiş Heap Sort (Iterative)
    - Recursive heapify yerine iterative yaklaşım kullanır.
    - Python'daki Recursion Limit hatasını engeller.
    - Büyük veri setlerinde (100k+) daha performanslıdır.
    """
    # Orijinal veriyi bozmamak için kopya üzerinde çalış
    arr_copy = arr.copy()
    n = len(arr_copy)

    # 1. Max Heap İnşa Et (Sondan başa doğru)
    # n//2 - 1 en son yaprak olmayan düğümdür.
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(arr_copy, n, i)

    # 2. Elemanları sırayla çek (Extract Max)
    for i in range(n - 1, 0, -1):
        # Kökü (en büyüğü) sona at
        arr_copy[0], arr_copy[i] = arr_copy[i], arr_copy[0]
        # Kökü tekrar düzelt (Heapify) - ama sadece kalan kısım için
        _sift_down(arr_copy, i, 0)

    return arr_copy


def _sift_down(arr: list, n: int, i: int) -> None:
    """
    Recursive heapify yerine Iterative (Döngüsel) yaklaşım.
    Bellek dostudur ve stack taşması yapmaz.
    """
    largest = i
    
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Sol çocuk var mı ve kökten büyük mü?
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        # Sağ çocuk var mı ve şu anki en büyükten büyük mü?
        if right < n and arr[right] > arr[largest]:
            largest = right
            
        # Eğer en büyük eleman kök değilse, yer değiştir ve devam et
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest  # Recursive çağrı yerine indeksi güncelle
        else:
            # Heap özelliği sağlandı, döngüden çık
            break
        