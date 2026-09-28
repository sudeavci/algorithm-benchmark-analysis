# ALGO PROJESI - BAŞKA BİR YAPAY ZEKAYA İZAH

## Selam! Sana ALGO adında bir proje hakkında detaylı bir analiz vereceğim.

Bu bilgiyi tamamen anlaman ve başka birine/başka bir sisteme açıklayabilmen için tasarlanmıştır.

---

## 📌 PROJE ÖZET

**PROJE ADI:** ALGO (Sorting Algorithm Performance Analyzer)  
**TANIMAMA:** Beş farklı sıralama algoritmasının performansını ölçen, karşılaştıran ve görselleştiren Python eğitim aracı

**MUHASEBESI:**
- 5 farklı sıralama algoritması (Quick, Merge, Heap, Shell, Radix)
- 3 veri boyutu (1000, 10000, 100000 eleman)
- 3 veri deseni (random, partially sorted, reverse)
- Toplam 45 benchmark testi
- Zaman ve bellek ölçümü
- Etkileşimli GUI
- Teorik karmaşıklık analizi

---

## 🏗️ YAPIŞI (ARCHITECTURE)

```
┌─────────────────────────────────────────────────────────┐
│                    GİRİŞ: main.py                      │
│                  (Benchmark başlatır)                  │
└────────────────┬────────────────────────────────────────┘
                 │
                 ├──────────────────────────────────────────┐
                 │                                          │
          ┌──────▼──────┐                          ┌───────▼────┐
          │ Benchmark   │                          │     GUI    │
          │   (runner)  │                          │  (tkinter) │
          └──────┬──────┘                          └───────┬────┘
                 │                                        │
         ┌───────┼────────────┐                   ┌───────▼────────┐
         │       │            │                   │                │
    ┌────▼─┐ ┌──▼──┐ ┌──────▼┐            ┌──────▼──┐ ┌─────────┐
    │ Data │ │Time │ │Memory │            │Theoretical│Visualization│
    │ Gen. │ │Meas │ │Meas.  │            │ Analysis  │(matplotlib) │
    └─────┘ └─────┘ └──────┘             └────┬──────┘ └─────────┘
         │                                      │
         └──────────────┬───────────────────────┘
                        │
                   ┌────▼─────┐
                   │ Algoritma │
                   │  (5 tane) │
                   └──────────┘
                        │
                   ┌────▼─────┐
                   │ Sonuçlar  │
                   │ (CSV)     │
                   └──────────┘
```

---

## 📂 TÜM DOSYALAR (DIRECTORY TREE)

