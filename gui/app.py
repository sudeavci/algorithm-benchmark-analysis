import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from turtle import mode
import customtkinter as ctk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import threading

from utils.table_saver import save_table_auto
from benchmark.runner import run_benchmark, DATA_SIZES
from visualization.tables import draw_results_table

# ================= MATPLOTLIB =================
matplotlib.use('TkAgg')
plt.style.use('dark_background')


# ================= THEORETICAL DATA =================

THEORETICAL_TIME = [
    ("Quick Sort", "O(n log n)", "O(n log n)", "O(n²)"),
    ("Merge Sort", "O(n log n)", "O(n log n)", "O(n log n)"),
    ("Heap Sort",  "O(n log n)", "O(n log n)", "O(n log n)"),
    ("Shell Sort", "~O(n^1.3)",  "~O(n^1.5)",  "O(n²)"),
    ("Radix Sort", "O(n)",       "O(n)",       "O(n)")
]

THEORETICAL_MEMORY = [
    ("Quick Sort", "O(log n)", "In-place"),
    ("Heap Sort",  "O(1)",     "In-place"),
    ("Shell Sort", "O(1)",     "In-place"),
    ("Merge Sort", "O(n)",     "Extra Memory"),
    ("Radix Sort", "O(n + k)", "Extra Memory")
]

THEORETICAL_SCORE = {
    "Quick Sort": 5,    # O(n^2)
    "Shell Sort": 4,    # ~O(n^1.5)
    "Merge Sort": 3,    # O(n log n)
    "Heap Sort": 3,     # O(n log n)
    "Radix Sort": 1     # O(n)
}


# === NORMALIZED THEORETICAL LEVELS (FOR CHARTS ONLY) ===
THEO_TIME_LEVEL = {
    "Radix Sort": 1,
    "Merge Sort": 3,
    "Heap Sort": 3,
    "Shell Sort": 4,
    "Quick Sort": 5
}

THEO_MEM_LEVEL = {
    "Quick Sort": 1,
    "Heap Sort": 1,
    "Shell Sort": 1,
    "Merge Sort": 5,
    "Radix Sort": 5
}



# === HUMAN-READABLE THEORETICAL DESCRIPTIONS ===
THEO_TIME_LABEL = {
    "Radix Sort": "O(n)",
    "Merge Sort": "O(n log n)",
    "Heap Sort": "O(n log n)",
    "Shell Sort": "~O(n^1.5)",
    "Quick Sort": "O(n²)"
}

THEO_MEM_LABEL = {
    "Quick Sort": "In-place (O(log n))",
    "Heap Sort": "In-place (O(1))",
    "Shell Sort": "In-place (O(1))",
    "Merge Sort": "Extra Memory (O(n))",
    "Radix Sort": "Extra Memory (O(n + k))"
}


# Matplotlib backend ayarları
matplotlib.use('TkAgg')
plt.style.use('dark_background')

# Proje kök dizinini yola ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



# --- TEMA AYARLARI ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Renk Paleti (Modern Tech)
COLORS = {
    "bg_dark": "#111827",      # Ana Arka Plan
    "panel_bg": "#1f2937",     # Panel Arka Planı
    "accent": "#7c3aed",       # Vurgu Rengi (Mor)
    "accent_hover": "#6d28d9", # Buton Hover
    "text": "#f3f4f6",         # Metin
    "chart_bg": "#1f2937"      # Grafik Arka Planı
}

