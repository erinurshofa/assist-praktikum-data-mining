import pandas as pd

# Dataframe fakta
sales = pd.DataFrame({
    "id_transaksi": [101, 102, 103, 104, 105, 106, 107, 108],
    "id_pelanggan": [1,   2,   1,   3,   2,   1,   3,   2],
    "id_produk":    [1,   2,   3,   1,   2,   3,   1,   2],
    "id_waktu":     [1,   1,   1,   2,   2,   2,   3,   3],
    "jumlah":       [2,   1,   5,   1,   4,   3,   2,   2],
    "harga_satuan": [80000, 1500000, 25000, 80000, 1500000, 25000, 80000, 1500000],
})

# Dataframe dimensi
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

print("=" * 60)
print("HASIL LANGKAH 1.3: STRUKTUR DATA WAREHOUSE")
print("=" * 60)
print(f"Sales (Fakta) : {sales.shape[0]} baris, {sales.shape[1]} kolom")
print(f"Pelanggan     : {dim_pelanggan.shape[0]} baris, {dim_pelanggan.shape[1]} kolom")
print(f"Produk        : {dim_produk.shape[0]} baris, {dim_produk.shape[1]} kolom")
print(f"Waktu         : {dim_waktu.shape[0]} baris, {dim_waktu.shape[1]} kolom")

print("\n--- TIPE DATA KOLOM PADA TABEL FAKTA (SALES) ---")
print(sales.dtypes)
