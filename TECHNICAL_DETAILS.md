# ALGO Projesi - İleri Teknik Detaylar

## A. MODÜL BAĞIMLILIKLARI (Import Graph)

```
main.py
  └── benchmark/runner.py
      ├── data/generator.py
      │   └── random, numpy
      ├── benchmark/time_analysis.py
      │   └── time
      ├── benchmark/memory_analysis.py
      │   └── tracemalloc
      ├── algorithms/quick_sort.py
      │   └── random
      ├── algorithms/merge_sort.py
      ├── algorithms/heap_sort.py
      ├── algorithms/shell_sort.py
      └── algorithms/radix_sort.py

gui/app.py
  ├── analysis/theoretical_analysis.py
  ├── data/generator.py
  ├── benchmark/time_analysis.py
  ├── benchmark/memory_analysis.py
  ├── tkinter (UI)
  ├── matplotlib (Grafik)
  └── Tüm algoritmaları import eder

visualization/*.py
  ├── pandas (CSV okuma)
  └── matplotlib (Grafik çizim)
```

---

## B. VERI AKIŞI DETAYLANDIRMASı

### B.1 Benchmark Türü Veri Akışı

```
BAŞLANGIÇ
    ↓
main.py çalıştırılır
    ↓
runner.run_benchmark() çağrılır
    ↓
[Loop] DATA_SIZES = [1000, 10000, 100000]
    ↓
    [Loop] DATA_TYPES = ["random", "partial", "reverse"]
        ↓
        [Loop] ALGORITHMS = {5 algoritma}
            ↓
            generate_dataset(size, type)
            Çıkış: int list [8392, 1023, ..., 5291]
            ↓
            data_for_time = deepcopy(veri)
            data_for_memory = deepcopy(veri)
            ↓
            measure_time(algoritma, data, runs=3)
            │ ├─ 1. Çalıştırma: start ─ algoritma ─ end
            │ ├─ 2. Çalıştırma: start ─ algoritma ─ end
            │ ├─ 3. Çalıştırma: start ─ algoritma ─ end
            │ └─ Ortalama = (çalıştırma1 + çalıştırma2 + çalıştırma3) / 3
            Çıkış: float (ms cinsinden)
            ↓
            measure_memory(algoritma, data)
            │ ├─ tracemalloc.start()
            │ ├─ algoritma(veri)
            │ ├─ current, peak = tracemalloc.get_traced_memory()
            │ └─ peak / 1024 = KB
            Çıkış: float (KB cinsinden)
            ↓
            [algo_name, size, type, time_ms] → time_list ekle
            [algo_name, size, type, memory_kb] → memory_list ekle
            
            EKRAN ÇIKTI:
            "Quick Sort | size=1000 | type=random | 3.10 ms | 8.85 KB"

save_time_results(time_list)
    ↓
    CSV yazma: results/time_results.csv
    ├─ Header: Algorithm,Data Size,Data Type,Time (ms)
    └─ Veri satırları

save_memory_results(memory_list)
    ↓
    CSV yazma: results/memory_results.csv
    ├─ Header: Algorithm,Data Size,Data Type,Memory (KB)
    └─ Veri satırları

SON
```

**Toplam Test Sayısı:** 3 boyut × 3 tür × 5 algoritma = **45 test**  
**Radix Sort Filtresi:** Negatif veri varsa atlanır

---

### B.2 GUI Veri Akışı

