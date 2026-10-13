import sqlite3
import pandas as pd

# 1. Menghubungkan ke database SQLite yang sudah dibuat
con = sqlite3.connect("data_warehouse.db")

print("=" * 60)
print("HASIL LANGKAH 5.2: QUERY SQL JOIN PADA data_warehouse.db")
print("=" * 60)

# 2. Menjalankan query SQL join murni antara fact_sales dan dim_produk
query_sql = """
    SELECT 
        s.id_transaksi, 
        p.nama_produk, 
        p.kategori, 
        s.jumlah,
        s.total_harga
    FROM fact_sales AS s
    JOIN dim_produk AS p ON s.id_produk = p.id_produk
