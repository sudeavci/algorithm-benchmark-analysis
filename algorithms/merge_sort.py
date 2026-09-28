# ============================================
# algorithms/merge_sort.py
# Optimized Merge Sort implementation
# ============================================

def merge_sort(arr: list) -> list:
    """
    Optimize Edilmiş Merge Sort
    - Slicing yerine indeks tabanlı yönetim (Bellek tasarrufu).
    - 'Already Sorted' kontrolü (Best case performans artışı).
    """
    # Orijinal veriyi korumak için tek bir kopya alıyoruz
    arr_copy = arr.copy()
    
    # Yardımcı fonksiyonu (in-place mantığıyla) çağır
    if len(arr_copy) > 1:
        _merge_sort_helper(arr_copy, 0, len(arr_copy) - 1)
        
    return arr_copy

def _merge_sort_helper(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        
        # Recursive çağrılar (Slicing YOK, sadece indeks geçiyoruz)
        _merge_sort_helper(arr, left, mid)
        _merge_sort_helper(arr, mid + 1, right)
        
        # Birleştirme işlemi
        _merge_optimized(arr, left, mid, right)

def _merge_optimized(arr, left, mid, right):
    # OPTİMİZASYON: Eğer sol parçanın sonu, sağ parçanın başından küçükse
    # birleştirmeye gerek yok (zaten sıralıdır).
    if arr[mid] <= arr[mid + 1]:
        return

    # Python'da tam in-place merge çok yavaştır. 
    # Bu yüzden sadece BİRLEŞTİRME anında geçici dilimler kullanmak 
    # recursive slicing'den çok daha performanslıdır.
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    
    i = 0
    j = 0
    k = left
    
    # Standart Merge İşlemi
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
        
    # Kalan elemanları ekle
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
        
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

# Manual test
if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", sample)
    print("Sorted:", merge_sort(sample))