```
BAŞLANGIÇ (GUI penceresi açılır)
    ↓
app.py → SortingGUI class yüklenir
    ├─ Tema yüklenir (LIGHT/DARK)
    ├─ Header oluşturulur
    ├─ Control paneli oluşturulur
    │  ├─ Analiz Modu: Practical (default) / Theoretical / Comparison
    │  ├─ Algoritma: Quick Sort (default)
    │  ├─ Veri Boyutu: 10000 (default)
    │  └─ Tümü Karşılaştır: Unchecked (default)
    └─ Matplotlib canvas başlatılır

Kullanıcı: Analiz Modu = "Practical" → Algoritma = "Quick Sort" → Run butonu
    ↓
update_view() çağrılır
    ├─ mode = "practical"
    └─ run_practical() çağrılır
        ↓
        size = 10000
        patterns = ["random", "partial", "reverse"]
        
        For each pattern:
            ├─ generate_dataset(10000, "random")
            │  Çıkış: [2891, 5023, ..., 1234]
            ├─ measure_time(quick_sort, data, runs=3)
            │  Çıkış: 20.7449 ms
            └─ ax_time.plot(
                x_values=["random", "partial", "reverse"],
                y_values=[20.7449, 19.6714, 19.0375],
                label="Quick Sort"
               )
        
        ↓
        ax_time.legend() ve gösterim
        ↓
        Matplotlib canvas güncellenir
        Ekranda grafik görünür


Kullanıcı: Analiz Modu = "Theoretical" → Algoritma = "Merge Sort" → Run butonu
    ↓
update_view() çağrılır
    ├─ mode = "theoretical"
    └─ show_theoretical() çağrılır
        ↓
        format_theoretical_text("Merge Sort") çağrılır
            ├─ get_theoretical_info("Merge Sort")
            │  Çıkış: {
            │    "best_case": "O(n log n)",
            │    "average_case": "O(n log n)",
            │    "worst_case": "O(n log n)",
            │    "space_complexity": "Extra memory O(n)",
            │    "notes": "Merge Sort has stable..."
            │  }
            └─ Format edilmiş metin oluştur:
               "Algorithm: Merge Sort
                Best Case: O(n log n)
                ..."
        ↓
        Canvas'a metin ekranda göster

Kullanıcı: "Tümü Karşılaştır" checkbox'ını işaretle → Run
    ↓
update_view() → run_practical()
    ├─ compare_all = True
    ├─ For each algorithm in ALGORITHMS:
    │   ├─ For each pattern in patterns:
    │   │   ├─ generate_dataset(10000, pattern)
    │   │   ├─ measure_time(algoritma, data)
    │   │   └─ time ekle
    │   └─ ax_time.plot(patterns, times, label=algo_name)
    └─ Tüm algoritmaların çizgileri görünür

SON
```

---

## C. ALGORİTMA EXECUTION FLOW

### C.1 Quick Sort Execution

```
quick_sort([38, 27, 43, 3, 9, 82, 10])
    ↓
arr_copy = [38, 27, 43, 3, 9, 82, 10]
_quick_sort(arr_copy, 0, 6)
    ↓
    low=0, high=6, low < high? YET
        ↓
        _random_partition(arr, 0, 6)
            ├─ pivot_index = random.randint(0, 6) → örn. 4
            ├─ arr[4] ↔ arr[6]: [38, 27, 43, 3, 82, 9, 10]
            ├─ _partition(arr, 0, 6)
            │   ├─ pivot = 10
            │   ├─ i = -1
            │   ├─ j=0: arr[0]=38 > 10? HAYIR
            │   ├─ j=1: arr[1]=27 > 10? HAYIR
            │   ├─ j=2: arr[2]=43 > 10? EVET
            │   ├─ j=3: arr[3]=3 ≤ 10? EVET → i=0, swap → [3, 27, 43, 38, 82, 9, 10]
            │   ├─ j=4: arr[4]=82 > 10? EVET
            │   ├─ j=5: arr[5]=9 ≤ 10? EVET → i=1, swap → [3, 9, 43, 38, 82, 27, 10]
            │   └─ son: swap(arr[2], arr[6]) → [3, 9, 10, 38, 82, 27, 43]
            │       return 2
            └─ pivot_index = 2
        ↓
        _quick_sort(arr, 0, 1)  // Sol taraf
        _quick_sort(arr, 3, 6)  // Sağ taraf

return [3, 9, 10, 27, 38, 43, 82]
```

