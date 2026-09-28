# ============================================
# algorithms/radix_sort.py
# Optimized Radix Sort (Handles Negative Integers)
# ============================================

def radix_sort(arr: list) -> list:
    """
    Geliştirilmiş Radix Sort
    - Standart Radix Sort sadece pozitif tamsayıları sıralar.
    - Bu versiyon, negatif sayıları ayırıp mutlak değerlerine göre sıralayarak
      hem negatif hem pozitif karışık veri setlerini destekler.
    """
    # Orijinal diziyi bozmamak için kopya al
    arr_copy = arr.copy()
    
    # 1. Negatif ve Pozitifleri ayır
    positives = [x for x in arr_copy if x >= 0]
    negatives = [-x for x in arr_copy if x < 0] # İşareti pozitife çevir (örn: -5 -> 5)

    # 2. Pozitifleri sırala
    if positives:
        _radix_core(positives)
    
    # 3. Negatifleri sırala
    if negatives:
        _radix_core(negatives)
        # Negatifleri sıraladıktan sonra (örn: 2, 5, 10),
        # orijinal haline çevirmek için ters çevirip -1 ile çarpmalıyız.
        # Sonuç: -10, -5, -2 (Doğru sıralama)
        negatives = [-x for x in reversed(negatives)]

    # 4. Listeleri Birleştir (Negatifler + Pozitifler)
    # Burada yeni bir liste döndürüyoruz
    return negatives + positives

def _radix_core(arr):
    """
    Standart LSD (Least Significant Digit) Radix Sort mantığı.
    Sadece pozitif tamsayılar üzerinde çalışır.
    """
    if not arr:
        return

    # Maksimum sayıyı bul (kaç basamaklı olduğunu anlamak için)
    max_val = max(arr)

    # Basamak basamak Counting Sort uygula (1ler, 10lar, 100ler...)
    exp = 1
    while max_val // exp > 0:
        _counting_sort(arr, exp)
        exp *= 10

def _counting_sort(arr, exp):
    """
    Spesifik bir basamak (exp) için Counting Sort uygular.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 0-9 arası rakamlar için bucket

    # O basamaktaki rakamları say
    for i in range(n):
        index = (arr[i] // exp)
        count[index % 10] += 1

    # Kümülatif toplam (Elemanların pozisyonunu belirlemek için)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Çıktı dizisini oluştur (Sıralamayı koruyarak - Stable Sort özelliği)
    # Sondan başa doğru gidiyoruz ki önceki basamaklardaki sıralama bozulmasın.
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)
        # count dizisindeki değer, o elemanın output dizisindeki yerini gösterir
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Sıralanmış çıktıyı orijinal diziye kopyala
    for i in range(n):
        arr[i] = output[i]

# Manual test
if __name__ == "__main__":
    # Test: Negatif ve pozitif karışık
    sample = [170, -45, 75, -90, 802, 24, 2, 66]
    print("Original:", sample)
    print("Sorted:  ", radix_sort(sample))