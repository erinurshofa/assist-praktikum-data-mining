import pandas as pd

# 1. Menyiapkan tabel fakta & semua tabel dimensi
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

# 2. Merakit kubus data lengkap (menggabungkan fakta dengan seluruh dimensi)
kubus = sales.merge(dim_pelanggan, on="id_pelanggan")
kubus = kubus.merge(dim_produk,  on="id_produk", suffixes=("", "_dim"))
kubus = kubus.merge(dim_waktu,   on="id_waktu")
kubus["total_harga"] = kubus["jumlah"] * kubus["harga_satuan"]

print("=" * 60)
print("HASIL LANGKAH 4.1: OPERASI OLAP — ROLL-UP")
print("=" * 60)

# Menampilkan cuplikan kubus data multidimensi
print("\n--- Cuplikan Kubus Data Lengkap ---")
print(kubus[["id_transaksi", "nama", "kota", "nama_produk", "kategori", "total_harga"]])

# Melakukan ROLL-UP: Penjualan diringkas per kota
print("\n--- Operasi ROLL-UP: Total Penjualan per Kota ---")
roll_up_kota = kubus.groupby("kota")["total_harga"].sum()
print(roll_up_kota)