### C.2 Merge Sort Execution

```
merge_sort([38, 27, 43, 3, 9, 82, 10])
    ↓
len(arr) = 7 > 1? EVET
    ├─ mid = 3
    ├─ merge_sort([38, 27, 43])  // left
    │   ├─ mid = 1
    │   ├─ merge_sort([38]) → [38]
    │   ├─ merge_sort([27, 43])
    │   │   ├─ mid = 1
    │   │   ├─ merge_sort([27]) → [27]
    │   │   ├─ merge_sort([43]) → [43]
    │   │   └─ _merge([27], [43]) → [27, 43]
    │   └─ _merge([38], [27, 43])
    │       ├─ 38 ≤ 27? HAYIR → 27 ekle
    │       ├─ 38 ≤ 43? EVET → 38 ekle
    │       └─ Kalan: [43]
    │       → [27, 38, 43]
    ├─ merge_sort([3, 9, 82, 10])
    │   └─ ... (benzer işlem)
    │   → [3, 9, 10, 82]
    └─ _merge([27, 38, 43], [3, 9, 10, 82])
        ├─ 27 ≤ 3? HAYIR → 3 ekle → [3]
        ├─ 27 ≤ 9? HAYIR → 9 ekle → [3, 9]
        ├─ 27 ≤ 10? HAYIR → 10 ekle → [3, 9, 10]
        ├─ 27 ≤ 82? EVET → 27 ekle → [3, 9, 10, 27]
        ├─ 38 ≤ 82? EVET → 38 ekle → [3, 9, 10, 27, 38]
        ├─ 43 ≤ 82? EVET → 43 ekle → [3, 9, 10, 27, 38, 43]
        └─ Kalan: [82]
        → [3, 9, 10, 27, 38, 43, 82]

return [3, 9, 10, 27, 38, 43, 82]
```

### C.3 Radix Sort Execution (LSD)

```
radix_sort([38, 27, 43, 3, 9, 82, 10])
    ↓
max_val = 82
exp = 1  // 1'ler basamağı
    ↓
While exp ≤ 82:
    ├─ exp = 1:
    │   _counting_sort(arr, 1)
    │   ├─ Digit çıkart: 38→8, 27→7, 43→3, 3→3, 9→9, 82→2, 10→0
    │   ├─ Count: [1, 0, 1, 2, 0, 0, 0, 1, 1, 1]
    │   │  (0 sayısı: 1 kere, 2 sayısı: 1 kere, 3 sayısı: 2 kere, ...)
    │   ├─ Cumulative: [1, 1, 2, 4, 4, 4, 4, 5, 6, 7]
    │   └─ Output: [10, 82, 43, 3, 27, 38, 9]
    │       (0'lar bitmiş, 2'ler, 3'ler, 7'ler, 8'ler, 9'lar)
    │
    ├─ exp = 10:
    │   _counting_sort(arr, 10)
    │   ├─ Digit çıkart: 10→1, 82→8, 43→4, 3→0, 27→2, 38→3, 9→0
    │   ├─ Count: [2, 1, 1, 1, 1, 0, 0, 0, 1, 0]
    │   └─ Output: [3, 9, 10, 27, 38, 43, 82]
    │
    └─ exp = 100: 82 < 100, döngü sona erer

return [3, 9, 10, 27, 38, 43, 82]
```

---

## D. BELLEK KULLANIMI ANALİZİ

### D.1 Algorithm Bazında Bellek Profili (n=10000)

