import sqlite3
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
print("HASIL LANGKAH 5.1: SIMPAN TABEL KE SQLITE (data_warehouse.db)")
print("=" * 60)

# Membuka koneksi ke file database SQLite (file otomatis dibuat jika belum ada)
con = sqlite3.connect("data_warehouse.db")

# Menyimpan masing-masing DataFrame menjadi tabel SQL
sales.to_sql("fact_sales", con, if_exists="replace", index=False)
dim_pelanggan.to_sql("dim_pelanggan", con, if_exists="replace", index=False)
dim_produk.to_sql("dim_produk", con, if_exists="replace", index=False)
dim_waktu.to_sql("dim_waktu", con, if_exists="replace", index=False)

# Tutup koneksi
con.close()

print("\n[OK] Berhasil menyimpan tabel-tabel data warehouse ke 'data_warehouse.db'!")
print("- Tabel fact_sales      (Tersimpan)")
print("- Tabel dim_pelanggan   (Tersimpan)")
print("- Tabel dim_produk      (Tersimpan)")
print("- Tabel dim_waktu       (Tersimpan)")
