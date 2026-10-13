# ==============================================================================
# SUB-BAB 3.5: BOXPLOT (DIAGRAM KOTAK GARIS)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Boxplot adalah "kotak detektif" untuk menangkap angka aneh (outlier/pencilan).
   Bentuknya seperti kotak dengan kumis (garis atas dan garis bawah):
   - Garis tengah di dalam kotak = Nilai Tengah (Median, 50% data).
   - Kotaknya itu sendiri        = Rumah bagi 50% data mahasiswa yang nilainya normal/umum.
   - Kumis atas & bawah         = Batas nilai wajar tertinggi dan terendah.
   - Titik yang keluar dari kumis = DATA ANEH (OUTLIER) yang nilainya terlalu ekstrem.

2. KENAPA BOXPLOT DISUKAI PARA ILMUWAN DATA?
   Karena dalam satu gambar kotak kecil ini, kita langsung tahu 5 hal sekaligus:
   nilai terendah, nilai kuartil 1, nilai median, nilai kuartil 3, dan nilai tertinggi,
   plus langsung ketahuan kalau ada nilai yang mencurigakan!

3. CONTOH DI DUNIA KERJA:
   - Polisi Siber / Fraud Analyst Bank: Saat memantau transaksi nasabah, kalau ada transaksi
     yang muncul sebagai titik di luar kumis boxplot (misal: biasanya transfer Rp 100 ribu, tiba-tiba
     ada transfer Rp 200 juta jam 3 pagi), sistem akan langsung membekukan kartu untuk mencegah pencurian.
   - Rumah Sakit: Memantau denyut nadi pasien untuk mendeteksi pasien yang denyutnya anomali.
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

# --- Kode Sub-bab 3.5 ---
plt.figure(figsize=(7, 5))
sns.boxplot(y=df["UAS"], color="orange")
plt.title("Boxplot Nilai UAS (Mendeteksi Sebaran & Angka Aneh)", fontsize=13, fontweight="bold")
plt.ylabel("Nilai UAS", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
