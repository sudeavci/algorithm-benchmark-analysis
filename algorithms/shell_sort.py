# ============================================
# algorithms/shell_sort.py
# Optimized Shell Sort (Knuth Sequence)
# ============================================

def shell_sort(arr: list) -> list:
    """
    Optimize Edilmiş Shell Sort
    - Standart Shell dizisi (n/2) yerine Knuth Dizisi (3x+1) kullanır.
    - Karmaşıklığı O(n^2)'den O(n^1.5)'e indirir.
    - Partially sorted verilerde çok hızlıdır.
    """
    # Orijinal veriyi korumak için kopya al
    arr_copy = arr.copy()
    n = len(arr_copy)

    # 1. Knuth Dizisi ile başlangıç aralığını (gap) belirle
    # Dizi: 1, 4, 13, 40, 121, 364...
    # Formül: h = 3*h + 1
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1

    # 2. Aralığı daraltarak sıralama yap
    while gap > 0:
        # Gap'li Insertion Sort uygula
        for i in range(gap, n):
            temp = arr_copy[i]
            j = i
            
            # Gap kadar geriye giderek karşılaştır ve kaydır
            while j >= gap and arr_copy[j - gap] > temp:
                arr_copy[j] = arr_copy[j - gap]
                j -= gap
            
            arr_copy[j] = temp
        
        # Bir sonraki adım için aralığı küçült (Ters işlem)
        gap //= 3

    return arr_copy


# Manual test
if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", sample)
    print("Sorted:", shell_sort(sample))