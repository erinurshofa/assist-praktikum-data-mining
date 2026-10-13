# ==============================================================================
# SUB-BAB 2.2: MELIHAT RINGKASAN DATA
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita sedang "berkenalan" dan melakukan "inspeksi cepat" pada data yang kita punya:
   - `df.head(3)`    : "Tolong intip 3 baris teratas saja." Biar layar tidak penuh kalau datanya ada 10.000 baris.
   - `df.info()`     : "Tolong cek kesehatan data." Memberitahu ada berapa total baris, apakah ada kotak yang kosong
                       (bolong/hilang), dan jenis datanya (angka atau tulisan teks).
   - `df.describe()` : "Tolong buatkan rangkuman matematika otomatis." Menghitung rata-rata, nilai terendah,
                       dan nilai tertinggi dalam sekejap tanpa rumus manual.

2. KENAPA INI WAJIB DILAKUKAN DULUAN?
   Ibarat membeli buah di pasar, kita tidak langsung memakannya kan? Kita pasti mengecek dulu
   apakah buahnya segar, ada bagian yang busuk/cacat, atau salah jenis.
   Di data science, mengecek data di awal menghindarkan kita dari salah hitung di langkah berikutnya.

3. CONTOH DI DUNIA KERJA:
   - Kasir Bank / Finance: Ketika membuka laporan transaksi keuangan harian, mereka langsung pakai `describe()`.
     Jika melihat nilai minimum uangnya minus (misal: -Rp 5.000.000) padahal harusnya positif,
     mereka langsung tahu ada sistem yang error atau kecurangan (fraud) hari itu.
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

# --- Kode Sub-bab 2.2 ---
print("=== 1. MENGINTIP 3 BARIS TERATAS (head) ===")
print(df.head(3))

print("\n=== 2. MENGECEK KESEHATAN & TIPE DATA (info) ===")
print(df.info())

print("\n=== 3. RANGKUMAN ANGKA OTOMATIS (describe) ===")
print(df.describe())
