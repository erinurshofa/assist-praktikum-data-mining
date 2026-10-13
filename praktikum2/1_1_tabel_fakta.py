# ==============================================================================
# LANGKAH 1.1: MEMBANGUN TABEL FAKTA (FACT TABLE) DENGAN PANDAS
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA ITU TABEL FAKTA (FACT TABLE)?
   Tabel fakta adalah tabel utama di pusat arsitektur Data Warehouse.
   Tabel ini mencatat kejadian operasional nyata (misalnya setiap transaksi penjualan kasir).
   Ciri khas tabel fakta:
   - Berisi angka-angka hasil pengukuran / transaksi yang disebut 'MEASURE'
     (contoh: jumlah barang, harga satuan, total harga).
   - Berisi kunci penghubung ('FOREIGN KEY' / FK) yang mengarah ke tabel dimensi
     (contoh: id_pelanggan, id_produk, id_waktu).

2. KENAPA ADA ID_WAKTU?
   Dalam data warehouse, dimensi waktu sangat vital untuk analisis tren bisnis.
   id_waktu bertindak sebagai FK penghubung ke tanggal, bulan, kuartal, dan tahun.
"""

import pandas as pd
import numpy as np

# Membangun tabel fakta transaksi penjualan (sales)
sales = pd.DataFrame({
    "id_transaksi": [101, 102, 103, 104, 105, 106, 107, 108],
    "id_pelanggan": [1,   2,   1,   3,   2,   1,   3,   2],
    "id_produk":    [1,   2,   3,   1,   2,   3,   1,   2],
    "id_waktu":     [1,   1,   1,   2,   2,   2,   3,   3],
    "jumlah":       [2,   1,   5,   1,   4,   3,   2,   2],
    "harga_satuan": [80000, 1500000, 25000, 80000, 1500000, 25000, 80000, 1500000],
})

# Menghitung Measure (ukuran bisnis): total_harga = jumlah * harga_satuan
sales["total_harga"] = sales["jumlah"] * sales["harga_satuan"]

print("=" * 60)
print("HASIL LANGKAH 1.1: TABEL FAKTA PENJUALAN (SALES)")
print("=" * 60)
print(sales[["id_transaksi", "id_pelanggan", "id_produk", "id_waktu", "jumlah", "harga_satuan", "total_harga"]])
