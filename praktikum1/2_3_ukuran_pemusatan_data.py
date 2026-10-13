# ==============================================================================
# SUB-BAB 2.3: UKURAN PEMUSATAN DATA (CENTRAL TENDENCY)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita mencari "Satu Angka Jagoan" yang bisa mewakili gambaran umum seluruh kelompok:
   - `mean()`   : Rata-rata (semua angka dijumlah lalu dibagi banyaknya orang).
   - `median()` : Nilai tengah persis setelah semua orang diurutkan dari yang terkecil ke terbesar.
   - `mode()`   : Modus (angka yang paling banyak kembarannya / paling sering muncul).
   - `min()` & `max()` : Nilai paling bontot (terendah) dan nilai paling juara (tertinggi).

2. KENAPA ADA MEAN DAN MEDIAN SEKALIGUS? KAN SAMA-SAMA NILAI TENGAH?
   Bayangkan di sebuah warung kopi ada 5 orang dengan uang saku: Rp 10.000, Rp 10.000, Rp 12.000, Rp 15.000,
   dan tiba-tiba masuk Raffi Ahmad dengan uang saku Rp 1.000.000.000.
   - Kalau pakai **Rata-rata (Mean)**, rata-rata uang saku di warung itu jadi Rp 200 juta per orang. (Ini bohong/tidak adil!).
   - Tapi kalau pakai **Median**, nilainya tetap sekitar Rp 12.000 (jauh lebih mencerminkan kenyataan).
   Itulah kenapa di dunia nyata, Median sering dipakai saat ada angka yang terlampau jomplang!

3. CONTOH DI DUNIA KERJA:
   - HRD Perusahaan: Menentukan standar gaji karyawan posisi programmer baru menggunakan Median,
     agar tidak terdistorsi oleh gaji segelintir bos besar.
   - Restoran Cepat Saji (McD / KFC): Menggunakan Modus untuk mengetahui paket menu apa yang paling sering
     dipesan jam makan siang, agar ayamnya digoreng duluan sebelum antrean membludak.
"""

import pandas as pd
import numpy as np

# Inisialisasi data (dari Sub-bab 2.1)
data = {
    "Nama"   : ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"],
    "JK"     : ["L", "L", "P", "P", "L", "L", "P"],
    "Usia"   : [19, 20, 18, 21, 20, 19, 20],
    "UTS"    : [78, 85, 92, 60, 70, 88, 75],
    "UAS"    : [80, 88, 95, 65, 72, 84, 90]
}
df = pd.DataFrame(data)

# --- Kode Sub-bab 2.3 ---
print("=== NILAI WAKIL KELOMPOK (UKURAN PEMUSATAN) ===")
# Rata-rata (mean)
print("Rata-rata UTS :", df["UTS"].mean())

# Median
print("Median UAS    :", df["UAS"].median())

# Modus (nilai paling sering muncul)
print("Modus Usia    :")
print(df["Usia"].mode())

# Nilai minimum dan maksimum
print("Nilai Terendah UTS  :", df["UTS"].min())
print("Nilai Tertinggi UTS :", df["UTS"].max())
