# ALGO Projesi - Detaylı Teknik Analiz

**Proje Türü:** Sıralama Algoritmalarının Performans Analiz Sistemi  
**Dil:** Python 3  
**Tarih:** 2025

---

## 1. PROJE ÖZETİ

Bu proje **5 farklı sıralama algoritmasının** (Quick Sort, Merge Sort, Heap Sort, Shell Sort, Radix Sort) gerçek zamanlı performansını ölçen ve analiz eden kapsamlı bir sistem. Teorik karmaşıklık hesaplamaları ile praktik benchmark sonuçlarını karşılaştırarak bilgisayar bilimi eğitim amaçlı kullanılıyor.

**Ana Hedefler:**
- Algoritmaların zaman karmaşıklığını pratik ölçülü
- Bellek kullanımını analiz etme
- Farklı veri desenleri (random, partially sorted, reverse) üzerinde performans inceleme
- GUI aracılığıyla interaktif görselleştirme
- Teorik vs Pratik karşılaştırma

---

## 2. PROJE YAPISI

```
ALGO/
├── main.py                          # Giriş noktası
├── requirements.txt                 # Python bağımlılıkları
├── README.md                        # Proje dokümantasyonu (boş)
│
├── algorithms/                      # SIRALAMAALGORITMASI UYGULAMALARI
│   ├── __init__.py                  # Python package marker
│   ├── quick_sort.py                # Hızlı Sırala (Randomized)
│   ├── merge_sort.py                # Birleştirmeli Sırala
│   ├── heap_sort.py                 # Yığın Sırala
│   ├── shell_sort.py                # Shell Sırala
│   └── radix_sort.py                # Radix Sırala (Sayı-tabanlı)
│
├── analysis/                        # TEORIK ANALİZ
│   └── theoretical_analysis.py      # Zaman/Alan Kompleksitesi Definisyonları
│
├── benchmark/                       # PERFORMANS ÖLÇÜMÜ
│   ├── __init__.py
│   ├── runner.py                    # Benchmark yöneticisi
│   ├── time_analysis.py             # Yürütme süresi ölçümü
│   └── memory_analysis.py           # Bellek kullanım ölçümü
│
├── data/                            # VERİ ÜRETİCİSİ
│   └── generator.py                 # Test veri setleri oluşturma
│
├── gui/                             # KULLANICI ARABIRIMI
│   ├── app.py                       # Tkinter GUI uygulaması
│   └── tempCodeRunnerFile.py        # Geçici dosya (görmezden gel)
│
├── visualization/                   # GRAFİK VİZÜALİZASYON
│   ├── time_comparison.py           # Zaman karşılaştırma grafikleri
│   ├── memory_comparison.py         # Bellek karşılaştırma grafikleri
│   ├── pattern_comparison.py        # Veri deseni karşılaştırması
│   ├── algorithm_pattern_comparison.py # Algoritma vs Desen
│   ├── plot_time.py                 # Matplotlib zaman grafikleri
│   ├── plot_memory.py               # Matplotlib bellek grafikleri
│   ├── sort_animation.py            # Sıralama animasyonu (eksik)
│   └── tables.py                    # Tablo oluşturma (boş)
│
├── results/                         # KAYDEDİLEN SONUÇLAR
│   ├── time_results.csv             # Zaman ölçüm verileri
│   └── memory_results.csv           # Bellek ölçüm verileri
│
└── report/                          # RAPOR VE ÖZETLERİ
    ├── theoretical_vs_practical.md  # Analiz raporu
    └── figures/                     # Kaydedilen grafikler
```

---

## 3. DOSYA AÇIKLAMALARI

### 3.1 GİRİŞ NOKTASI: `main.py`
```python
from benchmark.runner import run_benchmark

if __name__ == "__main__":
    run_benchmark()
```
**Amaç:** Projenin ana giriş noktası  
**İşlev:** Benchmark runner modülünü çalıştırır, tüm algoritmaları test eder  
**Çalıştırma:** `python main.py`

---

