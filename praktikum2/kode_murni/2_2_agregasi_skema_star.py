import pandas as pd

# Menyiapkan tabel fakta & dimensi
sales = pd.DataFrame({
    "id_transaksi": [101, 102, 103, 104, 105, 106, 107, 108],
    "id_pelanggan": [1,   2,   1,   3,   2,   1,   3,   2],
    "id_produk":    [1,   2,   3,   1,   2,   3,   1,   2],
    "id_waktu":     [1,   1,   1,   2,   2,   2,   3,   3],
    "jumlah":       [2,   1,   5,   1,   4,   3,   2,   2],
    "harga_satuan": [80000, 1500000, 25000, 80000, 1500000, 25000, 80000, 1500000],
})
sales["total_harga"] = sales["jumlah"] * sales["harga_satuan"]

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

# Merakit skema star
star = sales.merge(dim_pelanggan, on="id_pelanggan").merge(dim_waktu, on="id_waktu")

print("=" * 60)
print("HASIL LANGKAH 2.2: AGREGASI SKEMA STAR")
print("=" * 60)

# 1. Total penjualan per kota (level dimensi pelanggan)
print("\n--- [1] TOTAL PENJUALAN PER KOTA ---")
total_per_kota = star.groupby("kota")["total_harga"].sum()
print(total_per_kota)

# 2. Total penjualan per segmen pelanggan
print("\n--- [2] TOTAL PENJUALAN PER SEGMEN PELANGGAN ---")
total_per_segmen = star.groupby("segmen")["total_harga"].sum()
print(total_per_segmen)
