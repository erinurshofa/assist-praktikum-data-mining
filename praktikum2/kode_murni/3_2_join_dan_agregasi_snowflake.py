import pandas as pd

# 1. Tabel fakta sales
sales = pd.DataFrame({
    "id_transaksi": [101, 102, 103, 104, 105, 106, 107, 108],
    "id_pelanggan": [1,   2,   1,   3,   2,   1,   3,   2],
    "id_produk":    [1,   2,   3,   1,   2,   3,   1,   2],
    "id_waktu":     [1,   1,   1,   2,   2,   2,   3,   3],
    "jumlah":       [2,   1,   5,   1,   4,   3,   2,   2],
    "harga_satuan": [80000, 1500000, 25000, 80000, 1500000, 25000, 80000, 1500000],
})

# 2. Tabel dimensi ternormalisasi (Snowflake)
dim_kategori = pd.DataFrame({
    "id_kategori": [10, 20],
    "kategori":    ["Elektronik", "Perlengkapan"],
    "divisi":      ["Teknologi", "Logistik"],
})

dim_produk_snow = pd.DataFrame({
    "id_produk":    [1, 2, 3],
    "nama_produk":  ["Laptop", "Printer", "Tinta"],
    "id_kategori":  [10, 10, 20],
    "harga_satuan": [8000000, 1500000, 25000],
})

# 3. Join berantai: sales -> dim_produk_snow -> dim_kategori
snow = sales.merge(dim_produk_snow, on="id_produk", suffixes=("", "_dim"))
snow = snow.merge(dim_kategori, on="id_kategori")

# Hitung ulang measure total harga transaksi
snow["total_harga"] = snow["jumlah"] * snow["harga_satuan"]

print("=" * 60)
print("HASIL LANGKAH 3.2: SKEMA SNOWFLAKE & ROLL-UP DIVISI")
print("=" * 60)

print("\n--- Cuplikan Baris Hasil Join Berantai Skema Snowflake ---")
print(snow[["id_transaksi", "nama_produk", "kategori", "divisi", "jumlah", "total_harga"]])

# Roll-up: Total penjualan per divisi (level hierarki lebih tinggi dari produk & kategori)
print("\n--- Roll-Up: Total Penjualan per Divisi ---")
total_per_divisi = snow.groupby("divisi")["total_harga"].sum()
print(total_per_divisi)
