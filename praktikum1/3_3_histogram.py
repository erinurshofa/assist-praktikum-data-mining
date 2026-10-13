# ==============================================================================
# SUB-BAB 3.3: HISTOGRAM DAN DISTRIBUSI DATA
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA BEDANYA HISTOGRAM DENGAN DIAGRAM BATANG BIASA?
   - Diagram Batang biasa : Membandingkan KATEGORI (misal: Laki-laki vs Perempuan). Batangnya biasanya ada celah terpisah.
   - Histogram : Mengelompokkan ANGKA KONTINU ke dalam beberapa "keranjang" (disebut `bins`).
     Batangnya menempel satu sama lain untuk melihat di mana angka-angka tersebut paling banyak menumpuk.
   - Contoh di kode ini: Nilai UTS dibagi menjadi 5 keranjang (misal: 60-66, 67-73, dst).
     Tinggi balok menunjukkan ADA BERAPA ORANG yang nilainya masuk ke dalam keranjang tersebut.

2. KENAPA HISTOGRAM PENTING?
   Biar kita tahu pola sebaran nilai mahasiswa. Apakah kebanyakan dapat nilai sedang-sedang saja,
   atau malah banyak yang dapat nilai jelek, atau banyak yang jenius?

3. CONTOH DI DUNIA KERJA:
   - Nilai UTBK / Tes CPNS: Panitia membuat histogram untuk melihat nilai peserta ujian se-Indonesia.
     Dari bentuk gunungnya, mereka bisa menentukan nilai batas kelulusan yang adil.
   - Bank & Kredit: Melihat sebaran penghasilan calon peminjam dana.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Inisialisasi data (dari Sub-bab 2.1)
data = {
    "Nama"   : ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"],
    "JK"     : ["L", "L", "P", "P", "L", "L", "P"],
    "Usia"   : [19, 20, 18, 21, 20, 19, 20],
    "UTS"    : [78, 85, 92, 60, 70, 88, 75],
    "UAS"    : [80, 88, 95, 65, 72, 84, 90]
}
df = pd.DataFrame(data)

# --- Kode Sub-bab 3.3 ---
plt.figure(figsize=(8, 5))
plt.hist(df["UTS"], bins=5, color="green", edgecolor="black")
plt.title("Distribusi Sebaran Nilai UTS", fontsize=14, fontweight="bold")
plt.xlabel("Nilai UTS", fontsize=11)
plt.ylabel("Banyaknya Mahasiswa (Frekuensi)", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
