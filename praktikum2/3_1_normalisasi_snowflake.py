# ==============================================================================
# LANGKAH 3.1: NORMALISASI DIMENSI PADA SKEMA SNOWFLAKE
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA ITU SKEMA SNOWFLAKE (SNOWFLAKE SCHEMA)?
   Jika Skema Star berbentuk bintang tunggal yang sederhana, maka Skema Snowflake
   memecah (menormalisasi) tabel dimensi menjadi beberapa tabel yang saling berhubungan,
   menyerupai kristal salju (snowflake).

2. PERBEDAAN DENGAN SKEMA STAR:
   - Pada Star: Kolom 'kategori' dan atribut kelompok produk langsung ditaruh
     menumpuk di dalam tabel `dim_produk`.
   - Pada Snowflake: Tabel produk dinormalisasi!
     Dibuat tabel baru `dim_kategori` yang berisi id_kategori, nama kategori, dan divisi.
     Lalu di `dim_produk`, kolom kategori digantikan oleh Foreign Key `id_kategori`.

3. KELEBIHAN & KEKURANGAN:
   - Kelebihan: Menghindari redundansi data teks (hemat memori / storage).
   - Kekurangan: Query butuh join berantai (multi-hop join), sehingga sedikit lebih lambat.
"""

import pandas as pd

# Tabel kategori (dimensi ke-2 hasil normalisasi produk)
dim_kategori = pd.DataFrame({
    "id_kategori": [10, 20],
    "kategori":    ["Elektronik", "Perlengkapan"],
    "divisi":      ["Teknologi", "Logistik"],
})

# dim_produk sekarang memegang Foreign Key (FK) id_kategori, bukan menempel kategori langsung
dim_produk_snow = pd.DataFrame({
    "id_produk":    [1, 2, 3],
    "nama_produk":  ["Laptop", "Printer", "Tinta"],
    "id_kategori":  [10, 10, 20],
    "harga_satuan": [8000000, 1500000, 25000],
})

print("=" * 60)
print("HASIL LANGKAH 3.1: STRUKTUR NORMALISASI DIMENSI SNOWFLAKE")
print("=" * 60)

print("\n--- [1] TABEL DIM_KATEGORI (Level Lebih Tinggi) ---")
print(dim_kategori)

print("\n--- [2] TABEL DIM_PRODUK (Memegang FK id_kategori) ---")
print(dim_produk_snow)