class SortingGUI(ctk.CTk):
    def on_run_clicked(self):
        self.run_analysis()
        self.run_button.configure(state="disabled")
        self.status_label.configure(text="Benchmark çalışıyor...")

        t = threading.Thread(target=self.benchmark_worker, daemon=True)
        t.start()

    def open_single_algorithm_view(self):
        SingleAlgorithmGUI(self)


    def benchmark_worker(self):
        import time
        time.sleep(2)

        print(">>> THREAD BAŞLADI")

        # Eğer CSV varsa, benchmark çalıştırma
        if os.path.exists("../results/time_results.csv") and os.path.exists("../results/memory_results.csv"):
            print(">>> CSV VAR, BENCHMARK ATLANIYOR")
            self.after(0, self.update_ui_after_benchmark)
            return

        try:
            run_benchmark()
            print(">>> BENCHMARK BİTTİ")
            
            self.after(0, self.update_ui_after_benchmark)

        except Exception as e:
            print(">>> THREAD HATASI:", e)
            self.after(0, lambda: self.status_label.configure(text="Hata oluştu ❌"))

    def __init__(self):
        super().__init__()

        self.title("ALGO // Performance Analyzer")
        self.geometry("1300x850")
        self.configure(fg_color=COLORS["bg_dark"])

        # Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ================= SOL PANEL (SIDEBAR) =================
        self.sidebar = ctk.CTkFrame(self, width=280, corner_radius=0, fg_color=COLORS["panel_bg"])
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(10, weight=1)

        # -- LOGO --
        self.logo_label = ctk.CTkLabel(self.sidebar, text="ALGORITHMS\nBENCHMARK", 
                                     font=ctk.CTkFont(family="Roboto", size=24, weight="bold"),
                                     text_color=COLORS["accent"])
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 20))

        # -- STATUS --
        self.status_label = ctk.CTkLabel(self.sidebar, text="", 
                                       font=ctk.CTkFont(size=12),
                                       text_color="gray")
        self.status_label.grid(row=1, column=0, padx=20, pady=(0, 10))

        # -- AYARLAR --
        self.settings_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.settings_frame.grid(row=2, column=0, padx=10, sticky="ew")

        # 1. Analiz Modu
        self.create_label(self.settings_frame, "ANALYSIS MODE", 0)
        self.mode_menu = ctk.CTkOptionMenu(
            self.settings_frame, 
            values=[
                "Practical Analysis",
                "Theoretical Analysis",
                "Compare Analysis"
            ],
            fg_color=COLORS["accent"], 
            button_color=COLORS["accent_hover"],
            button_hover_color=COLORS["accent"],
            text_color="white"
        )
        self.mode_menu.set("Practical Analysis")  
        self.mode_menu.grid(row=1, column=0, padx=10, pady=(0, 15), sticky="ew")
        
        
        # 2. Veri Boyutu
        self.create_label(self.settings_frame, "DATA SIZE (N)", 2)
        self.size_menu = ctk.CTkOptionMenu(self.settings_frame, 
                                         values=[str(s) for s in DATA_SIZES],
                                         fg_color=COLORS["panel_bg"], 
                                         button_color=COLORS["panel_bg"],
                                         button_hover_color=COLORS["accent"],
                                         text_color="white",
                                         dropdown_fg_color=COLORS["panel_bg"])
        self.size_menu.set("10000")
        self.size_menu.grid(row=3, column=0, padx=10, pady=(0, 15), sticky="ew")

        # 3. Veri Tipi
        self.create_label(self.settings_frame, "DATA PATTERN", 4)
        self.dtype_menu = ctk.CTkOptionMenu(self.settings_frame, 
                                          values=["random", "reverse", "partial"],
                                          fg_color=COLORS["panel_bg"],
                                          button_color=COLORS["panel_bg"],
                                          button_hover_color=COLORS["accent"],
                                          dropdown_fg_color=COLORS["panel_bg"],
                                          text_color="white")
        self.dtype_menu.grid(row=5, column=0, padx=10, pady=(0, 15), sticky="ew")

        # 4. Algoritmalar
        self.create_label(self.settings_frame, "ALGORITHMS", 6)
        self.checkbox_frame = ctk.CTkFrame(self.settings_frame, fg_color="#374151", corner_radius=10)
        self.checkbox_frame.grid(row=7, column=0, padx=10, pady=(0, 20), sticky="ew")

        self.algorithms = ["Quick Sort", "Merge Sort", "Heap Sort", "Shell Sort", "Radix Sort"]
        self.check_vars = {}
        
        for i, alg in enumerate(self.algorithms):
            var = ctk.StringVar(value="on")
            cb = ctk.CTkCheckBox(self.checkbox_frame, text=alg, variable=var, 
                               onvalue="on", offvalue="off",
                               hover_color=COLORS["accent"], fg_color=COLORS["accent"],
                               font=ctk.CTkFont(size=12))
            cb.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            self.check_vars[alg] = var

        # -- BUTON --
        self.run_button = ctk.CTkButton(self.sidebar, text="START ANALYSIS  ▶", 
                                      command=self.on_run_clicked,
                                      height=50,
                                      font=ctk.CTkFont(size=14, weight="bold"),
                                      fg_color=COLORS["accent"], 
                                      hover_color=COLORS["accent_hover"],
                                      corner_radius=25)
        self.run_button.grid(row=9, column=0, padx=20, pady=20, sticky="ew")

        self.single_algo_btn = ctk.CTkButton(
            self.sidebar, 
            text="SINGLE ALGORITHM \nANALYSIS  ▶",
            command=self.open_single_algorithm_view,
            height=50,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#6d28d9",      # biraz farklı ton
            hover_color="#5b21b6",
            corner_radius=25
        )
        
        self.single_algo_btn.grid(row=10, column=0, padx=20, pady=(0, 20), sticky="ew")

        # ================= SAĞ PANEL =================
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_rowconfigure(0, weight=3)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # -- GRAFİK ALANI --
        self.plot_container = ctk.CTkFrame(self.main_frame, fg_color=COLORS["panel_bg"], corner_radius=15)
        self.plot_container.grid(row=0, column=0, sticky="nsew", pady=(0, 15))
        
        self.fig = Figure(figsize=(8, 6), dpi=100, facecolor=COLORS["panel_bg"])
        self.ax_time = self.fig.add_subplot(211)
        self.ax_mem = self.fig.add_subplot(212)
        
        self.ax_time.set_facecolor(COLORS["panel_bg"])
        self.ax_mem.set_facecolor(COLORS["panel_bg"])
        self.fig.subplots_adjust(hspace=0.4, top=0.9, bottom=0.1)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_container)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        # -- TABLO ALANI --
        self.table_container = ctk.CTkFrame(self.main_frame, fg_color=COLORS["panel_bg"], corner_radius=15)
        self.table_container.grid(row=1, column=0, sticky="nsew")
        
        self.fig_table = Figure(figsize=(8, 2), dpi=100, facecolor=COLORS["panel_bg"])
        self.ax_table = self.fig_table.add_subplot(111)
        self.ax_table.axis("off")
        
        self.canvas_table = FigureCanvasTkAgg(self.fig_table, master=self.table_container)
        self.canvas_table.draw()
        self.canvas_table.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

    def create_label(self, parent, text, row):
        label = ctk.CTkLabel(parent, text=text, 
                           font=ctk.CTkFont(size=11, weight="bold"),
                           text_color="gray")
        label.grid(row=row, column=0, padx=10, pady=(5, 2), sticky="w")

    def get_selected_algorithms(self):
        selected = []
        for alg, var in self.check_vars.items():
            if var.get() == "on":
                selected.append(alg)
        return selected

    def run_analysis(self):
        self.selected_algos = self.get_selected_algorithms()
        self.data_size = int(self.size_menu.get())
        self.data_type = self.dtype_menu.get()

        if not self.selected_algos:
            return

        self.ax_time.clear()
        self.ax_mem.clear()
        

    def update_ui_after_benchmark(self):
        print(">>> UI GÜNCELLENİYOR")
        mode = self.mode_menu.get()
        
        # ================= THEORETICAL ANALYSIS =================
        if mode == "Theoretical Analysis":
            self.ax_time.clear()
            self.ax_mem.clear()
            self.ax_table.clear()
            self.ax_table.axis("off")

            # === THEORETICAL GRAPH DATA ===
            algs = [a for a, _, _, _ in THEORETICAL_TIME]

            time_levels = [THEORETICAL_SCORE[a] for a in algs]
            mem_levels  = [THEO_MEM_LEVEL[a] for a in algs]

            bars1 = self.ax_time.bar(algs, time_levels, alpha=0.9)
            self.ax_time.set_title(
                "Theoretical Time Complexity (Normalized)",
                color="white",
                fontsize=10,
                weight="bold"
            )
            self.ax_time.set_ylabel("Complexity Level", color="gray")
            self.ax_time.set_yticks([1, 2, 3, 4, 5])
            self.ax_time.set_yticklabels(
                ["O(n)", "", "O(n log n)", "~O(n^1.5)", "O(n²)"],
                color="white"
            )
            self.ax_time.tick_params(colors="white")
            self.ax_time.grid(True, axis='y', linestyle=':', alpha=0.3)
            self.add_labels(self.ax_time, bars1)

            bars2 = self.ax_mem.bar(algs, mem_levels, alpha=0.9)
            self.ax_mem.set_title(
                "Theoretical Memory Usage",
                color="white",
                fontsize=10,
                weight="bold"
            )
            self.ax_mem.set_ylabel("Memory Type", color="gray")
            self.ax_mem.set_yticks([1, 5])
            self.ax_mem.set_yticklabels(
                ["In-place", "Extra Memory"],
                color="white"
            )
            self.ax_mem.tick_params(colors="white")
            self.ax_mem.grid(True, axis='y', linestyle=':', alpha=0.3)
            self.add_labels(self.ax_mem, bars2)

            # --- TIME COMPLEXITY TABLE ---
            time_data = [[a, b, c, d] for a, b, c, d in THEORETICAL_TIME]
            table1 = self.ax_table.table(
                cellText=time_data,
                colLabels=["Algorithm", "Best", "Average", "Worst"],
                loc="center",
                cellLoc="center"
            )
            table1.scale(1, 1.4)
            table1.auto_set_font_size(False)
            table1.set_fontsize(10)

            for (row, col), cell in table1.get_celld().items():
                cell.set_edgecolor(COLORS["panel_bg"])
                if row == 0:
                    cell.set_facecolor(COLORS["accent"])
                    cell.set_text_props(color='white', weight='bold')
                else:
                    cell.set_facecolor("#374151" if row % 2 == 0 else "#4b5563")
                    cell.set_text_props(color='white')

            self.ax_table.set_title(
                "Theoretical Time Complexity (Best / Average / Worst)",
                color="white",
                fontsize=12,
                pad=10
            )

            self.canvas_table.draw()
            self.canvas.draw()
            self.run_button.configure(state="normal")
            self.status_label.configure(text="")

            # === THEORETICAL TABLE AUTO SAVE ===
            theoretical_df = pd.DataFrame(
                THEORETICAL_TIME,
                columns=["Algorithm", "Best Case", "Average Case", "Worst Case"]
            )

            save_table_auto(
                theoretical_df,
                analysis_type="start_analysis",
                extra_info="theoretical_analysis"
            )
            return

        # ================= COMPARE ANALYSIS =================
        if mode == "Compare Analysis":
            self.ax_time.clear()
            self.ax_mem.clear()
            self.ax_table.clear()
            self.ax_table.axis("off")

            # --- PRACTICAL TIME DATA ---
            df_time = pd.read_csv("../results/time_results.csv")
            mask = (
                (df_time["Data Size"] == self.data_size) &
                (df_time["Data Type"] == self.data_type) &
                (df_time["Algorithm"].isin(self.selected_algos))
            )
            practical = df_time[mask]

            if practical.empty:
                return

            # === GRAPH 1: PRACTICAL EXECUTION TIME ===
            bars1 = self.ax_time.bar(
                practical["Algorithm"],
                practical["Time (ms)"],
                color="#60a5fa",
                alpha=0.9
            )
            self.ax_time.set_title(
                "Practical Execution Time",
                color="white",
                fontsize=10,
                weight="bold"
           )
            self.ax_time.set_ylabel("Time (ms)", color="gray")
            self.ax_time.tick_params(colors="white")
            self.ax_time.grid(True, axis='y', linestyle=':', alpha=0.3)
            self.add_labels(self.ax_time, bars1)

            # === GRAPH 2: THEORETICAL TIME (NORMALIZED) ===
            theoretical_vals = [THEORETICAL_SCORE[a] for a in practical["Algorithm"]]

            bars2 = self.ax_mem.bar(
                practical["Algorithm"],
                theoretical_vals,
                color="#f472b6",
                alpha=0.9
            )
            self.ax_mem.set_title(
                "Theoretical Time Complexity (Normalized)",
                color="white",
                fontsize=10,
                weight="bold"
            )
            self.ax_mem.set_ylabel("Complexity Level", color="gray")
            self.ax_mem.set_yticks([1, 2, 3, 4, 5])
            self.ax_mem.set_yticklabels(
                ["O(n)", "", "O(n log n)", "~O(n^1.5)", "O(n²)"],
                color="white"
            )
            self.ax_mem.tick_params(colors="white")
            self.ax_mem.grid(True, axis='y', linestyle=':', alpha=0.3)
            self.add_labels(self.ax_mem, bars2)


            # === TABLE: SUMMARY ===
            # --- READ PRACTICAL DATA ---
            df_time = pd.read_csv("../results/time_results.csv")
            df_mem = pd.read_csv("../results/memory_results.csv")

            mask_time = (
                (df_time["Data Size"] == self.data_size) &
                (df_time["Data Type"] == self.data_type) &
                (df_time["Algorithm"].isin(self.selected_algos))
            )
            mask_mem = (
                (df_mem["Data Size"] == self.data_size) &
                (df_mem["Data Type"] == self.data_type) &
                (df_mem["Algorithm"].isin(self.selected_algos))
            )

            t = df_time[mask_time]
            m = df_mem[mask_mem]

            compare_rows = []

            THEO_TIME_MAP = {
                "Quick Sort": "O(n²)",
                "Merge Sort": "O(n log n)",
                "Heap Sort": "O(n log n)",
                "Shell Sort": "~O(n^1.5)",
                "Radix Sort": "O(n)"
            }

            INPLACE_SET = {"Quick Sort", "Heap Sort", "Shell Sort"}

            for alg in t["Algorithm"]:
                practical_time = t[t["Algorithm"] == alg]["Time (ms)"].values[0]
                practical_mem = m[m["Algorithm"] == alg]["Memory (KB)"].values[0]

                memory_label = "Low" if alg in INPLACE_SET else "High"
                inplace_label = "✔" if alg in INPLACE_SET else "✖"

                compare_rows.append([
                    alg,
                    THEO_TIME_LABEL[alg],
                    f"{practical_time:.2f} ms",
                    THEO_MEM_LABEL[alg],
                    "✔" if alg in INPLACE_SET else "✖"
                ])

            table = self.ax_table.table(
                cellText=compare_rows,
                colLabels=["Algorithm", "Theoretical Time", "Practical Time", "Memory Usage", "In-place"],
                loc="center",
                cellLoc="center"
            )
            table.scale(1, 1.4)
            table.auto_set_font_size(False)
            table.set_fontsize(10)

            for (row, col), cell in table.get_celld().items():
                cell.set_edgecolor(COLORS["panel_bg"])
                if row == 0:
                    cell.set_facecolor(COLORS["accent"])
                    cell.set_text_props(color='white', weight='bold')
                else:
                    cell.set_facecolor("#374151" if row % 2 == 0 else "#4b5563")
                    cell.set_text_props(color='white')

            self.ax_table.set_title(
                "Comparison of Theoretical and Practical Results",
                color="white",
                fontsize=12,
                pad=10
            )
            self.canvas.draw()
            self.canvas_table.draw()
            self.run_button.configure(state="normal")
            self.status_label.configure(text="")

            # === COMPARE ANALYSIS TABLE AUTO SAVE ===
            compare_df = pd.DataFrame(
                compare_rows,
                columns=[
                    "Algorithm",
                    "Theoretical Time",
                    "Practical Time",
                    "Memory Usage",
                    "In-place"
                ]
            )

            save_table_auto(
                compare_df,
                analysis_type="start_analysis",
                extra_info=f"compare_{self.data_type}_N{self.data_size}"
            )
            return

        try:
            df_time = pd.read_csv("../results/time_results.csv")
            df_mem = pd.read_csv("../results/memory_results.csv")

            print(">>> CSV OKUNDU")

            
            mask_time = (df_time["Data Size"] == self.data_size) & \
                        (df_time["Data Type"] == self.data_type) & \
                        (df_time["Algorithm"].isin(self.selected_algos))
            
            mask_mem = (df_mem["Data Size"] == self.data_size) & \
                       (df_mem["Data Type"] == self.data_type) & \
                       (df_mem["Algorithm"].isin(self.selected_algos))
            
            filtered_time = df_time[mask_time]
            filtered_mem = df_mem[mask_mem]

            print(f">>> Seçili Algoritmalar: {self.selected_algos}")
            print(f">>> Veri Boyutu: {self.data_size}, Tip: {self.data_type}")
            print(f">>> Filtrelenmiş Zaman Verisi: {len(filtered_time)} satır")
            print(f">>> Filtrelenmiş Bellek Verisi: {len(filtered_mem)} satır")

            bar_colors = ['#3b82f6', '#8b5cf6', '#ec4899', '#10b981', '#f59e0b']

            # Zaman Grafiği
            bars1 = self.ax_time.bar(filtered_time["Algorithm"], filtered_time["Time (ms)"], 
                                   color=bar_colors[:len(filtered_time)], alpha=0.9)
            self.ax_time.set_title(f"EXECUTION TIME ({self.data_type} | N={self.data_size})", color="white", fontsize=10, weight='bold')
            self.ax_time.set_ylabel("Time (ms)", color="gray")
            self.ax_time.tick_params(colors='white')
            self.ax_time.grid(True, axis='y', linestyle=':', alpha=0.3, color='gray')
            self.add_labels(self.ax_time, bars1)

            # Bellek Grafiği
            bars2 = self.ax_mem.bar(filtered_mem["Algorithm"], filtered_mem["Memory (KB)"], 
                                  color=bar_colors[:len(filtered_mem)], alpha=0.9)
            self.ax_mem.set_title(f"MEMORY USAGE ({self.data_type} | N={self.data_size})", color="white", fontsize=10, weight='bold')
            self.ax_mem.set_ylabel("Peak Memory (KB)", color="gray")
            self.ax_mem.tick_params(colors='white')
            self.ax_mem.grid(True, axis='y', linestyle=':', alpha=0.3, color='gray')
            self.add_labels(self.ax_mem, bars2)

            self.canvas.draw()
            self.update()

            # Tablo
            merged_df = pd.merge(filtered_time, filtered_mem, on=["Algorithm", "Data Size", "Data Type"])
            display_df = merged_df[["Algorithm", "Time (ms)", "Memory (KB)"]]
            
            self.ax_table.clear()
            self.ax_table.axis('off')
            
            if not display_df.empty:
                cell_text = []
                for row in display_df.itertuples(index=False):
                    cell_text.append([str(x) for x in row])
                
                col_labels = display_df.columns.tolist()
                
                table = self.ax_table.table(cellText=cell_text, colLabels=col_labels, 
                                          loc='center', cellLoc='center', 
                                          colWidths=[0.3, 0.3, 0.3])
                
                table.auto_set_font_size(False)
                table.set_fontsize(10)
                table.scale(1, 1.3)
                
                for (row, col), cell in table.get_celld().items():
                    cell.set_edgecolor(COLORS["panel_bg"])
                    if row == 0:
                        cell.set_facecolor(COLORS["accent"])
                        cell.set_text_props(color='white', weight='bold')
                    else:
                        cell.set_facecolor("#374151" if row % 2 == 0 else "#4b5563")
                        cell.set_text_props(color='white')

            self.canvas_table.draw()
            self.update()

            # Tabloyu otomatik kaydet
            save_table_auto(
                display_df,
                analysis_type="start_analysis",
                extra_info=f"{self.data_type}_N{self.data_size}"
            )

            # Başarılı olursa button'u enable et ve status'ı temizle
            self.run_button.configure(state="normal")
            self.status_label.configure(text="")

        except Exception as e:
            print(">>> UI HATASI:", e)

            self.status_label.configure(text="Çıktı üretilemedi ❌")
            self.run_button.configure(state="normal")


    def add_labels(self, ax, bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}',
                    ha='center', va='bottom', color='white', fontsize=9)
            
