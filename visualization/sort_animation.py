# ============================================
# visualization/sort_animation.py
# Generator-based Sorting Animation Logic
# ============================================

def quick_sort_animation_generator(arr):
    """
    Quick Sort algoritmasının animasyon için generator versiyonu.
    Her değişiklikte (swap) dizinin o anki durumunu 'yield' eder.
    Böylece GUI, her adımı tek tek çizebilir.
    """
    yield from _quick_sort_visual(arr, 0, len(arr) - 1)

def _quick_sort_visual(arr, low, high):
    if low < high:
        # Partition işleminden gelen yield'ları yukarı taşı
        pivot_index = yield from _partition_visual(arr, low, high)
        
        # Sol ve Sağ tarafları recursive çağır ve yield'ları ilet
        yield from _quick_sort_visual(arr, low, pivot_index - 1)
        yield from _quick_sort_visual(arr, pivot_index + 1, high)

def _partition_visual(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr  # SWAP gerçekleşti, yeni durumu gönder!
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr  # Pivot yerine oturdu, durumu gönder!
    
    return i + 1