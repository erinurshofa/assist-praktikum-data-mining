# ==============================================================================
# LANGKAH 5.2: QUERY SQL JOIN LANGSUNG PADA DATA WAREHOUSE DI SQLITE
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA KEGUNAAN QUERY SQL LANGSUNG PADA DATA WAREHOUSE?
   Setelah data dimuat (Load) ke database relasional, analis data dapat memakai
   bahasa standar SQL (Structured Query Language) untuk menggabungkan fakta dan dimensi.

2. METODE `pd.read_sql_query()`:
   Pandas memungkinkan kita menulis query SQL murni seperti:
   `SELECT ... FROM fact_sales JOIN dim_produk ...`
   dan langsung mengembalikan hasilnya ke dalam bentuk DataFrame Pandas yang rapi!
"""

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
"""

hasil_query = pd.read_sql_query(query_sql, con)

print("\n--- Hasil Query SQL JOIN (fact_sales JOIN dim_produk) ---")
print(hasil_query)

# 3. Selalu tutup koneksi database setelah selesai
con.close()
print("\n[INFO] Koneksi SQLite berhasil ditutup.")