### 3.2 BAĞIMLILLIKLAR: `requirements.txt`
```
matplotlib>=3.5.0      # Grafik çizim kütüphanesi
numpy>=1.19.0          # Matematiksel hesaplamalar
```
**Bağlantılı paketler:** pandas, tkinter (standart)

---

## 4. ALGORITMA UYGULAMALARI (`algorithms/`)

### 4.1 `quick_sort.py` - Hızlı Sırala (Randomized)

**Karmaşıklık:**
- Best/Average: O(n log n)
- Worst: O(n²)
- Space: O(log n) [recursive stack]

**Uygulama Detayları:**
- **Public Interface:** `quick_sort(arr: list) -> list`
  - Giriş: Sıralanacak liste
  - Çıkış: Yeni sıralanmış liste
  - İç işlem: Orijinal listeyi kopyalayıp modifiye eder

- **Private Functions:**
  - `_quick_sort(arr, low, high)`: Recursive sıralama
  - `_random_partition(arr, low, high)`: Rastgele pivot seçimi
    - Pivot randomization **worst case'i önlemek** için kullanılır
  - `_partition(arr, low, high)`: Pivot etrafında bölme

**Pivot Stratejisi:** Rastgele seçim (Randomized Quicksort)  
**İn-Place:** Evet (bellek verimli)  
**Stabil:** Hayır

---

### 4.2 `merge_sort.py` - Birleştirmeli Sırala

**Karmaşıklık:**
- Best/Average/Worst: O(n log n) ✓ **Garantili**
- Space: O(n) [auxiliary array]

**Uygulama Detayları:**
- **Public Interface:** `merge_sort(arr: list) -> list`
- **Strategi:** Böl-ve-yönet (Divide and Conquer)
  1. Dizi ortasından bölün
  2. Sol ve sağ tarafı recursive sıralayın
  3. Sıralı iki yarıyı birleştirin

- **Private Functions:**
  - `_merge(left, right)`: İki sıralı diziyi birleştir
    - İşaretçi tekniği: `i` ve `j` ile karşılaştırma
    - Stabil birleştirme (eşit elemanlar sırasını korur)

**İn-Place:** Hayır (ekstra bellek gerekli)  
**Stabil:** Evet ✓  
**Avantaj:** Tahmin edilebilir O(n log n) performans

---

### 4.3 `heap_sort.py` - Yığın Sırala

**Karmaşıklık:**
- Best/Average/Worst: O(n log n) ✓
- Space: O(1) [in-place]

**Uygulama Detayları:**
- **Public Interface:** `heap_sort(arr: list) -> list`
- **Aşamalar:**
  1. **Max Heap İnşa:** n/2 - 1 index'ten başlayıp geriye doğru heapify
  2. **Extraction:** En büyük elemanı (root) sona taşı, yığını küçült, tekrarla

- **Private Functions:**
  - `_heapify(arr, heap_size, root_index)`: Max heap özelliğini sağla
    - Recursive olarak ağaç yapısını düzenle
    - Left child: 2*i + 1
    - Right child: 2*i + 2

**İn-Place:** Evet  
**Stabil:** Hayır

---

### 4.4 `shell_sort.py` - Shell Sırala

**Karmaşıklık:**
- Best: O(n log n)
- Average: O(n^1.25) [gap sequence bağlı]
- Worst: O(n²)
- Space: O(1)

**Uygulama Detayları:**
- **Public Interface:** `shell_sort(arr: list) -> list`
- **Gap Sequence:** `gap = n/2; gap = gap/2; ...`
  - Her iterasyonda elemeler daha da yakın aralıklarla sıralanır
  - Son iterasyon = Insertion Sort (1-spaced)

- **Mantık:**
  1. Farklı aralıklarla subarray'leri sırala (shell'ler)
  2. Gap'i yarıya düşür
  3. Tekrarla

**İn-Place:** Evet  
**Stabil:** Hayır  
**Avantaj:** Partially sorted veri üzerinde çok hızlı

---

