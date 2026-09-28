# ALGO Projesi - Hızlı Referans Kılavuzu

## 1. PRİM REFERANS

| Dosya | Amaç | Dil | Satır |
|-------|------|------|-------|
| **main.py** | Giriş noktası | Python | 9 |
| **algorithms/quick_sort.py** | Hızlı Sırala | Python | 54 |
| **algorithms/merge_sort.py** | Birleştirmeli Sırala | Python | 47 |
| **algorithms/heap_sort.py** | Yığın Sırala | Python | 54 |
| **algorithms/shell_sort.py** | Shell Sırala | Python | 45 |
| **algorithms/radix_sort.py** | Radix Sırala | Python | 65 |
| **benchmark/runner.py** | Benchmark Yöneticisi | Python | 69 |
| **benchmark/time_analysis.py** | Zaman Ölçümü | Python | 25 |
| **benchmark/memory_analysis.py** | Bellek Ölçümü | Python | 25 |
| **data/generator.py** | Veri Üreticisi | Python | 50 |
| **analysis/theoretical_analysis.py** | Teorik Bilgi | Python | 124 |
| **gui/app.py** | GUI Uygulaması | Python | 518 |

---

## 2. ÇIKTI DOSYALARI

| Dosya | İçerik | Format | Güncellenme |
|-------|--------|--------|------------|
| `results/time_results.csv` | Zaman ölçümleri | CSV | `runner.py` |
| `results/memory_results.csv` | Bellek ölçümleri | CSV | `runner.py` |
| `report/figures/*.png` | Grafikler | PNG | `visualization/` |
| `report/theoretical_vs_practical.md` | Analiz Raporu | Markdown | Manuel |

---

## 3. AÇIK SORULAR VE CEVAPLAR

### S: Proje neyi yapıyor?
**C:** 5 sıralama algoritmasının performansını ölçen ve karşılaştıran bir eğitim aracı.

### S: Ana modüller nelerdir?
**C:** 
- **Algorithms:** Sıralama uygulamaları
- **Benchmark:** Performans ölçümü
- **Data:** Test veri üretimi
- **GUI:** Kullanıcı arayüzü
- **Visualization:** Grafik çizim
- **Analysis:** Teorik bilgi

### S: Program nasıl çalışır?
**C:**
```
python main.py → Benchmark çalıştır → CSV kaydet → GUI'de görüntüle
```

### S: GUI'de ne yapabilirim?
**C:**
- Algoritma seç
- Veri boyutunu ayarla
- 3 analiz modu: Praktik / Teorik / Karşılaştırma
- Tüm algoritmaları karşılaştır

### S: CSV dosyalarındaki veriler ne anlama geliyor?
**C:**
- `time_results.csv`: Her algoritmanın zaman performansı (ms)
- `memory_results.csv`: Her algoritmanın bellek kullanımı (KB)