```
ALGO/
├── main.py                                    [9 satır]
│   └─ Giriş noktası, run_benchmark() çağırır
│
├── algorithms/                                [5 uyg.]
│   ├── quick_sort.py                         [54 satır]
│   │   ├─ Public: quick_sort(arr) → list
│   │   ├─ Private: _quick_sort, _random_partition, _partition
│   │   ├─ Strategi: Randomized pivot (worst case kaçınma)
│   │   ├─ Karmaşıklık: Avg O(n log n), Worst O(n²)
│   │   ├─ Space: O(log n) recursion stack
│   │   ├─ In-place: EVET
│   │   └─ Stabil: HAYIR
│   │
│   ├── merge_sort.py                         [47 satır]
│   │   ├─ Public: merge_sort(arr) → list
│   │   ├─ Private: _merge(left, right)
│   │   ├─ Strategi: Böl-Yönet (Divide & Conquer)
│   │   ├─ Karmaşıklık: TÜMÜ O(n log n) ✓ Garantili
│   │   ├─ Space: O(n) auxiliary array
│   │   ├─ In-place: HAYIR
│   │   └─ Stabil: EVET ✓
│   │
│   ├── heap_sort.py                          [54 satır]
│   │   ├─ Public: heap_sort(arr) → list
│   │   ├─ Private: _heapify(arr, size, idx)
│   │   ├─ Strategi: Max-Heap oluştur, elemanlı çıkar
│   │   ├─ Karmaşıklık: TÜMÜ O(n log n)
│   │   ├─ Space: O(1) in-place
│   │   ├─ In-place: EVET
│   │   └─ Stabil: HAYIR
│   │
│   ├── shell_sort.py                         [45 satır]
│   │   ├─ Public: shell_sort(arr) → list
│   │   ├─ Strategi: Gap sequence (n/2, n/4, ..., 1)
│   │   ├─ Karmaşıklık: Best O(n log n), Avg O(n^1.5), Worst O(n²)
│   │   ├─ Space: O(1)
│   │   ├─ In-place: EVET
│   │   ├─ Stabil: HAYIR
│   │   └─ Özellik: Partially sorted veri için ÇOK HIZLI
│   │
│   └── radix_sort.py                         [65 satır]
│       ├─ Public: radix_sort(arr) → list
│       ├─ Private: _counting_sort(arr, exp)
│       ├─ Strategi: LSD (Least Significant Digit)
│       ├─ Karmaşıklık: TÜMÜ O(nk) [k=digit sayısı]
│       ├─ Space: O(n+10) output+buckets
│       ├─ In-place: HAYIR
│       ├─ Stabil: EVET
│       ├─ Özellik: Non-comparison, Integer-only
│       └─ Kısıtlama: Negatif sayılar desteklenmez
│
├── benchmark/                                 [3 dosya]
│   ├── runner.py                             [69 satır]
│   │   ├─ run_benchmark()
│   │   │   ├─ Parametreler:
│   │   │   │   ├─ DATA_SIZES = [1000, 10000, 100000]
│   │   │   │   ├─ DATA_TYPES = ["random", "partial", "reverse"]
│   │   │   │   └─ ALGORITHMS = {5 sıralama}
│   │   │   ├─ Akış: For Size, Type, Algo: Ölç & Kaydet
│   │   │   └─ Çıktı: time_results.csv + memory_results.csv
│   │   └─ save_time_results() / save_memory_results()
│   │
│   ├── time_analysis.py                      [25 satır]
│   │   └─ measure_time(sort_func, data, runs=3) → float (ms)
│   │      ├─ Yapı: 3 kez çalıştır, ortalama al
│   │      ├─ Tool: time.perf_counter()
│   │      └─ Çıkış: Milisaniye cinsinde
│   │
│   └── memory_analysis.py                    [25 satır]
│       └─ measure_memory(sort_func, data) → float (KB)
│          ├─ Yapı: tracemalloc ile peak bellek ölç
│          ├─ Tool: tracemalloc.get_traced_memory()
│          └─ Çıkış: Kilobyte cinsinde
│
├── data/                                      [1 dosya]
│   └── generator.py                          [50 satır]
│       ├─ generate_dataset(size, type) → list
│       ├─ Türleri:
│       │   ├─ "random": [8392, 2011, 5729, ...] (rasgele)
│       │   ├─ "reverse": [10000, 9999, ..., 1] (ters)
│       │   └─ "partial": [0,1,2,...,7000] + [89,23,45] (70% sıralı)
│       ├─ Yardımcı: generate_random, generate_reverse, generate_partially_sorted
│       └─ Kullanım: Benchmark için test veri üretmek
│
├── analysis/                                  [1 dosya]
│   └── theoretical_analysis.py               [124 satır]
│       ├─ THEORETICAL_INFO = {5 algoritmanın bilgisi}
│       │   └─ Her algoritma:
│       │       ├─ best_case (string: "O(...)")
│       │       ├─ average_case
│       │       ├─ worst_case
│       │       ├─ space_complexity
│       │       └─ notes (açıklama metni)
│       ├─ get_algorithm_names() → list
│       ├─ get_theoretical_info(name) → dict
│       └─ format_theoretical_text(name) → str
│       └─ Kullanım: GUI'de teorik bilgi göstermek
│
├── gui/                                       [2 dosya]
│   ├── app.py                                [518 satır]
│   │   ├─ SortingGUI(tk.Tk) class
│   │   ├─ Bileşenler:
│   │   │   ├─ Header: Başlık + Açıklama
│   │   │   ├─ Control Panel:
│   │   │   │   ├─ Analiz Modu (Practical/Theoretical/Comparison)
│   │   │   │   ├─ Algoritma Seçimi (dropdown)
│   │   │   │   ├─ Veri Boyutu (spinbox: 1000-100000)
│   │   │   │   ├─ Tümü Karşılaştır (checkbox)
│   │   │   │   └─ Run/Show butonu
│   │   │   └─ Plot Area (matplotlib canvas)
│   │   ├─ Temalar: LIGHT & DARK
│   │   ├─ Analiz Modları:
│   │   │   ├─ Practical: Gerçek ölçüm sonuçları (grafik)
│   │   │   ├─ Theoretical: Teori Big-O (metin)
│   │   │   └─ Comparison: Tüm algoritmalar (çok grafik)
│   │   └─ Yöntemler: update_view(), run_practical(), show_theoretical(), show_comparison()
│   │
│   └── tempCodeRunnerFile.py                 [Geçici, görmezden gel]
│
├── visualization/                             [6 dosya + 2 boş/eksik]
│   ├── time_comparison.py                    [38 satır]
│   │   └─ plot_time_comparison(size, type) → PNG kaydeder
│   │
│   ├── memory_comparison.py                  [38 satır]
│   │   └─ plot_memory_comparison(size, type) → PNG kaydeder
│   │
│   ├── pattern_comparison.py                 [38 satır]
│   │   └─ plot_pattern_comparison(algo, size) → PNG kaydeder
│   │
│   ├── algorithm_pattern_comparison.py       [38 satır]
│   │   └─ plot_algorithm_pattern_comparison(size) → PNG kaydeder
│   │
│   ├── plot_time.py                          [32 satır]
│   │   └─ plot_time_by_size(type) → etkileşimli matplotlib
│   │
│   ├── plot_memory.py                        [32 satır]
│   │   └─ plot_memory_by_algorithm(size, type) → etkileşimli matplotlib
│   │
│   ├── sort_animation.py                     [EKSIK]
│   │   └─ quick_sort_visual(arr) → generator (hatalı/eksik)
│   │
│   └── tables.py                             [BOŞ]
│       └─ CSV → Tablo görselleştirmesi (yapılmamış)
│
├── results/                                   [2 dosya]
│   ├── time_results.csv                      [46 satır: 1 header + 45 data]
│   │   ├─ Sütunlar: Algorithm,Data Size,Data Type,Time (ms)
│   │   └─ Örnek: Quick Sort,10000,random,20.7449
│   │
│   └── memory_results.csv                    [46 satır]
│       ├─ Sütunlar: Algorithm,Data Size,Data Type,Memory (KB)
│       └─ Örnek: Quick Sort,10000,random,79.87
│
├── report/                                    [2 dosya + klasör]
│   ├── theoretical_vs_practical.md           [Analiz raporu]
│   │   └─ Her algoritma için: Teori + Pratik + Uyum analizi
│   │
│   └── figures/                              [PNG grafikler]
│       └─ report/figures/*.png (visualization/ tarafından oluşturulur)
│
├── requirements.txt                          [3 paket]
│   ├─ matplotlib>=3.5.0
│   ├─ numpy>=1.19.0
│   └─ pandas (implied, tkinter built-in)
│
└── README.md                                 [BOŞ]
```