class SingleAlgorithmGUI(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Single Algorithm Analysis")
        self.geometry("900x600")
        self.configure(fg_color=COLORS["bg_dark"])

        self.algorithm_var = tk.StringVar(value="Quick Sort")
        self.mode_var = tk.StringVar(value="Compare Sizes")
        self.pattern_var = tk.StringVar(value="random")
        self.size_var = tk.StringVar(value="10000")

        # === TOP CONTROLS ===
        control_frame = ctk.CTkFrame(self, fg_color=COLORS["panel_bg"])
        control_frame.pack(fill="x", padx=20, pady=15)

        ctk.CTkLabel(control_frame, text="Algorithm").grid(row=0, column=0, padx=10)
        ctk.CTkOptionMenu(
            control_frame,
            values=["Quick Sort", "Merge Sort", "Heap Sort", "Shell Sort", "Radix Sort"],
            variable=self.algorithm_var
        ).grid(row=1, column=0, padx=10)

        ctk.CTkLabel(control_frame, text="Mode").grid(row=0, column=1, padx=10)
        ctk.CTkOptionMenu(
            control_frame,
            values=["Compare Sizes", "Compare Patterns"],
            variable=self.mode_var,
            command=self.on_mode_change
        ).grid(row=1, column=1, padx=10)

        ctk.CTkLabel(control_frame, text="Pattern").grid(row=0, column=2, padx=10)
        self.pattern_menu = ctk.CTkOptionMenu(
            control_frame,
            values=["random", "partial", "reverse"],
            variable=self.pattern_var
        )
        self.pattern_menu.grid(row=1, column=2, padx=10)

        ctk.CTkLabel(control_frame, text="Size").grid(row=0, column=3, padx=10)
        self.size_menu = ctk.CTkOptionMenu(
            control_frame,
            values=[str(s) for s in DATA_SIZES],
            variable=self.size_var
        )
        self.size_menu.grid(row=1, column=3, padx=10)

        # === MAIN FRAME ===
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # === PLOT ===
        self.fig = Figure(figsize=(6, 4), dpi=100, facecolor=COLORS["panel_bg"])
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor(COLORS["panel_bg"])

        canvas = FigureCanvasTkAgg(self.fig, master=main_frame)
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.canvas = canvas

        # === TABLE ===
        self.fig_table = Figure(figsize=(6, 2), dpi=100, facecolor=COLORS["panel_bg"])
        self.ax_table = self.fig_table.add_subplot(111)
        self.ax_table.axis("off")

        self.canvas_table = FigureCanvasTkAgg(self.fig_table, master=main_frame)
        self.canvas_table.get_tk_widget().grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        main_frame.grid_rowconfigure(0, weight=3)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # === RUN BUTTON ===
        ctk.CTkButton(
            self,
            text="RUN SINGLE ANALYSIS",
            command=self.run_single_analysis,
            fg_color=COLORS["accent"],
            hover_color=COLORS["accent_hover"]
        ).pack(pady=10)

        self.on_mode_change()

    def on_mode_change(self, *_):
        if self.mode_var.get() == "Compare Sizes":
            self.pattern_menu.configure(state="normal")
            self.size_menu.configure(state="disabled")
        else:
            self.pattern_menu.configure(state="disabled")
            self.size_menu.configure(state="normal")

    def run_single_analysis(self):
        df = pd.read_csv("../results/time_results.csv")

        algo = self.algorithm_var.get()
        mode = self.mode_var.get()

        # === GRAFİK TEMİZLE ===
        self.ax.clear()

        # === TABLO TEMİZLE ===
        self.ax_table.clear()
        self.ax_table.axis("off")

        if mode == "Compare Sizes":
            # === SABİT PATTERN, SADECE 3 SIZE ===
            pattern = self.pattern_var.get()
            sizes = [1000, 10000, 100000]

            data = df[
                (df["Algorithm"] == algo) &
                (df["Data Type"] == pattern) &
                (df["Data Size"].isin(sizes))
            ].sort_values("Data Size")

            # --- BAR CHART ---
            self.ax.bar(
                data["Data Size"].astype(str),
                data["Time (ms)"],
                color="#60a5fa"
            )

            self.ax.set_xlabel("Data Size (N)")
            self.ax.set_title(f"{algo} | Pattern = {pattern}")

            # --- TABLE DATA ---
            table_data = [
                [algo,pattern, int(row["Data Size"]), f'{row["Time (ms)"]:.3f}']
                for _, row in data.iterrows()
            ]
            col_labels = ["Algorithm","Data Pattern", "Data Size (N)", "Time (ms)"]

        else:
            # === SABİT SIZE, PATTERN KARŞILAŞTIR ===
            size = int(self.size_var.get())

            data = df[
                (df["Algorithm"] == algo) &
                (df["Data Size"] == size)
            ]

            # --- BAR CHART ---
            self.ax.bar(
                data["Data Type"],
                data["Time (ms)"],
                color="#34d399"
            )

            self.ax.set_xlabel("Data Pattern")
            self.ax.set_title(f"{algo} | N = {size}")

            # --- TABLE DATA ---
            table_data = [
                [algo,size, row["Data Type"], f'{row["Time (ms)"]:.3f}']
                for _, row in data.iterrows()
            ]
            col_labels = ["Algorithm", "Data Size (N)", "Data Pattern", "Time (ms)"]

        # === GRAFİK ORTAK AYARLAR ===
        self.ax.set_ylabel("Time (ms)")
        self.ax.grid(True, axis="y", linestyle=":", alpha=0.3)
        self.canvas.draw()

        # === TABLO ÇİZ ===
        table = self.ax_table.table(
            cellText=table_data,
            colLabels=col_labels,
            loc="center",
            cellLoc="center"
        )
        
        table.scale(1, 1.4)
        table.auto_set_font_size(False)
        table.set_fontsize(10)

        # --- TABLO STİL ---
        for (row, col), cell in table.get_celld().items():
            cell.set_edgecolor(COLORS["panel_bg"])
            if row == 0:
                cell.set_facecolor(COLORS["accent"])
                cell.set_text_props(color="white", weight="bold")
            else:
                cell.set_facecolor("#374151" if row % 2 == 0 else "#4b5563")
                cell.set_text_props(color="white")

        self.canvas_table.draw()

        # Tabloyu otomatik kaydet
        save_table_auto(
            pd.DataFrame(table_data, columns=col_labels),
            analysis_type="single_algorithm",
            extra_info=f"{algo}_{self.mode_var.get()}"
        )


if __name__ == "__main__":
    app = SortingGUI()
    app.mainloop()