### S: Hangi algoritma en hızlı?
**C:** **Radix Sort** (n=10000'da ~15ms)

### S: Hangi algoritma en verimli (bellek)?
**C:** **Heap Sort, Quick Sort, Shell Sort** (in-place, ~8KB)

### S: Neden Radix Sort negatif sayılar işlemiyor?
**C:** LSD Radix Sort sayı basamaklarına göre çalışır, negatifler special handling gerektirir.

---

## 4. ALGORITMA ÖZET TABLOSU

```
┌──────────────┬──────────────┬──────────────┬─────────┬──────────┬────────┐
│ Algoritma    │ Best Case    │ Avg Case     │ Worst   │ Space    │ In-Pl. │
├──────────────┼──────────────┼──────────────┼─────────┼──────────┼────────┤
│ Quick Sort   │ O(n log n)   │ O(n log n)   │ O(n²)   │ O(log n) │ ✓      │
│ Merge Sort   │ O(n log n)   │ O(n log n)   │ O(...)  │ O(n)     │ ✗      │
│ Heap Sort    │ O(n log n)   │ O(n log n)   │ O(...)  │ O(1)     │ ✓      │
│ Shell Sort   │ O(n log n)   │ O(n^1.5)     │ O(n²)   │ O(1)     │ ✓      │
│ Radix Sort   │ O(nk)        │ O(nk)        │ O(nk)   │ O(n+k)   │ ✗      │
└──────────────┴──────────────┴──────────────┴─────────┴──────────┴────────┘
```

---

## 5. VERİ DESENLERI

| Desen | Açıklama | Örnek (n=10) | Kullanım |
|-------|----------|-------------|----------|
| **random** | Tamamen rastgele | `[7,2,9,1,4,8,3,6,5,0]` | Ortalama durum |
| **reverse** | Tamamen ters | `[10,9,8,7,6,5,4,3,2,1]` | Worst case |
| **partial** | %70 sıralı | `[0,1,2,3,4,5,6]+[89,23]` | Gerçek dünya |

---

## 6. FONKSİYON İMZALARI

### Algoritmaların Interface'i
```python
def quick_sort(arr: list) -> list
def merge_sort(arr: list) -> list
def heap_sort(arr: list) -> list
def shell_sort(arr: list) -> list
def radix_sort(arr: list) -> list
# Tümü: arr giriş, sıralanmış list çıkış
```

### Benchmark Fonksiyonları
```python
measure_time(sort_func, data, runs=3) → float (ms)
measure_memory(sort_func, data) → float (KB)
generate_dataset(size, data_type) → list
```

### Teorik Bilgi
```python
get_theoretical_info(algorithm_name) → dict
format_theoretical_text(algorithm_name) → str
```

---

## 7. ORTAM KURULUMU

```bash
# 1. Proje klasörüne git
cd /Users/aysebernabaysal/Downloads/ALGO

# 2. Bağımlılıkları kur
pip install -r requirements.txt

# 3. Benchmark çalıştır
python main.py

# 4. GUI aç
python gui/app.py

# 5. Grafik oluştur
python visualization/time_comparison.py
```

---

## 8. DOSYA HIYERARŞI

```
ALGO/
├── algorithms/          ← Sıralama uygulamaları
│   ├── quick_sort.py
│   ├── merge_sort.py
│   ├── heap_sort.py
│   ├── shell_sort.py
│   └── radix_sort.py
│
├── benchmark/          ← Performans ölçümü
│   ├── runner.py
│   ├── time_analysis.py
│   └── memory_analysis.py
│
├── data/              ← Test veri üretimi
│   └── generator.py
│
├── gui/              ← Kullanıcı arayüzü
│   └── app.py
│
├── visualization/    ← Grafik ve tablolar
│   ├── time_comparison.py
│   ├── memory_comparison.py
│   ├── pattern_comparison.py
│   └── ...
│
├── analysis/         ← Teorik bilgi
│   └── theoretical_analysis.py
│
├── results/          ← Ölçüm sonuçları
│   ├── time_results.csv
│   └── memory_results.csv
│
├── report/           ← Raporlar
│   ├── theoretical_vs_practical.md
│   └── figures/
│
└── main.py          ← Giriş noktası
```

---

## 9. BENCHMARK SONUÇLAR (n=10000, random)

```
Hızlanma Sırası (en hızlı → en yavaş):
1. Radix Sort      ⚡ 15.5 ms
2. Quick Sort      ⚡ 20.7 ms
3. Merge Sort      📊 34.4 ms
4. Shell Sort      📊 29.5 ms
5. Heap Sort       🐢 47.3 ms

Bellek Kullanımı (en az → en çok):
1. Heap Sort       🟢 78.6 KB
2. Shell Sort      🟢 78.3 KB
3. Quick Sort      🟢 79.8 KB
4. Merge Sort      🟠 164.9 KB
5. Radix Sort      🟠 156.7 KB
```

---

## 10. UYGULAMADAKI GÖREVLER

| Görev | Dosya | Fonksiyon | Amaç |
|-------|-------|----------|------|
| Veri üret | `data/generator.py` | `generate_dataset()` | Test veri hazırla |
| Zamanı ölç | `benchmark/time_analysis.py` | `measure_time()` | Yürütme süresi al |
| Belleği ölç | `benchmark/memory_analysis.py` | `measure_memory()` | Peak bellek al |
| Çalıştır | `benchmark/runner.py` | `run_benchmark()` | Tüm testleri yap |
| Göster | `gui/app.py` | `SortingGUI.update_view()` | Sonuçları göster |

---

## 11. VERI AKIŞI (SimpleFlow)

```
Başlangıç
   ↓
Parametreler: Size, Type, Algorithm
   ↓
Veri Üret (generator.py)
   ↓
Algoritma Çalıştır (algorithms/*.py)
   ↓
Ölçüm (time_analysis.py + memory_analysis.py)
   ↓
Sonuçlar (results/*.csv)
   ↓
Görselleştir (visualization/* veya gui/app.py)
   ↓
Sonuç
```

---

## 12. ÖRNEK KOMUTLAR

```bash
# Benchmark çalıştır ve CSV kaydet
python main.py

# GUI başlat (etkileşimli)
python gui/app.py

# Time karşılaştırması grafiği yap
python visualization/time_comparison.py

# Memory karşılaştırması grafiği yap
python visualization/memory_comparison.py

# Veri deseni karşılaştırması yap
python visualization/pattern_comparison.py

# Tüm algoritmaların desenlere tepkisi
python visualization/algorithm_pattern_comparison.py

# Zaman grafiği (etkileşimli)
python visualization/plot_time.py

# Bellek grafiği (etkileşimli)
python visualization/plot_memory.py
```

---

## 13. KONFIGÜRASYON

### Benchmark Parametreleri (runner.py)
```python
DATA_SIZES = [1000, 10000, 100000]
DATA_TYPES = ["random", "partial", "reverse"]
ALGORITHMS = {5 algoritma}
```

### GUI Defaults (app.py)
```python
analysis_mode = "practical"
algorithm = "Quick Sort"
data_size = 10000
compare_all = False
```

### Veri Üretim (generator.py)
```python
generate_random(size)          # random int
generate_reverse(size)         # descending
generate_partially_sorted(size, sorted_ratio=0.7)  # 70% sorted
```

---

## 14. ÇIKTI ÖRNEKLERI

### CSV Örneği
```
Algorithm,Data Size,Data Type,Time (ms)
Quick Sort,1000,random,3.1019
Quick Sort,1000,partial,2.1274
...
```

### Terminal Çıktısı
```
Quick Sort | size=1000 | type=random | 3.10 ms | 8.85 KB
Merge Sort | size=1000 | type=random | 2.19 ms | 16.83 KB
...
```

### GUI Grafiği
```
Matplotlib Figure:
- Title: "Sorting Algorithms Performance Visualizer"
- X-axis: Algorithm adları
- Y-axis: Time (ms)
- Bars: Her algoritmanın performansı
```

---

## 15. HATA ÇÖZÜMÜ

| Hata | Çözüm |
|------|-------|
| `ModuleNotFoundError: pandas` | `pip install pandas` |
| `ModuleNotFoundError: matplotlib` | `pip install matplotlib` |
| `FileNotFoundError: results/` | `mkdir -p results/` |
| Radix Sort negatif sayı veriyor | Veri yalnızca non-negative |
| GUI açılmıyor | `pip install tkinter` |

---

## 16. PROJE İSTATİSTİKLERİ

- **Toplam Dosya:** 27 dosya
- **Python Dosyası:** 18 dosya
- **Algoritma Uygulaması:** 5
- **Benchmark Test:** 45 kombinasyon
- **Toplam Kod Satırı:** ~1500 satır
- **Veri Satırı (CSV):** 90 satır (45 × 2)

---

## 17. ALGORITMA SEÇME REHBERİ

```
Seçeceksem...          İyi çünkü...
────────────────────────────────────────────
Hızlı sıralama         Quicksort = Standart seçim
Garantili O(n log n)   Merge Sort = Stabil + tahmin edilebilir
Bellek tasarrufu       Heap Sort = In-place + O(1) ekstra
Partially sorted veri  Shell Sort = Büyük atlama + hızlı
Integer-only dataset   Radix Sort = Non-comparison, çok hızlı
```

---

## 18. BENCHMARK SÜRE TAHMINI

| Veri Boyutu | Toplam Süre |
|-----------|-----------|
| 1000 | ~1 saniye |
| 10000 | ~10 saniye |
| 100000 | ~2 dakika |
| **Tüm Benchmark** | **~3 dakika** |

---

## 19. DOSYA BAŞLATMA SÜTUNLARI

```
Başlat için:                      Çalıştır:
──────────────────────────────────────────
Benchmark                         python main.py
GUI                              python gui/app.py
Time Grafiği                      python visualization/time_comparison.py
Memory Grafiği                    python visualization/memory_comparison.py
```

---

## 20. KISİ AŞAMALAR (Learning Path)

```
1. algorithms/ → Algoritmaları anla (basit)
2. data/ → Veri üretimini gör
3. benchmark/ → Ölçüm metriklerini öğren
4. results/ → CSV çıktılarını incele
5. analysis/ → Teorik bilgiyi karşılaştır
6. visualization/ → Grafikleri oluştur
7. gui/ → Etkileşimli interface'i kullan
8. report/ → Bulgularını yazı olarak özetle
```

