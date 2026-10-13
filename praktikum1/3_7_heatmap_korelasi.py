# ==============================================================================
# SUB-BAB 3.7: HEATMAP KORELASI (SEABORN)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Heatmap adalah tabel korelasi yang "DIBERI WARNA CERDAS":
   - Kotak Merah / Hangat = Hubungannya SEARAH dan KUAT (korelasi positif mendekati +1.0).
     (Jika A naik, B ikut naik).
   - Kotak Biru / Dingin  = Hubungannya BERLAWANAN ARAH (korelasi negatif mendekati -1.0).
     (Jika A naik, B malah turun).
   - `annot=True`         = Menuliskan angka desimal korelasi di dalam masing-masing kotak agar jelas.

2. KENAPA KITA LEBIH SUKA HEATMAP DARIPADA TABEL ANGKA BIASA?
   Mata manusia malas membaca puluhan angka desimal kecil di tabel.
   Dengan Heatmap, cukup melihat sekilas: "Oh kotak merahnya menyala di pertemuan kolom UTS dan UAS!",
   maka kita langsung tahu kedua hal itulah yang paling erat hubungannya.

3. CONTOH DI DUNIA KERJA:
   - Rekomendasi Film di Netflix: Memetakan korelasi tontonan pengguna.
     Orang yang suka film Action superhero ternyata punya korelasi merah pekat dengan penonton film Sci-Fi luar angkasa,
     sehingga Netflix otomatis menyarankan film tersebut di beranda mereka.
   - Analis Saham: Menampilkan heatmap hubungan antar sektor industri (perbankan, energi, teknologi).
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Inisialisasi data (dari Sub-bab 2.1)
data = {
    "Nama"   : ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"],
    "JK"     : ["L", "L", "P", "P", "L", "L", "P"],
    "Usia"   : [19, 20, 18, 21, 20, 19, 20],
    "UTS"    : [78, 85, 92, 60, 70, 88, 75],
    "UAS"    : [80, 88, 95, 65, 72, 84, 90]
}
df = pd.DataFrame(data)

# --- Kode Sub-bab 3.7 ---
plt.figure(figsize=(6, 5))
sns.heatmap(
    df[["Usia", "UTS", "UAS"]].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    square=True,
    linewidths=0.5
)
plt.title("Heatmap Peta Warna Korelasi", fontsize=13, fontweight="bold")
plt.show()