### 4.5 `radix_sort.py` - Radix Sırala (LSD)

**Karmaşıklık:**
- Best/Average/Worst: O(nk) [k = digit sayısı]
- Space: O(n + 10) [10 bucket]
- **Önemli:** Comparison-based DEĞILDIR

**Uygulama Detayları:**
- **Public Interface:** `radix_sort(arr: list) -> list`
- **Kısıtlama:** Yalnızca **negatif olmayan integer'lar** için
- **Algoritma (LSD = Least Significant Digit):**
  1. En az anlamlı rakam'dan en önemli'ye doğru sırala
  2. Her digit için counting sort uygulanır
  3. Stabil olmasına önem verilir

- **Private Functions:**
  - `_counting_sort(arr, exp)`: Spesifik digit için sayma sıralaması
    - `exp = 1, 10, 100, ...`
    - Stable counting: Sağdan sola backtrack (order korunur)

**İn-Place:** Hayır (output array gerekli)  
**Stabil:** Evet ✓  
**Avantaj:** Integer dataset'lerde çok hızlı

---

## 5. ANALİZ MODÜLÜ (`analysis/`)

### `theoretical_analysis.py`

**Amaç:** Saf teorik bilgi depolaması, hiçbir ölçüm yapmayan sabit veri  

**Yapı:** `THEORETICAL_INFO` dictionary
```python
{
    "Algorithm Name": {
        "best_case": "O(...)",
        "average_case": "O(...)",
        "worst_case": "O(...)",
        "space_complexity": "O(...)",
        "notes": "Açıklama..."
    }
}
```

**Helper Functions:**
- `get_algorithm_names()`: Algoritma isimlerinin listesi
- `get_theoretical_info(name)`: Spesifik algoritmanın bilgisi
- `format_theoretical_text(name)`: GUI gösterimi için formatlanmış metin

**Kullanım:** GUI'de teorik karmaşıklık göstermek için

---

## 6. BENCHMARK MODÜLÜ (`benchmark/`)

### 6.1 `runner.py` - Ana Benchmark Yöneticisi

**Ana İşlev:** `run_benchmark()`

**Parameterler:**
```python
DATA_SIZES = [1000, 10000, 100000]
DATA_TYPES = ["random", "partial", "reverse"]
```

**Akış:**
```
Her DATA_SIZE için:
  Her DATA_TYPE için:
    Her ALGORITMA için:
      - Veri üret (generate_dataset)
      - Zamanı ölç (measure_time)
      - Belleği ölç (measure_memory)
      - Sonuçları listeye ekle
      
→ CSV dosyalarına kaydet
```

**Önemli:** Radix Sort negatif veri filtrelemesi

**Çıktı Dosyaları:**
- `results/time_results.csv`: Algorithm | Data Size | Data Type | Time (ms)
- `results/memory_results.csv`: Algorithm | Data Size | Data Type | Memory (KB)

---

### 6.2 `time_analysis.py` - Zaman Ölçümü

```python
def measure_time(sort_function, data: list, runs: int = 3) -> float
```

**İşlem:**
1. Belirtilen sayıda (`runs`) test çalıştır
2. Her çalıştırmada: `time.perf_counter()` ile başlangıç-bitiş kaydı
3. Toplam zamanı ortalama al
4. Milisaniyeye çevir

**Niçin 3 runs?** Tutarsızlıkları azaltmak için ortalama alır

---

### 6.3 `memory_analysis.py` - Bellek Ölçümü

```python
def measure_memory(sort_function, data: list) -> float
```

**İşlem:**
1. `tracemalloc.start()` - izleme başla
2. Fonksiyonu çalıştır
3. `tracemalloc.get_traced_memory()` - pik bellek al
4. Byte'tan KB'ye çevir (÷1024)

**Neden pik?** Algoritmanın en çok bellek kullandığı an ölçüldü

---

## 7. VERİ ÜRETİCİSİ (`data/generator.py`)

### Amaç
Farklı senaryolarda algoritmaları test etmek için temsili veri setleri oluştur