```
Quick Sort:
├─ Orijinal array: ~80 KB
├─ Recursive stack: O(log n) = 10 levels × ~1KB ≈ 10 KB
├─ Pivot selection: O(1)
└─ TOPLAM: ~90 KB (in-place)

Merge Sort:
├─ Orijinal array: ~80 KB
├─ Auxiliary arrays (merging): ~80 KB × n level ≈ 80 KB
├─ Recursive call stack: ~10 KB
└─ TOPLAM: ~165 KB (çift boyut)

Heap Sort:
├─ Orijinal array: ~80 KB
├─ Heap structure: (In-place aynı array)
├─ Recursive heapify stack: ~10 KB
└─ TOPLAM: ~80 KB (in-place)

Shell Sort:
├─ Orijinal array: ~80 KB
├─ Gap sequence: O(1)
└─ TOPLAM: ~80 KB (in-place)

Radix Sort:
├─ Orijinal array: ~80 KB
├─ Output array (counting sort): ~80 KB
├─ Count array (10 buckets): ~1 KB
└─ TOPLAM: ~165 KB (extra array)
```

### D.2 Tracemalloc Ölçüm Örneği

```python
tracemalloc.start()
quick_sort([...])  # 10.000 eleman

Heap tarafından kullanılan bellek:
├─ Array allocation: 80 KB
├─ Function call stack: ~5 KB
├─ Python object overhead: ~2 KB
└─ Temp variables: ~1 KB
= 88 KB (peak)

tracemalloc.get_traced_memory()
→ (current=88000 bytes, peak=88000 bytes)
→ peak / 1024 = 85.94 KB
```

---

## E. VERİ AYRILARI (Data Patterns)

### E.1 Random Pattern Üretim

```python
generate_random(size=10)
→ [random.randint(0, 100) for _ in range(10)]
→ [47, 23, 89, 12, 65, 34, 78, 56, 9, 41]
   (Hiçbir düzen yok)
```

### E.2 Reverse Pattern Üretim

```python
generate_reverse(size=10)
→ list(range(10, 0, -1))
→ [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
   (Tamamen ters sıralı)
```

### E.3 Partially Sorted Pattern Üretim

```python
generate_partially_sorted(size=10, sorted_ratio=0.7)
→ sorted_part = list(range(7))
→ sorted_part = [0, 1, 2, 3, 4, 5, 6]
→ random_part = [random.randint(0, 100) for _ in range(3)]
→ random_part = [87, 23, 45]
→ return [0, 1, 2, 3, 4, 5, 6] + [87, 23, 45]
→ [0, 1, 2, 3, 4, 5, 6, 87, 23, 45]
   (%70 sıralı, %30 rastgele)
```

---

## F. BENCHMARK ÇIKTI DETAYLI TABLOSU

### Tam Dataset (45 test sonucu)

```
Data Size: 1000
┌──────────────┬──────────┬────────────────┬──────────────┐
│ Algorithm    │ Random   │ Partial        │ Reverse      │
├──────────────┼──────────┼────────────────┼──────────────┤
│ Quick Sort   │ 3.10 ms  │ 2.13 ms        │ 1.60 ms      │
│ Merge Sort   │ 2.19 ms  │ 2.50 ms        │ 2.66 ms      │
│ Heap Sort    │ 2.76 ms  │ 3.54 ms        │ 2.98 ms      │
│ Shell Sort   │ 1.86 ms  │ 1.83 ms        │ 1.39 ms      │
│ Radix Sort   │ 1.14 ms  │ 1.74 ms        │ 1.08 ms      │
└──────────────┴──────────┴────────────────┴──────────────┘

Data Size: 10000
┌──────────────┬──────────┬────────────────┬──────────────┐
│ Algorithm    │ Random   │ Partial        │ Reverse      │
├──────────────┼──────────┼────────────────┼──────────────┤
│ Quick Sort   │ 20.74 ms │ 19.67 ms       │ 19.04 ms     │
│ Merge Sort   │ 34.43 ms │ 19.78 ms       │ 17.90 ms     │
│ Heap Sort    │ 47.30 ms │ 42.62 ms       │ 41.34 ms     │
│ Shell Sort   │ 29.54 ms │ 23.61 ms       │ 19.86 ms     │
│ Radix Sort   │ 15.53 ms │ 15.64 ms       │ 19.18 ms     │
└──────────────┴──────────┴────────────────┴──────────────┘

Data Size: 100000
┌──────────────┬──────────┬────────────────┬──────────────┐
│ Algorithm    │ Random   │ Partial        │ Reverse      │
├──────────────┼──────────┼────────────────┼──────────────┤
│ Quick Sort   │ 282.21 ms│ 227.65 ms      │ 216.96 ms    │
│ Merge Sort   │ 304.71 ms│ 233.85 ms      │ 198.62 ms    │
│ Heap Sort    │ 595.79 ms│ 572.45 ms      │ 478.74 ms    │
│ Shell Sort   │ 496.96 ms│ 366.86 ms      │ 268.05 ms    │
│ Radix Sort   │ 217.37 ms│ 186.83 ms      │ 188.67 ms    │
└──────────────┴──────────┴────────────────┴──────────────┘
```

