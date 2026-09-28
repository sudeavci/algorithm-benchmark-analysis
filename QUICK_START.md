# 🚀 Hızlı Başlangıç Kılavuzu

## ⚠️ ÖNEMLİ: Virtual Environment Kullanın!

macOS'ta Homebrew Python (`/opt/homebrew/bin/python3`) kullanmak sorun çıkarır çünkü tkinter desteği yoktur.

## ✅ Doğru Kullanım

### 1. Virtual Environment'ı Aktifleştirin

```bash
cd /Users/aysebernabaysal/Downloads/ALGO
source venv/bin/activate
```

**Başarılı aktifleştirme sonrası terminal'inizde `(venv)` yazısını görürsünüz:**

```bash
(venv) aysebernabaysal@192 ALGO %
```

### 2. Paket Yükleme (Gerekirse)

```bash
# Virtual environment aktifken
pip install -r requirements.txt
```

**⚠️ ASLA şunu yapmayın:**
```bash
# ❌ YANLIŞ - Homebrew Python kullanmayın!
/opt/homebrew/bin/python3 -m pip install ...
```

### 3. Programları Çalıştırma

```bash
# Virtual environment aktifken
python main.py          # Benchmark
python gui/app.py       # GUI
```

### 4. Virtual Environment'dan Çıkış (İsteğe Bağlı)

```bash
deactivate
```

## 🔍 Virtual Environment Aktif mi Kontrol Edin

Virtual environment aktifken:

```bash
which python
# Çıktı şöyle olmalı: /Users/aysebernabaysal/Downloads/ALGO/venv/bin/python
```

Eğer `/opt/homebrew/bin/python3` görüyorsanız, virtual environment aktif değil demektir!

## 📦 Yüklü Paketleri Kontrol Etme

```bash
# Virtual environment aktifken
pip list
```

Şu paketler yüklü olmalı:
- ✅ customtkinter
- ✅ matplotlib  
- ✅ numpy
- ✅ pillow
- ✅ packaging

## 💡 İpucu

Terminal'i her açtığınızda virtual environment'ı aktifleştirmeniz gerekir. Veya shell config dosyanıza (`.zshrc`) şunu ekleyebilirsiniz:

```bash
# ~/.zshrc dosyasına ekleyin
alias algo-activate='cd /Users/aysebernabaysal/Downloads/ALGO && source venv/bin/activate'
```

Sonra sadece şunu yazın:
```bash
algo-activate
```