---

## 🔄 VERİ AKIŞI (Data Flow)

### Senaryo 1: Benchmark Çalıştırma

```
BAŞLANGIÇ
   ↓
main.py → benchmark/runner.py → run_benchmark()
   ↓
[Paralel değil, sırasız]
For size in [1000, 10000, 100000]:
  For type in ["random", "partial", "reverse"]:
    For algo_name, algo_func in ALGORITHMS.items():
      ↓
      DATA_GEN: generate_dataset(size, type)
      Çıkış: list of int
      ↓
      COPY: data_for_time = deepcopy(data)
      ↓
      TIME_MEASURE: measure_time(algo_func, data_for_time, runs=3)
        │ Run 1: t_start → algo → t_end → delta
        │ Run 2: t_start → algo → t_end → delta
        │ Run 3: t_start → algo → t_end → delta
        │ Avg = (delta1 + delta2 + delta3) / 3
        └ Return: float (ms)
      ↓
      COPY: data_for_memory = deepcopy(data)
      ↓
      MEMORY_MEASURE: measure_memory(algo_func, data_for_memory)
        │ tracemalloc.start()
        │ algo(data)
        │ current, peak = tracemalloc.get_traced_memory()
        │ tracemalloc.stop()
        └ Return: peak / 1024 (float, KB)
      ↓
      COLLECT: Append [algo_name, size, type, time_ms] to time_results
      COLLECT: Append [algo_name, size, type, memory_kb] to memory_results
      ↓
      PRINT: "Quick Sort | size=1000 | type=random | 3.10 ms | 8.85 KB"
   ↓
SAVE: write time_results to results/time_results.csv
SAVE: write memory_results to results/memory_results.csv
   ↓
SON

Toplam Test: 3 × 3 × 5 = 45 test
Toplam Süre: ~3 dakika
```