---

## G. GRAFIK ÇIKTI AÇIKLAMASI

### G.1 Time Comparison Grafiği

```
     Time (ms)
     ^
 600 |                     ╔═╗  ┃┃  (Heap Sort)
 500 |                     ║ ║  ┃┃
 400 |                ┃┃   ║ ║  ┃┃
 300 |  ╔═╗ ╔═╗ ┃┃   ┃┃   ║ ║
 200 |  ║ ║ ║ ║ ┃┃   ┃┃   ║ ║  ╔═╗ ╔═╗
 100 |  ║ ║ ║ ║ ┃┃   ┃┃   ║ ║  ║ ║ ║ ║
   0 └──║─║─║─║─┃┃───┃┃───║─║──║─║─║─║────────>
       QS MS HS SS RS     (n=100000, random)
       
QS = Quick Sort  
MS = Merge Sort  
HS = Heap Sort (En yavaş)  
SS = Shell Sort  
RS = Radix Sort (En hızlı)
```

### G.2 Memory Comparison Grafiği

```
     Memory (KB)
     ^
2000 |  ╔════╗        
1500 |  ║ MS ║ ╔════╗     
1000 |  ║    ║ ║ RS ║  ╔╗╔╗╔╗
 500 |  ╔════╗ ║    ║  ║║║║║║
   0 └──║ QS ║─────╔╗──║║║║║║─────>
       (n=10000)   HS SS

QS = In-place (8KB)    ✓
MS = Extra (165KB)     ✗
HS = In-place (8KB)    ✓
SS = In-place (8KB)    ✓
RS = Extra (156KB)     ✗
```

---

## H. HATA YÖNETIMI (Error Handling)

### H.1 Radix Sort Limitations

```python
# runner.py L32-33
if algo_name == "Radix Sort" and min(base_data) < 0:
    continue  # Negative data için skip
```

**Neden:** Radix Sort yalnızca **negatif olmayan tam sayılar** için tasarlandı

**Çözüm:** generate_dataset() sadece negatif olmayan sayı üretir

### H.2 Deep Copy Zorunluluğu

```python
data_for_time = copy.deepcopy(base_data)
data_for_memory = copy.deepcopy(base_data)
```

**Neden:** In-place algoritmalar orijinal veriyi modifiye eder  
**Sonuç:** Herbir test için temiz kopya gerekli

---

## I. PERFORMANSKARŞILAŞTIRMASI

### I.1 n=10000'da Best Performer

```
Bütün desenlerde:
1. Radix Sort: ~15-19 ms ⚡ (Sayı-tabanlı, verimli)
2. Quick Sort: ~19-20 ms ⚡ (Randomized pivot iyi)
3. Merge Sort: ~17-34 ms 📊 (Desenin etkisi var)
```

### I.2 n=100000'da Bellek Trade-off