### Fonksiyonlar

#### 7.1 `generate_random(size: int) -> list`
```python
[random.randint(0, size * 10) for _ in range(size)]
```
- Tam rastgele, başka hiçbir sipariş yok
- Ortalama durum testi için ideal

#### 7.2 `generate_reverse(size: int) -> list`
```python
list(range(size, 0, -1))
```
- Tamamen ters sıralı: [n, n-1, n-2, ..., 1]
- **En kötü durum testleri:** Quicksort O(n²), Shell/Merge O(n log n)

#### 7.3 `generate_partially_sorted(size: int, sorted_ratio: float = 0.7) -> list`
```python
sorted_part + random_part
```
- %70 sıralı, %30 rastgele
- Gerçek dünya senaryosu (çoğu veri kısmen sıralanmış)
- **Shell Sort'u avantajlı hale getirir**

#### 7.4 `generate_best_case(size: int) -> list` (Kullanılmayan)
```python
list(range(size))
```
- En iyi durum: Tamamen sıralı
- Benchmarkta kullanılmıyor, ama örnek için var

---

## 8. GUI UYGULAMASI (`gui/app.py`)

**Framework:** Tkinter (Python standart UI kütüphanesi)

### 8.1 Mimarı

```
SortingGUI (tk.Tk)
├── Header (başlık ve açıklama)
├── Control Frame (ayarlar ve butonlar)
│   ├── Analiz Modu Seçimi (Practical/Theoretical/Comparison)
│   ├── Algoritma Seçimi (Dropdown)
│   ├── Veri Boyutu (Spinbox: 1000-100000)
│   ├── Tümü Karşılaştır (Checkbox)
│   └── Run/Show Butonu
└── Plot Area (matplotlib canvas)
    ├── ax_time (zaman grafiği)
    └── ax_memory (bellek grafiği)
```

### 8.2 Tema Sistemi

**LIGHT Theme:**
```python
{
    "bg": "#f5f6fa",              # Açık gri arka plan
    "card": "#ffffff",             # Beyaz kontrol paneli
    "text": "#111827",             # Koyu metin
    "button": "#6d28d9"            # Mor buton
}
```

**DARK Theme:** Ters renkler

### 8.3 Analiz Modları

#### Practical Mode
```
Seçilen algoritmanın farklı veri desenleri üzerinde performansını göster
→ Grafik: X=Veri Deseni(random/partial/reverse), Y=Zaman(ms)
```

#### Theoretical Mode
```
Algoritmanın Big-O karmaşıklığını teorik olarak göster
→ Metin: Best/Average/Worst case, Bellek, Açıklama
```

#### Comparison Mode
```
Tüm algoritmaları karşılaştır
→ Üst Grafik: Zamanı karşılaştır
→ Alt Grafik: Belleği karşılaştır
```

### 8.4 İnteraksiyon Detayları

**Compare All Checkbox:**
- Checkbox işaretli → Algorithm dropdown devre dışı, tüm algoritmalar göster
- Checkbox boş → Tek algoritma seç

**Data Size Spinbox:**
- 1000 - 100000 arası seçim
- Default: 10000

---

## 9. VİZÜALİZASYON MODÜLLERI (`visualization/`)

### 9.1 `time_comparison.py`

```python
def plot_time_comparison(data_size=10000, data_type="random")
```

- **Girdi:** CSV dosyasından filtrele (belirtilen boyut ve tür)
- **Çıktı:** Bar grafiği (Algoritma vs Zaman)
- **Dosya:** `report/figures/time_comparison_{type}_{size}.png`

### 9.2 `memory_comparison.py`

```python
def plot_memory_comparison(data_size=10000, data_type="random")
```

- **Grafik:** Bar chart (Algoritma vs Bellek KB)
- **Renk:** In-place (yeşil) vs Non-in-place (kırmızı) ayırması yapılabilir

### 9.3 `pattern_comparison.py`

```python
def plot_pattern_comparison(algorithm="Quick Sort", data_size=10000)
```

