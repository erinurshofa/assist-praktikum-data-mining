# ==============================================================================
# SUB-BAB 3.4: DIAGRAM SEBAR (SCATTER PLOT)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita sedang menaruh titik-titik di bidang koordinat (seperti main game tembak sasaran):
   - Sumbu mendatar (X) = Nilai UTS
   - Sumbu tegak (Y)    = Nilai UAS
   Setiap satu titik mewakili satu mahasiswa (misal: Andi UTS-nya 78, UAS-nya 80, maka titik Andi ada di koordinat (78, 80)).

2. BAGAIMANA CARA MEMBACANYA?
   - Kalau titik-titiknya cenderung miring NAIK dari kiri-bawah ke kanan-atas:
     Artinya MAKIN TINGGI UTS, MAKIN TINGGI JUGA UAS-NYA (ada hubungan positif!).
   - Kalau titik-titiknya menyebar berantakan tanpa arah:
     Artinya tidak ada hubungan sama sekali antara kedua nilai tersebut.

3. CONTOH DI DUNIA KERJA:
   - Toko Handphone: Memetakan titik-titik antara "Kapasitas Baterai (mAh)" vs "Waktu Pemakaian HP (Jam)".
   - Dokter / Ahli Gizi: Memetakan hubungan antara "Jumlah Kalori Makanan" vs "Berat Badan Pasien".
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

# --- Kode Sub-bab 3.4 ---
plt.figure(figsize=(7, 5))
plt.scatter(df["UTS"], df["UAS"], color="purple", s=70, edgecolors="black")
plt.title("Hubungan Nilai UTS dan UAS (Scatter Plot)", fontsize=14, fontweight="bold")
plt.xlabel("Nilai UTS", fontsize=11)
plt.ylabel("Nilai UAS", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()