```
Hızlı ama pahalı:
- Radix Sort: 217 ms, 1563 KB (hızlı + çok bellek)
- Merge Sort: 304 ms, 1686 KB (yavaş + çok bellek)

Yavaş ama verimli:
- Shell Sort: 496 ms, 781 KB (orta + az bellek)
- Heap Sort: 595 ms, 781 KB (yavaş + az bellek)
```

---

## J. TEORIK KARMAŞIKLIK İSPATI

### J.1 Quick Sort: O(n log n) Ortalama

```
Average Case:
T(n) = 2T(n/2) + O(n)     [Pivot ortalama n/2 böler]
Karşılık: Master Theorem → O(n log n) ✓

Worst Case:
T(n) = T(n-1) + T(0) + O(n)  [Pivot her zaman en büyük]
Karşılık: T(n) = n + (n-1) + ... + 1 = O(n²) ✓
```

### J.2 Merge Sort: O(n log n) Garantili

```
Recurrence:
T(n) = 2T(n/2) + O(n)
       [2 yarım dizi + O(n) merge]

Master Theorem (a=2, b=2, f(n)=n):
O(n log n) TÜÜM durumlarda ✓
```

### J.3 Radix Sort: O(nk) Non-Comparison

```
Dış loop: k iterasyon (digit sayısı)
İç loop: Counting sort = O(n + 10)
Toplam: O(k × (n + 10)) = O(nk) ✓
```

---

## K. OPTİMİZASYON FIRSATLARI

```
❌ Şu anki:
- Radix Sort negative number'lar skip ediyor
- Sort animation boş
- Tablo görselleştirmesi yok

✅ Yapılabilir:
- Dual Pivot Quick Sort
- Timsort (Merge+Insertion hybrid)
- Counting Sort negative support
- Parallel sorting (multiprocessing)
- Animation framework (Pygame/Matplotlib animation)
```

---

## L. CSV ÖNEKLİ VERI YAPISI

### L.1 time_results.csv

```
Algorithm,Data Size,Data Type,Time (ms)
Quick Sort,1000,random,3.1019
Quick Sort,1000,partial,2.1274
Quick Sort,1000,reverse,1.5988
Quick Sort,10000,random,20.7449
...
Radix Sort,100000,reverse,188.6744
```

**Toplam Satır:** 1 header + 45 data = 46 satır

### L.2 memory_results.csv

```
Algorithm,Data Size,Data Type,Memory (KB)
Quick Sort,1000,random,8.85
Quick Sort,1000,partial,8.96
...
Radix Sort,100000,reverse,1563.01
```

**Toplam Satır:** 1 header + 45 data = 46 satır

---

## M. TKINTER GUI COMPONENTLER

```
Window (980×760)
│
├─ header (tk.Frame)
│  ├─ title_lbl: "Sorting Algorithms Performance Visualizer"
│  └─ subtitle_lbl: "Practical, Theoretical and Comparison Analysis"
│
├─ control_frame (tk.Frame)
│  ├─ Radiobutton: "Practical"
│  ├─ Radiobutton: "Theoretical"
│  ├─ Radiobutton: "Comparison"
│  ├─ Separator (vertical)
│  ├─ Label: "Algorithm"
│  ├─ Combobox: [Quick Sort, Merge Sort, ...]
│  ├─ Separator (vertical)
│  ├─ Label: "Data Size"
│  ├─ Spinbox: 1000 to 100000
│  ├─ Checkbutton: "Compare All Algorithms"
│  └─ Button: "Run / Show"
│
└─ plot_area (tk.Frame)
   ├─ FigureCanvasTkAgg (Matplotlib)
   ├─ ax_time (eksen)
   └─ ax_memory (eksen)
```

---

## N. KAYNAKÇA & REFERANSLAR

- Quick Sort randomization: Introductionto Algorithms (Cormen et al.)
- LSD Radix Sort: Standard Algorithms textbook
- Tracemalloc: Python official documentation
- Tkinter Canvas: tkinter library reference
- Matplotlib integration: Embedding Matplotlib with Tkinter