- **X-Axis:** Veri Desenleri (random, partial, reverse)
- **Y-Axis:** Zaman (ms)
- **Grafik:** Seçilen algoritmanın veri desenine göre duyarlılığı

### 9.4 `algorithm_pattern_comparison.py`

```python
def plot_algorithm_pattern_comparison(data_size=10000)
```

- **Bonus Görselleştirme**
- **Grafik:** Her algoritma için desenlere karşı çizgiler
- **Amacı:** Tüm algoritmaların veri desen duyarlılığını karşılaştırma

### 9.5 `plot_time.py` & `plot_memory.py`

- Etkileşimli matplotlib grafikler
- `.show()` ile ekranda açma
- GUI'den bağımsız

### 9.6 `sort_animation.py`

```python
def quick_sort_visual(arr)
```

- **Amaç:** Quicksort'un her adımını generator yield ediyor
- **Durum:** Eksik/Hatalı (kullanılmayan)
- **Hedefi:** Sıralama animasyonu göstermek

### 9.7 `tables.py`

- **Durum:** Boş dosya (henüz uygulanmadı)
- **Amaç:** CSV verisini tablo formatında göstermek

---

## 10. SONUÇ VERİLERİ (`results/`)

### 10.1 `time_results.csv`

Yapı:
```
Algorithm,Data Size,Data Type,Time (ms)
Quick Sort,1000,random,3.1019
Merge Sort,1000,random,2.1875
...
```

