# ==============================================================================
# SUB-BAB 2.6: SELEKSI DAN FILTER DATA
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita sedang "memilih dan menyaring" data sesuai kebutuhan kita:
   - Memilih Kolom   : `df[['Nama', 'UTS']]` -> "Tolong ambil kolom Nama dan UTS saja ya, kolom lain singkirkan dulu."
   - Menyaring Baris : `df[df['UTS'] >= 75]` -> "Tolong carikan mahasiswa yang nilainya 75 ke atas saja, yang lain sembunyikan."
   - Mengelompokkan  : `groupby('JK')['UAS'].mean()` -> "Tolong pisahkan yang Laki-laki dan Perempuan,
                       lalu hitung rata-rata nilai UAS masing-masing kelompok."

2. KENAPA KITA PERLU FILTER & GROUPBY?
   Karena di dunia nyata data itu bisa berisi jutaan baris. Kita tidak mungkin melihat semuanya satu per satu.
   Kita hanya butuh melihat data orang-orang tertentu yang memenuhi syarat.

3. CONTOH DI DUNIA KERJA:
   - Aplikasi Ojek Online (Gojek / Grab):
     * Filter: Hanya tampilkan driver yang sedang online dan berjarak kurang dari 2 km dari pemesan.
     * Groupby: Menghitung rata-rata penghasilan driver per kota (Jakarta vs Semarang vs Surabaya).
   - E-Commerce: Menyaring pelanggan yang memasukkan barang ke keranjang belanja tapi belum bayar
     dalam 24 jam untuk dikirimi notifikasi pengingat via WhatsApp.
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

# --- Kode Sub-bab 2.6 ---
# Memilih kolom tertentu
print("=== 1. HANYA MELIHAT NAMA DAN NILAI UTS ===")
print(df[["Nama", "UTS"]])

# Memilih baris berdasarkan kondisi (filter)
print("\n=== 2. MAHASISWA YANG LULUS (NILAI UTS >= 75) ===")
mahasiswa_lulus = df[df["UTS"] >= 75]
print(mahasiswa_lulus)

# Pengelompokan berdasarkan kategori (JK)
print("\n=== 3. RATA-RATA UAS BERDASARKAN GENDER (LAKI-LAKI VS PEREMPUAN) ===")
print(df.groupby("JK")["UAS"].mean())
