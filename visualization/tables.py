# ============================================
# visualization/tables.py
# CSV verilerini tablo formatında gösterir
# ============================================

import csv
import os
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingImports]
import customtkinter as ctk  # pyright: ignore[reportMissingImports]
from tkinter import ttk

# Renk paleti (app.py ile uyumlu)
COLORS = {
    "primary": "#6366F1",
    "dark_bg": "#1E1E2E",
    "card_bg": "#2D2D44",
    "text_primary": "#F8FAFC",
    "text_secondary": "#94A3B8",
    "border": "#3F3F5F",
}


def show_time_table(parent_window):
    """
    Zaman sonuçlarını CSV'den okuyup tablo olarak gösterir.
    """
    csv_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "results",
        "time_results.csv"
    )
    
    if not os.path.exists(csv_path):
        _show_error(parent_window, "Zaman sonuçları dosyası bulunamadı!")
        return
    
    # Yeni pencere oluştur
    window = ctk.CTkToplevel(parent_window)
    window.title("⏱️ Zaman Sonuçları Tablosu")
    window.geometry("900x600")
    window.configure(fg_color=COLORS["dark_bg"])
    
    # Başlık
    title = ctk.CTkLabel(
        window,
        text="⏱️ Zaman Performans Tablosu",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color=COLORS["text_primary"]
    )
    title.pack(pady=(20, 10))
    
    # Frame ve scrollbar için container
    container = ctk.CTkFrame(window, fg_color=COLORS["card_bg"])
    container.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    # Treeview (tablo)
    tree = ttk.Treeview(
        container,
        columns=("Algorithm", "Data Size", "Data Type", "Time (ms)"),
        show="headings",
        height=20
    )
    
    # Kolon başlıkları
    tree.heading("Algorithm", text="Algoritma")
    tree.heading("Data Size", text="Veri Boyutu")
    tree.heading("Data Type", text="Veri Tipi")
    tree.heading("Time (ms)", text="Süre (ms)")
    
    # Kolon genişlikleri
    tree.column("Algorithm", width=150, anchor="center")
    tree.column("Data Size", width=120, anchor="center")
    tree.column("Data Type", width=120, anchor="center")
    tree.column("Time (ms)", width=150, anchor="center")
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    # CSV'yi oku ve tabloya ekle
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tree.insert(
                    "",
                    "end",
                    values=(
                        row["Algorithm"],
                        f"{int(row['Data Size']):,}",
                        row["Data Type"],
                        f"{float(row['Time (ms)']):.4f}"
                    )
                )
    except Exception as e:
        _show_error(window, f"CSV okuma hatası: {e}")
        return
    
    # Layout
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Kapat butonu
    btn_close = ctk.CTkButton(
        window,
        text="Kapat",
        command=window.destroy,
        fg_color=COLORS["primary"],
        width=100
    )
    btn_close.pack(pady=(10, 20))


