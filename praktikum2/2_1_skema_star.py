# ==============================================================================
# LANGKAH 2.1: IMPLEMENTASI SKEMA STAR (MERGE FAKTA DENGAN DIMENSI)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA ITU SKEMA STAR (STAR SCHEMA)?
   Bentuknya seperti bintang:
   - Di tengah adalah SATU TABEL FAKTA (penjualan).
   - Di sekelilingnya adalah TABEL-TABEL DIMENSI (pelanggan, produk, waktu).
   - Tabel dimensi TIDAK dinormalisasi (denormalized), artinya langsung dihubungkan
     ke tabel fakta hanya dengan 1 kali relasi (join 1 tingkat).

2. KELEBIHAN SKEMA STAR:
   - Query sangat cepat dan sederhana karena join tidak berlapis.
   - Paling populer digunakan dalam Data Mart bisnis.
"""

import pandas as pd

# 1. Menyiapkan tabel fakta
sales = pd.DataFrame({
    "id_transaksi": [101, 102, 103, 104, 105, 106, 107, 108],
    "id_pelanggan": [1,   2,   1,   3,   2,   1,   3,   2],
    "id_produk":    [1,   2,   3,   1,   2,   3,   1,   2],
    "id_waktu":     [1,   1,   1,   2,   2,   2,   3,   3],
    "jumlah":       [2,   1,   5,   1,   4,   3,   2,   2],
    "harga_satuan": [80000, 1500000, 25000, 80000, 1500000, 25000, 80000, 1500000],
})
sales["total_harga"] = sales["jumlah"] * sales["harga_satuan"]

# 2. Menyiapkan tabel dimensi
dim_pelanggan = pd.DataFrame({
    "id_pelanggan": [1, 2, 3],
    "nama":         ["Andi", "Budi", "Citra"],
    "kota":         ["Semarang", "Semarang", "Solo"],
    "provinsi":     ["Jawa Tengah", "Jawa Tengah", "Jawa Tengah"],
    "segmen":       ["Retail", "Wholesale", "Retail"],
})

dim_waktu = pd.DataFrame({
    "id_waktu": [1, 2, 3],
    "tanggal":  ["2026-01-05", "2026-01-12", "2026-01-19"],
    "tahun":    [2026, 2026, 2026],
    "bulan":    [1, 1, 1],
    "kuartal":  ["Q1", "Q1", "Q1"],
    "hari":     ["Min", "Min", "Min"],
})

# 3. Merakit Skema Star dengan merge
# Gabungkan fakta -> dimensi pelanggan -> dimensi waktu
star = sales.merge(dim_pelanggan, on="id_pelanggan")
star = star.merge(dim_waktu, on="id_waktu")

print("=" * 60)
print("HASIL LANGKAH 2.1: SKEMA STAR (JOIN FAKTA & DIMENSI)")
print("=" * 60)

# Tampilkan kolom kunci hasil skema star
print("\n--- Cuplikan Kolom Utama Skema Star ---")
print(star[["id_transaksi", "nama", "kota", "segmen", "tahun", "bulan", "total_harga"]])

# Tampilkan seluruh nama kolom yang terbentuk
print("\n--- Semua Kolom yang Tersedia dalam Skema Star ---")
print(star.columns.tolist())
