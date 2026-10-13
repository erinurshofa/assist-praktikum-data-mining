# ==============================================================================
# LANGKAH 4.2: OPERASI OLAP — DRILL-DOWN (RINCI KE LEVEL BAWAH & KUBUS 2D)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA ITU DRILL-DOWN?
   Drill-down adalah kebalikan dari Roll-up.
   Jika Roll-up meringkas ke atas (contoh: per wilayah/kota), maka Drill-down
   menggali lebih dalam ke rincian di bawahnya (contoh: rincian segmen konsumen).

2. KUBUS 2D (PIVOT TABLE):
   Kita menyilangkan 2 sumbu dimensi sekaligus:
   - Sumbu Baris: Kota
   - Sumbu Kolom: Kategori Produk
   Ini membentuk tabel silang (matriks) yang menampilkan persebaran omset.
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
print("HASIL LANGKAH 4.2: OPERASI OLAP — DRILL-DOWN & KUBUS 2D")
print("=" * 60)

# Drill-down: Dari kota turun melihat detail per segmen pelanggan
print("\n--- DRILL-DOWN: Total Penjualan per Segmen Pelanggan ---")
drill_segmen = kubus.groupby("segmen")["total_harga"].sum()
print(drill_segmen)

# Kombinasi dua sumbu dimensi: Matriks Kubus 2D (Kota vs Kategori Produk)
print("\n--- KUBUS 2D (PIVOT TABLE): Kota x Kategori Produk ---")
pivot_2d = kubus.pivot_table(
    index="kota",
    columns="kategori",
    values="total_harga",
    aggfunc="sum",
    fill_value=0
)
print(pivot_2d)