### Senaryo 2: GUI Çalıştırma

```
BAŞLANGIÇ
   ↓
python gui/app.py
   ↓
SortingGUI.__init__()
├─ theme = LIGHT (default)
├─ analysis_mode = "practical" (default)
├─ algorithm_var = "Quick Sort" (default)
├─ data_size = 10000 (default)
├─ compare_all = False (default)
├─ Create UI components (header, controls, canvas)
└─ Tkinter window açılır (980×760)
   ↓
USER INTERACTION: Seçim yap
│ Algorithm: "Merge Sort" seç
│ Data Size: 50000 değiştir
│ Analysis Mode: "Comparison" seç
│ Run/Show butonu tıkla
   ↓
SortingGUI.update_view() çağrılır
   ├─ mode = "comparison"
   └─ show_comparison() çağrılır
      │
      ├─ For algo_name, algo_func in ALGORITHMS.items():
      │   │
      │   For pattern in ["random", "partial", "reverse"]:
      │     │
      │     generate_dataset(50000, pattern)
      │     measure_time(algo_func, data, runs=3)
      │     measure_memory(algo_func, data)
      │     │
      │     ax_time.plot(patterns, times, label=algo_name)
      │     ax_memory.plot(patterns, memories, label=algo_name)
      │
      └─ Canvas güncellenir, Matplotlib figure görüntülenir
   ↓
SON
```

---

## 📊 ALGORİTMA KARŞILAŞTIRMA

### Zaman (n=10000, random)

```
                    Perf.
Radix Sort         15.5 ms  ⚡⚡⚡ Çok Hızlı
Quick Sort         20.7 ms  ⚡⚡
Merge Sort         34.4 ms  📊 Orta
Shell Sort         29.5 ms  📊 Orta
Heap Sort          47.3 ms  🐢 Yavaş
```

### Bellek (n=10000, random)

```
Heap Sort          78.6 KB  🟢🟢🟢 In-place
Shell Sort         78.3 KB  🟢🟢🟢 In-place
Quick Sort         79.8 KB  🟢🟢🟢 In-place
Merge Sort        164.9 KB  🟠 Extra array
Radix Sort        156.7 KB  🟠 Extra array
```

### Karmaşıklık Tablosu

```
           | Best       | Average    | Worst      | Space    | In-Pl. | Stabil |
─────────────────────────────────────────────────────────────────────────────
Quick      | O(n log n) | O(n log n) | O(n²)      | O(log n) | ✓      | ✗      |
Merge      | O(n log n) | O(n log n) | O(n log n) | O(n)     | ✗      | ✓      |
Heap       | O(n log n) | O(n log n) | O(n log n) | O(1)     | ✓      | ✗      |
Shell      | O(n log n) | O(n^1.5)   | O(n²)      | O(1)     | ✓      | ✗      |
Radix      | O(nk)      | O(nk)      | O(nk)      | O(n+k)   | ✗      | ✓      |
```

---

## 🎯 KILIT PROGRAMLAMA KONSEPTLERI

