# ==============================================================================
# SUB-BAB 2.1: MEMBUAT DATAFRAME SEDERHANA
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita sedang membuat "Tabel Excel versi Python" yang dinamakan DataFrame.
   Data aslinya masih berupa catatan biasa (dictionary di Python), lalu dengan perintah
   `pd.DataFrame(data)`, Python otomatis menyusunnya jadi tabel rapi lengkap
   dengan judul kolom dan nomor baris (0, 1, 2, dst).

2. KENAPA KITA BUTUH DATAFRAME?
   - Lebih rapi dan enak dibaca mata manusia.
   - Kalau datanya sudah jadi DataFrame, kita bisa menyaring, menghitung rata-rata,
     sampai membuat grafik hanya dengan mengetik 1 baris perintah saja, tanpa perlu
     bikin rumus yang ribet berulang kali.

3. CONTOH DI DUNIA KERJA:
   - Toko Online / Shopee: Saat pembeli mengisi formulir checkout (nama barang, alamat,
     harga, metode bayar), data yang masuk awalnya acak-acakan. Sistem akan mengubahnya
     menjadi DataFrame rapi seperti ini agar bagian gudang bisa langsung tahu barang apa
     saja yang harus dikemas hari ini.
"""

import pandas as pd
import numpy as np

# Membuat DataFrame dari data nilai mahasiswa
data = {
    "Nama"   : ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"],
    "JK"     : ["L", "L", "P", "P", "L", "L", "P"],
    "Usia"   : [19, 20, 18, 21, 20, 19, 20],
    "UTS"    : [78, 85, 92, 60, 70, 88, 75],
    "UAS"    : [80, 88, 95, 65, 72, 84, 90]
}

df = pd.DataFrame(data)

print("=== TABEL DATA MAHASISWA ===")
print(df)