def show_memory_table(parent_window):
    """
    Bellek sonuçlarını CSV'den okuyup tablo olarak gösterir.
    """
    csv_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "results",
        "memory_results.csv"
    )
    
    if not os.path.exists(csv_path):
        _show_error(parent_window, "Bellek sonuçları dosyası bulunamadı!")
        return
    
    # Yeni pencere oluştur
    window = ctk.CTkToplevel(parent_window)
    window.title("💾 Bellek Sonuçları Tablosu")
    window.geometry("900x600")
    window.configure(fg_color=COLORS["dark_bg"])
    
    # Başlık
    title = ctk.CTkLabel(
        window,
        text="💾 Bellek Kullanım Tablosu",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color=COLORS["text_primary"]
    )
    title.pack(pady=(20, 10))
    
    # Frame ve scrollbar için container
    container = ctk.CTkFrame(window, fg_color=COLORS["card_bg"])
    container.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    # Treeview (tablo)
    tree = ttk.Treeview(
        container,
        columns=("Algorithm", "Data Size", "Data Type", "Memory (KB)"),
        show="headings",
        height=20
    )
    
    # Kolon başlıkları
    tree.heading("Algorithm", text="Algoritma")
    tree.heading("Data Size", text="Veri Boyutu")
    tree.heading("Data Type", text="Veri Tipi")
    tree.heading("Memory (KB)", text="Bellek (KB)")
    
    # Kolon genişlikleri
    tree.column("Algorithm", width=150, anchor="center")
    tree.column("Data Size", width=120, anchor="center")
    tree.column("Data Type", width=120, anchor="center")
    tree.column("Memory (KB)", width=150, anchor="center")
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    # CSV'yi oku ve tabloya ekle
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tree.insert(
                    "",
                    "end",
                    values=(
                        row["Algorithm"],
                        f"{int(row['Data Size']):,}",
                        row["Data Type"],
                        f"{float(row['Memory (KB)']):.2f}"
                    )
                )
    except Exception as e:
        _show_error(window, f"CSV okuma hatası: {e}")
        return
    
    # Layout
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Kapat butonu
    btn_close = ctk.CTkButton(
        window,
        text="Kapat",
        command=window.destroy,
        fg_color=COLORS["primary"],
        width=100
    )
    btn_close.pack(pady=(10, 20))


def draw_results_table(ax, result_file_path=None):
    """
    CSV dosyasını okur ve verilen Matplotlib Axes (ax) üzerine tablo çizer.
    
    Parameters:
        ax: Matplotlib Axes nesnesi
        result_file_path: CSV dosya yolu (None ise varsayılan yol kullanılır)
    """
    ax.clear()
    ax.axis('off')  # Eksen çizgilerini gizle

    # Varsayılan dosya yolu
    if result_file_path is None:
        result_file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "results",
            "time_results.csv"
        )

    # Dosya kontrolü
    if not os.path.exists(result_file_path):
        ax.text(0.5, 0.5, "Henüz sonuç verisi yok.\nLütfen benchmark çalıştırın.", 
                ha='center', va='center', fontsize=12)
        return

    data = []
    try:
        with open(result_file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)  # Başlığı al
            if header:
                data.append(header)
            
            # Satırları oku (En fazla 15 satır göster ki ekran taşmasın)
            rows = list(reader)
            # Sonuçları algoritmaya göre değil, süreye veya boyuta göre sıralamak mantıklı olabilir
            # Şimdilik olduğu gibi alıyoruz
            data.extend(rows[-15:])  # Son 15 testi göster
            
    except Exception as e:
        ax.text(0.5, 0.5, f"Veri okuma hatası:\n{str(e)}", ha='center', va='center')
        return

    if not data:
        return

    # Tabloyu oluştur
    table = ax.table(
        cellText=data,
        loc='center',
        cellLoc='center',
        colWidths=[0.25, 0.2, 0.2, 0.2]  # Sütun genişlikleri
    )

    # Tablo Stili
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)  # Satır yüksekliği

    # Başlık hücresi stili
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#4a4e69')  # Başlık rengi (Koyu mor)
        else:
            # Alternatif satır renklendirme (Zebra striping)
            if row % 2 == 0:
                cell.set_facecolor('#f2f2f2')
            else:
                cell.set_facecolor('#ffffff')

    ax.set_title("Son Benchmark Sonuçları", fontsize=14, pad=10)


def _show_error(parent_window, message: str):
    """Hata mesajı gösterir."""
    error_window = ctk.CTkToplevel(parent_window)
    error_window.title("Hata")
    error_window.geometry("400x150")
    error_window.configure(fg_color=COLORS["dark_bg"])
    
    label = ctk.CTkLabel(
        error_window,
        text=f"❌ {message}",
        font=ctk.CTkFont(size=14),
        text_color="#EF4444",
        wraplength=350
    )
    label.pack(pady=30)
    
    btn = ctk.CTkButton(
        error_window,
        text="Tamam",
        command=error_window.destroy,
        fg_color=COLORS["primary"]
    )
    btn.pack(pady=10)