### 1. Recursive vs Iterative
- **Quick Sort:** Recursive (pivot seç, böl, yinele)
- **Merge Sort:** Recursive (böl, eşitle, birleştir)
- **Heap Sort:** Iterative (döngü ile heapify)
- **Shell Sort:** Iterative (gap döngüsü)
- **Radix Sort:** Iterative (digit döngüsü)

### 2. In-Place Memory Management
```
In-Place (bellek verimli):
- Quick Sort: arr[i], arr[j] swap
- Heap Sort: Aynı array'de parent/child
- Shell Sort: Aynı array'de gap-shifted

Non-In-Place (ekstra bellek):
- Merge Sort: left[], right[] → merged[]
- Radix Sort: output[] ← arr[] per digit
```

### 3. Benchmark Best Practices
```python
measure_time():
  - Birden çok çalıştırma (runs=3)
  - Ortalama al (noise azaltma)
  - Konsistent ortam (aynı veri boyutu)

measure_memory():
  - Peak bellek ölç (tracemalloc)
  - Başlat/durdur her fonksiyon için
  - Byte → KB çevirme
```

### 4. Data Pattern Effects
```
Random Data:
- Quick Sort iyi (pivot rasgele)
- Heap Sort yavaş (constant factors)
- Radix Sort iyi (balanced digit dist.)

Partial Sorted:
- Shell Sort ÇOOOOOK iyi (gap > gap>...>1)
- Quick Sort biraz iyi
- Merge Sort biraz iyi

Reverse Sorted:
- Merge Sort iyi (divide and conquer)
- Quick Sort biraz iyi (pivot rasgele)
- Heap Sort yavaş (heapify daha fazla)
```

---

## 🛠️ TEKNIK STAKEHOLDERLER

| Dosya Grubu | Amacı | Input | Processing | Output |
|-------------|-------|-------|-----------|--------|
| algorithms/ | Sırala | list | Swap/Arrange | Sorted list |
| data/ | Veri Üret | size, type | Random/Pattern | Test list |
| benchmark/ | Ölç | func, data | time.perf, tracemalloc | ms, KB |
| gui/ | Göster | user input | matplotlib | Visual chart |
| analysis/ | Bilgi | algo name | Dict lookup | Big-O text |
| visualization/ | Kaydet | CSV | Plot pandas | PNG file |

---

## 💾 CSV VERİ YAPISI

### time_results.csv
```
Algorithm,Data Size,Data Type,Time (ms)
Quick Sort,1000,random,3.1019
Quick Sort,1000,partial,2.1274
Quick Sort,1000,reverse,1.5988
Quick Sort,10000,random,20.7449
...
Radix Sort,100000,reverse,188.6744
```

**Satır Sayısı:** 1 (header) + 45 (data) = 46
**Kombinasyon:** 5 algo × 3 size × 3 type = 45

### memory_results.csv
```
Algorithm,Data Size,Data Type,Memory (KB)
Quick Sort,1000,random,8.85
...
```

**Yapı:** time_results.csv ile aynı, değişen sütun: Memory (KB)

---

## 🎯 EXECUTION ÖRNEK

### Quick Sort Trace'i (n=7)

```
Input: [38, 27, 43, 3, 9, 82, 10]

quick_sort() → arr_copy = [38, 27, 43, 3, 9, 82, 10]
  ↓
  _quick_sort(arr, 0, 6)
    ├─ low=0, high=6 (not sorted)
    ├─ _random_partition(0, 6)
    │  ├─ pivot_idx = random.randint(0, 6) → 4
    │  ├─ swap(arr[4], arr[6]) → [38, 27, 43, 3, 82, 9, 10]
    │  ├─ _partition(0, 6)
    │  │  ├─ pivot = 10
    │  │  ├─ Loop j: Karşılaştır ve swap
    │  │  │  j=0: 38>10 NO
    │  │  │  j=1: 27>10 NO
    │  │  │  j=2: 43>10 YES
    │  │  │  j=3: 3≤10 YES → swap, i=0
    │  │  │  j=4: 82>10 YES
    │  │  │  j=5: 9≤10 YES → swap, i=1
    │  │  └─ Final: swap(arr[2], arr[6]) → [3, 9, 10, 38, 82, 27, 43]
    │  └─ Return pivot_idx = 2
    ├─ _quick_sort(0, 1)   ← Left side [3, 9]
    │  ├─ low=0, high=1
    │  ├─ partition → pivot_idx=0 or 1
    │  └─ Recursively sort → [3, 9]
    └─ _quick_sort(3, 6)   ← Right side [38, 82, 27, 43]
       └─ Recursively sort → [27, 38, 43, 82]

Output: [3, 9, 10, 27, 38, 43, 82] ✓
```

