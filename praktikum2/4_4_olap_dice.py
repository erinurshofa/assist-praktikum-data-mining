# ==============================================================================
# LANGKAH 4.4: OPERASI OLAP — DICE (SUB-KUBUS DENGAN LEBIH DARI SATU KRITERIA)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA ITU OPERASI DICE?
   Jika Slice hanya memotong berdasarkan 1 kriteria tunggal (misal: hanya Semarang),
   maka 'Dice' memotong sub-balok (sub-kubus) menggunakan 2 kriteria atau lebih
   secara bersamaan.

2. CONTOH KASUS DICE KALI INI:
   Manajer ingin mencari:
   - Kriteria 1: Transaksi berasal dari kota "Semarang"
   - Kriteria 2: Total harga belanja di atas 500.000 rupiah (> 500000)
"""

import pandas as pd

# Menyiapkan data fakta & dimensi
sales = pd.DataFrame({
    "id_transaksi": [101, 102, 103, 104, 105, 106, 107, 108],
    "id_pelanggan": [1,   2,   1,   3,   2,   1,   3,   2],
    "id_produk":    [1,   2,   3,   1,   2,   3,   1,   2],
    "id_waktu":     [1,   1,   1,   2,   2,   2,   3,   3],
    "jumlah":       [2,   1,   5,   1,   4,   3,   2,   2],
    "harga_satuan": [80000, 1500000, 25000, 80000, 1500000, 25000, 80000, 1500000],
})

dim_pelanggan = pd.DataFrame({
    "id_pelanggan": [1, 2, 3],
    "nama":         ["Andi", "Budi", "Citra"],
    "kota":         ["Semarang", "Semarang", "Solo"],
    "provinsi":     ["Jawa Tengah", "Jawa Tengah", "Jawa Tengah"],
    "segmen":       ["Retail", "Wholesale", "Retail"],
})

dim_produk = pd.DataFrame({
    "id_produk":    [1, 2, 3],
    "nama_produk":  ["Laptop", "Printer", "Tinta"],
    "kategori":     ["Elektronik", "Elektronik", "Perlengkapan"],
    "harga_satuan": [8000000, 1500000, 25000],
})

dim_waktu = pd.DataFrame({
    "id_waktu": [1, 2, 3],
    "tanggal":  ["2026-01-05", "2026-01-12", "2026-01-19"],
    "tahun":    [2026, 2026, 2026],
    "bulan":    [1, 1, 1],
    "kuartal":  ["Q1", "Q1", "Q1"],
    "hari":     ["Min", "Min", "Min"],
})

# Merakit kubus data
kubus = sales.merge(dim_pelanggan, on="id_pelanggan").merge(dim_produk, on="id_produk", suffixes=("", "_dim")).merge(dim_waktu, on="id_waktu")
kubus["total_harga"] = kubus["jumlah"] * kubus["harga_satuan"]

print("=" * 60)
print("HASIL LANGKAH 4.4: OPERASI OLAP — DICE")
print("=" * 60)

# Melakukan DICE: Filter dengan dua kondisi sekaligus menggunakan operator & (AND)
hasil_dice = kubus[(kubus["kota"] == "Semarang") & (kubus["total_harga"] > 500000)]

print("\n--- DICE: Transaksi di Semarang & Total Harga > 500.000 ---")
print(hasil_dice[["id_transaksi", "nama", "kota", "nama_produk", "jumlah", "total_harga"]])
