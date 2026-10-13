import pandas as pd

# 1. Dimensi Pelanggan (Who & Where)
dim_pelanggan = pd.DataFrame({
    "id_pelanggan": [1, 2, 3],
    "nama":         ["Andi", "Budi", "Citra"],
    "kota":         ["Semarang", "Semarang", "Solo"],
    "provinsi":     ["Jawa Tengah", "Jawa Tengah", "Jawa Tengah"],
    "segmen":       ["Retail", "Wholesale", "Retail"],
})

# 2. Dimensi Produk (What)
dim_produk = pd.DataFrame({
    "id_produk":    [1, 2, 3],
    "nama_produk":  ["Laptop", "Printer", "Tinta"],
    "kategori":     ["Elektronik", "Elektronik", "Perlengkapan"],
    "harga_satuan": [8000000, 1500000, 25000],
})

# 3. Dimensi Waktu (When)
dim_waktu = pd.DataFrame({
    "id_waktu": [1, 2, 3],
    "tanggal":  ["2026-01-05", "2026-01-12", "2026-01-19"],
    "tahun":    [2026, 2026, 2026],
    "bulan":    [1, 1, 1],
    "kuartal":  ["Q1", "Q1", "Q1"],
    "hari":     ["Min", "Min", "Min"],
})

print("=" * 60)
print("HASIL LANGKAH 1.2: TABEL DIMENSI DATA WAREHOUSE")
print("=" * 60)

print("\n[1] DIMENSI PELANGGAN:")
print(dim_pelanggan)

print("\n[2] DIMENSI PRODUK:")
print(dim_produk)

print("\n[3] DIMENSI WAKTU:")
print(dim_waktu)