---

## 🎓 ÖĞRETİM DEĞERİ

Bu proje şu konuları **görselleştirir:**

1. **Big-O Karmaşıklığı:** Teorik O(n log n) vs Pratik ms
2. **Algorithm Tradeoffs:** Hız vs Bellek, In-Place vs Stability
3. **Veri Deseni Etkisi:** Aynı algoritma farklı davranış
4. **Benchmark Metodoloji:** Nasıl doğru ölçüm yapılır
5. **Python İleri Kavramları:** Recursive, Generators, GUI, CSV

---

## ⚠️ LIMITATIONS (SINIRLILARI)

```
❌ Eksik Özellikler:
- sort_animation.py hatalı (generator trace eksik)
- tables.py boş (tablo görselleştirmesi yok)
- README.md boş (dokümantasyon eksik)
- Negative number handling (Radix Sort)

✅ Yapılabilir İyileştirmeler:
- Dual Pivot Quick Sort
- Timsort (Hybrid)
- Parallel sorting
- Web Dashboard
- Export reports
```

---

## 🚀 BAŞLANGIÇ KODUhemem

```bash
# Kurulum
cd /Users/aysebernabaysal/Downloads/ALGO
pip install -r requirements.txt

# Benchmark çalıştır (3 dakika)
python main.py

# GUI aç (etkileşimli)
python gui/app.py

# Grafikler oluştur
python visualization/time_comparison.py
```

---

## 📈 BEKLENEN ÇIKTI (40. satır time_results.csv)

```
Algorithm,Data Size,Data Type,Time (ms)
Quick Sort,100000,random,282.2125
Merge Sort,100000,random,304.7101
Heap Sort,100000,random,595.7939
Shell Sort,100000,random,496.959
Radix Sort,100000,random,217.3664
```

**Bulgu:** Radix Sort en hızlı (217 ms), Heap Sort en yavaş (595 ms)

---

## 🔐 KRİTİK KODLAR

### Quicksort Pivot Stratejisi
```python
def _random_partition(arr, low, high):
    pivot_index = random.randint(low, high)  # ← ÖNEMLİ
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return _partition(arr, low, high)
```

**Neden?** Worst case O(n²) kaçınmak için randomness

### Bellek Ölçümü
```python
tracemalloc.start()
sort_function(data_copy)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
peak_kb = peak / 1024  # ← CONVERSION
```

**Neden?** Peak bellek algoritmanın max kullanımını gösterir

### GUI Mod Seçimi
```python
if mode == "practical":
    self.run_practical()  # Gerçek ölçüm
elif mode == "theoretical":
    self.show_theoretical()  # Metin Big-O
elif mode == "comparison":
    self.show_comparison()  # Tüm algoritma
```

**Neden?** 3 ayrı görselleştirme türü

---

## ✨ ÖZETİ

| Yön | Açıklama |
|-----|----------|
| **AMAÇ** | 5 sıralama algoritmasını karşılaştırma |
| **VERİ** | 45 benchmark (3 size × 3 type × 5 algo) |
| **METRIK** | Zaman (ms) + Bellek (KB) |
| **OUTPUT** | CSV + PNG + GUI |
| **EDUKASYONALDEĞERİ** | Big-O, Benchmark, Algorithm Design |
| **KOD KALİTESİ** | Temiz, Modüler, Okunabilir |
| **HAZIRLIK** | %95 (sort_animation eksik, tables boş) |

---

**TAMAMLANDI!** Bu dokümantasyon bir başka yapay zekaya (veya kişiye) bu projeyi **tamamen** anlatan bir **başvuru kılavuzudur**.