**Önemli Bulgular:**
- **Hızlı:** Radix Sort (doğru veri tipi için)
- **Stabil:** Merge Sort (her zaman O(n log n))
- **Worst Case:** Heap Sort (yüksek constant factor)
- **Bağlı-Veri:** Shell Sort (partially sorted'da iyi)

### 10.2 `memory_results.csv`

Yapı:
```
Algorithm,Data Size,Data Type,Memory (KB)
Quick Sort,1000,random,8.85
...
```

**Bulgular:**
- **In-Place (az bellek):** Quick Sort, Heap Sort, Shell Sort (~8 KB)
- **Non-In-Place (çok bellek):** Merge Sort, Radix Sort (~16 KB)
- **Ölçekleme:** Bellek ÷ Data Size = Sabit (doğru ölçüm)

---

## 11. RAPOR (`report/`)

### `theoretical_vs_practical.md`

Her algoritma için:
1. **Teorik Karmaşıklık:** Big-O notasyonu
2. **Praktik Gözlem:** Benchmark sonuçlarından çıkan gerçek davranış
3. **Uyum:** Teori ile uygulama arasındaki ilişki

**Örnek Bulgular:**
```
Quick Sort:
- Teorik: Ortalama O(n log n), En kötü O(n²)
- Praktik: Randomized pivot sayesinde ortalama duruma çok yakın
- Sonuç: Uyumlu

Merge Sort:
- Teorik: Her zaman O(n log n)
- Praktik: Yüksek bellek kullanması dışında tutarlı
- Sonuç: Uyumlu
```

---

## 12. VERI AKIŞI (Data Flow)

### Benchmark Çalıştırma Süreci

```
main.py
  ↓
runner.run_benchmark()
  ↓
  For each size, type, algorithm:
    ├─ generate_dataset(size, type) → data[]
    ├─ measure_time(algorithm, data) → time_ms
    ├─ measure_memory(algorithm, data) → memory_kb
    └─ Append to lists
  ↓
save_time_results() → results/time_results.csv
save_memory_results() → results/memory_results.csv
```

### GUI Kullanım Süresi

```
gui/app.py
  ↓
User seçim: Mode + Algorithm + Size
  ↓
update_view()
  ├─ practical mode:
  │   ├─ generate_dataset() × 3 (random/partial/reverse)
  │   ├─ measure_time() × 3
  │   └─ Zaman grafiği çiz
  │
  ├─ theoretical mode:
  │   └─ theoretical_analysis.format_theoretical_text()
  │
  └─ comparison mode:
      ├─ Tüm algoritmalar için measure_time()
      └─ İki grafik (zaman + bellek)
```

---

## 13. UYGULANMAYAN ÖZELLIKLER

- ❌ `sort_animation.py`: Eksik/Hatalı
- ❌ `tables.py`: Boş
- ❌ `README.md`: Boş

---

## 14. TEKNOLOJI YÖ

| Katman | Teknoloji | Amaç |
|--------|-----------|------|
| **Veri** | Python lists, random | Test veri üretimi |
| **Hesaplama** | Pure Python | Algoritma uygulaması |
| **Ölçüm** | time, tracemalloc | Performans metriği |
| **UI** | Tkinter | Etkileşimli arayüz |
| **Grafikler** | Matplotlib | Veri görselleştirme |
| **Veri Depolama** | CSV | Sonuç kaydı |
| **Analiz** | Pandas, NumPy | Veri işleme |

---

## 15. ÖNEMLİ KÓD ÖRNEKLERİ

### Benchmark Ayarları
```python
DATA_SIZES = [1000, 10000, 100000]          # 3 boyut
DATA_TYPES = ["random", "partial", "reverse"]  # 3 desen
ALGORITHMS = {5 algoritma}
# Toplam: 3 × 3 × 5 = 45 benchmark testi
```

### Zamanı Ölçme
```python
def measure_time(..., runs: int = 3):
    for _ in range(3):              # 3 kez çalıştır
        data_copy = data.copy()
        start = time.perf_counter()
        sort_function(data_copy)
        end = time.perf_counter()
        total_time += (end - start)
    return (total_time / 3) * 1000  # ms cinsinden ortalama
```

### Belleği Ölçme
```python
def measure_memory(...):
    tracemalloc.start()
    sort_function(data_copy)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024  # KB
```

---

## 16. KARMAŞIKLIK TABLOSU

| Algoritma | Best | Average | Worst | Space | In-Place | Stabil |
|-----------|------|---------|-------|-------|----------|--------|
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ✓ | ✗ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✗ | ✓ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ✓ | ✗ |
| Shell Sort | O(n log n) | O(n^1.5) | O(n²) | O(1) | ✓ | ✗ |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | ✗ | ✓ |

---

## 17. ÖZELLİKLER VE KIŞI TLAMALAR

### Güçlü Yönler
✅ Kapsamlı benchmark sistem  
✅ 5 farklı algoritma karşılaştırması  
✅ Teorik vs Pratik analiz  
✅ GUI aracılığıyla etkileşimli sorgu  
✅ Detaylı bellek ölçümü  

### Zayıf Yönler
❌ Sort animation eksik  
❌ Tablo görselleştirmesi boş  
❌ README dokümantasyonu yok  
❌ Negative number handling sınırlı  

---

## 18. KULLANIM TALIMATLAR

### 1. Benchmark Çalıştırma
```bash
cd /Users/aysebernabaysal/Downloads/ALGO
python main.py
# Sonuç: results/time_results.csv & results/memory_results.csv
```

### 2. GUI Başlatma
```bash
python gui/app.py
# Tkinter penceresi açılır, algoritmaları seçip test edebilirsin
```

### 3. Grafik Oluşturma
```bash
python visualization/time_comparison.py
python visualization/memory_comparison.py
# Grafikler report/figures/ klasörüne kaydedilir
```

---

## 19. SONUÇ

Bu proje **algoritma eğitimi ve performans analizi** için kapsamlı bir platform sağlar. Teorik karmaşıklık hesaplamalarını pratik ölçümlerle doğrulayarak, öğrencilerin Big-O notasyonunun gerçek anlamını görüntülemelerine yardımcı olur.

**Hedef Kullanıcı:** Bilgisayar Mühendisliği öğrencileri ve algoritma merakları

**Eğitim Değeri:**
- 5 farklı sıralama stratejisi karşılaştırması
- Zaman vs Bellek trade-off'ları
- Veri deseni etkisinin görülmesi
- Teorik karmaşıklık vs Pratik performans

