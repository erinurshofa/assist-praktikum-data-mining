# ==============================================================================
# SUB-BAB 3.2: DIAGRAM BATANG (BAR CHART)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita sedang membandingkan rata-rata nilai UAS antara mahasiswa Laki-laki (L) dan Perempuan (P)
   menggunakan balok/tiang berdiri (diagram batang).
   - Makin TINGGI tiangnya = Berarti nilainya makin besar.
   - `plt.bar(...)` : Perintah menggambar tiang batang. Kita beri warna biru muda (skyblue) untuk pria
     dan warna salmon untuk wanita.

2. KAPAN KITA HARUS PAKAI DIAGRAM BATANG?
   Gunakan diagram batang saat kamu ingin MEMBANDINGKAN nilai antar KATEGORI yang berbeda
   (misal: Laki-laki vs Perempuan, Kota Jakarta vs Surabaya, Jurusan TI vs SI).
   Mata manusia paling mudah dan paling cepat membandingkan tinggi tiang!

3. CONTOH DI DUNIA KERJA:
   - Manajer Toko Kopi (Kopi Kenangan / Janji Jiwa): Membandingkan jumlah cup kopi yang terjual
     antara Cabang A, Cabang B, dan Cabang C untuk melihat cabang mana yang paling ramai.
   - YouTube Creator: Membandingkan jumlah penonton video berdasarkan kategori (Tutorial, Vlog, Gaming).
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

# --- Kode Sub-bab 3.2 ---
# Rata-rata UAS per jenis kelamin
rata_per_jk = df.groupby("JK")["UAS"].mean()

plt.figure(figsize=(6, 5))
plt.bar(rata_per_jk.index, rata_per_jk.values, color=["skyblue", "salmon"], edgecolor="black")
plt.title("Rata-rata UAS Berdasarkan Jenis Kelamin", fontsize=13, fontweight="bold")
plt.xlabel("Jenis Kelamin", fontsize=11)
plt.ylabel("Rata-rata UAS", fontsize=11)
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
