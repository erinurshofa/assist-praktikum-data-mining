# ==============================================================================
# MODUL PRAKTIKUM 2 LENGKAP: DATA WAREHOUSE & SKEMA STAR - SNOWFLAKE DENGAN PYTHON
# Laboratorium Data Mining - Program Studi Teknik Informatika, Universitas Semarang
# ==============================================================================

import pandas as pd
import numpy as np
import sqlite3

def main():
    print("=" * 70)
    print("MODUL PRAKTIKUM 2: DATA WAREHOUSE DAN SKEMA STAR & SNOWFLAKE")
    print("=" * 70)

    # --------------------------------------------------------------------------
    # LANGKAH 1: MEMBANGUN TABEL FAKTA DAN TABEL DIMENSI
    # --------------------------------------------------------------------------
    print("\n" + "#" * 50)
    print("LANGKAH 1: MEMBANGUN TABEL FAKTA DAN DIMENSI DENGAN PANDAS")
    print("#" * 50)

    # 1.1 Tabel Fakta (Sales)
    sales = pd.DataFrame({
        "id_transaksi": [101, 102, 103, 104, 105, 106, 107, 108],
        "id_pelanggan": [1,   2,   1,   3,   2,   1,   3,   2],
        "id_produk":    [1,   2,   3,   1,   2,   3,   1,   2],
        "id_waktu":     [1,   1,   1,   2,   2,   2,   3,   3],
        "jumlah":       [2,   1,   5,   1,   4,   3,   2,   2],
        "harga_satuan": [80000, 1500000, 25000, 80000, 1500000, 25000, 80000, 1500000],
    })
    sales["total_harga"] = sales["jumlah"] * sales["harga_satuan"]

    print("\n--- 1.1 Tabel Fakta Penjualan (Sales) ---")
    print(sales[["id_transaksi", "id_pelanggan", "id_produk", "id_waktu", "jumlah", "harga_satuan", "total_harga"]])

    # 1.2 Tabel Dimensi
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

    print("\n--- 1.2 Dimensi Pelanggan ---")
    print(dim_pelanggan)
    print("\n--- 1.2 Dimensi Produk ---")
    print(dim_produk)
    print("\n--- 1.2 Dimensi Waktu ---")
    print(dim_waktu)

    # 1.3 Struktur Data Warehouse
    print("\n--- 1.3 Struktur & Tipe Data ---")
    print(f"Sales: {sales.shape} | Pelanggan: {dim_pelanggan.shape} | Produk: {dim_produk.shape} | Waktu: {dim_waktu.shape}")
    print("\nTipe Data Sales:")
    print(sales.dtypes)

    # --------------------------------------------------------------------------
    # LANGKAH 2: IMPLEMENTASI SKEMA STAR
    # --------------------------------------------------------------------------
    print("\n" + "#" * 50)
    print("LANGKAH 2: IMPLEMENTASI SKEMA STAR")
    print("#" * 50)

    star = sales.merge(dim_pelanggan, on="id_pelanggan")
    star = star.merge(dim_waktu, on="id_waktu")

    print("\n--- Hasil Skema Star (Merge Fakta -> Pelanggan & Waktu) ---")
    print(star[["id_transaksi", "nama", "kota", "segmen", "tahun", "bulan", "total_harga"]])

    print("\n--- Total Penjualan per Kota (Skema Star) ---")
    print(star.groupby("kota")["total_harga"].sum())

    print("\n--- Total Penjualan per Segmen Pelanggan (Skema Star) ---")
    print(star.groupby("segmen")["total_harga"].sum())

    # --------------------------------------------------------------------------
    # LANGKAH 3: IMPLEMENTASI SKEMA SNOWFLAKE
    # --------------------------------------------------------------------------
    print("\n" + "#" * 50)
    print("LANGKAH 3: IMPLEMENTASI SKEMA SNOWFLAKE")
    print("#" * 50)

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

    print("\n--- Dimensi Kategori (Hasil Normalisasi) ---")
    print(dim_kategori)
    print("\n--- Dimensi Produk Ternormalisasi (Dengan FK id_kategori) ---")
    print(dim_produk_snow)

    snow = sales.merge(dim_produk_snow, on="id_produk", suffixes=("", "_dim"))
    snow = snow.merge(dim_kategori, on="id_kategori")
    snow["total_harga"] = snow["jumlah"] * snow["harga_satuan"]

    print("\n--- Hasil Join Berantai Skema Snowflake ---")
    print(snow[["id_transaksi", "nama_produk", "kategori", "divisi", "jumlah", "total_harga"]])

    print("\n--- Roll-Up: Total Penjualan per Divisi (Snowflake) ---")
    print(snow.groupby("divisi")["total_harga"].sum())

    # --------------------------------------------------------------------------
    # LANGKAH 4: OPERASI OLAP (ROLL-UP, DRILL-DOWN, SLICE, DICE)
    # --------------------------------------------------------------------------
    print("\n" + "#" * 50)
    print("LANGKAH 4: OPERASI OLAP")
    print("#" * 50)

    kubus = sales.merge(dim_pelanggan, on="id_pelanggan")
    kubus = kubus.merge(dim_produk,  on="id_produk", suffixes=("", "_dim"))
    kubus = kubus.merge(dim_waktu,   on="id_waktu")
    kubus["total_harga"] = kubus["jumlah"] * kubus["harga_satuan"]

    print("\n--- Kubus Data Multidimensi Lengkap ---")
    print(kubus[["id_transaksi", "nama", "kota", "nama_produk", "kategori", "total_harga"]])

    print("\n--- 4.1 ROLL-UP: Total Penjualan per Kota ---")
    print(kubus.groupby("kota")["total_harga"].sum())

    print("\n--- 4.2 DRILL-DOWN: Total Penjualan per Segmen Pelanggan ---")
    print(kubus.groupby("segmen")["total_harga"].sum())

    print("\n--- 4.2 KUBUS 2D (Pivot Table: Kota x Kategori Produk) ---")
    print(kubus.pivot_table(index="kota", columns="kategori", values="total_harga", aggfunc="sum", fill_value=0))

    print("\n--- 4.3 SLICE: Hanya Transaksi Kota Semarang ---")
    iris = kubus[kubus["kota"] == "Semarang"]
    print(iris[["id_transaksi", "nama", "total_harga"]])

    print("\n--- 4.4 DICE: Transaksi Semarang & Total > 500.000 ---")
    hasil_dice = kubus[(kubus["kota"] == "Semarang") & (kubus["total_harga"] > 500000)]
    print(hasil_dice[["id_transaksi", "nama", "total_harga"]])

    # --------------------------------------------------------------------------
    # LANGKAH 5: MENYIMPAN DATA WAREHOUSE KE DATABASE (SQLITE)
    # --------------------------------------------------------------------------
    print("\n" + "#" * 50)
    print("LANGKAH 5: MENYIMPAN KE SQLITE & QUERY JOIN")
    print("#" * 50)

    con = sqlite3.connect("data_warehouse.db")
    sales.to_sql("fact_sales", con, if_exists="replace", index=False)
    dim_pelanggan.to_sql("dim_pelanggan", con, if_exists="replace", index=False)
    dim_produk.to_sql("dim_produk", con, if_exists="replace", index=False)
    dim_waktu.to_sql("dim_waktu", con, if_exists="replace", index=False)
    print("Tabel berhasil disimpan ke file 'data_warehouse.db'!")

    hasil_sql = pd.read_sql_query("""
        SELECT s.id_transaksi, p.nama_produk, p.kategori, s.jumlah
        FROM fact_sales AS s
        JOIN dim_produk AS p ON s.id_produk = p.id_produk
    """, con)
    print("\nHasil Query SQL JOIN dari data_warehouse.db:")
    print(hasil_sql)
    con.close()

    print("\n" + "=" * 70)
    print("SELURUH LANGKAH PRAKTIKUM 2 BERHASIL DIJALANKAN DENGAN SUKSES!")
    print("=" * 70)

if __name__ == "__main__":
    main()
