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
print("HASIL LANGKAH 4.3: OPERASI OLAP — SLICE")
print("=" * 60)

# Melakukan SLICE: Mengambil irisan data di mana kota == 'Semarang'
iris_semarang = kubus[kubus["kota"] == "Semarang"]

print("\n--- SLICE: Transaksi Khusus Wilayah Semarang ---")
print(iris_semarang[["id_transaksi", "nama", "kota", "nama_produk", "jumlah", "total_harga"]])
