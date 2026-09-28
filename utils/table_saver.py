# utils/table_saver.py

import os
from datetime import datetime

def save_table_auto(df, analysis_type, extra_info=None):
    """
    df            : pandas DataFrame (kaydedilecek tablo)
    analysis_type : 'start_analysis' | 'single_algorithm'
    extra_info    : opsiyonel açıklama (algo, size, pattern vs.)
    """

    base_dir = "results/tables"
    os.makedirs(base_dir, exist_ok=True)

    save_dir = os.path.join(base_dir, analysis_type)
    os.makedirs(save_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if extra_info:
        filename = f"{analysis_type}_{extra_info}_{timestamp}.csv"
    else:
        filename = f"{analysis_type}_{timestamp}.csv"

    file_path = os.path.join(save_dir, filename)

    df.to_csv(file_path, index=False)

    print(f"[AUTO SAVE] Table saved -> {file_path}")
