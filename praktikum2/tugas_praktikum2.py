# ==============================================================================
# TUGAS PRAKTIKUM 2: STUDI KASUS DATA WAREHOUSE TOKO ONLINE "ELEKTROSHOP"
# Lingkup Waktu: Januari – Maret 2026 (Kuartal 1 / Q1 2026)
# ==============================================================================
"""
[DESKRIPSI TUGAS]
Studi kasus analisis Data Warehouse untuk toko online 'ElektroShop' yang menjual
perangkat teknologi dan aksesoris komputer.

Persyaratan Tugas:
1. Tabel fakta `fakta_penjualan` (min 12 transaksi: idtransaksi, idpelanggan, idproduk, idwaktu, jumlah, total_harga).
2. Tabel dimensi: `dim_pelanggan`, `dim_produk`, `dim_waktu` yang konsisten dengan FK pada fakta.
3. Skema Star: Total penjualan per kota & per kategori produk.
4. Skema Snowflake: Memecah dim_produk + dim_kategori, roll-up total per divisi.
5. Operasi OLAP:
   - Drill-down: Total penjualan per segmen pelanggan
   - Slice: Hanya transaksi di kota "Semarang"
   - Dice: Transaksi dengan total >= 1.000.000
6. Simpan seluruh tabel ke database SQLite `elektroshop.db` & query SQL JOIN nama produk + total penjualan.
"""

import pandas as pd
import numpy as np
import sqlite3

def main():
    print("=" * 75)
    print("TUGAS PRAKTIKUM 2: DATA WAREHOUSE ELEKTROSHOP (JANUARI - MARET 2026)")
    print("=" * 75)

    # --------------------------------------------------------------------------
    # 1. MEMBANGUN TABEL DIMENSI
    # --------------------------------------------------------------------------
    print("\n" + "=" * 50)
    print("1. MEMBANGUN TABEL DIMENSI")
    print("=" * 50)

    # Dimensi Pelanggan (id, nama, kota, provinsi, segmen)
    dim_pelanggan = pd.DataFrame({
        "idpelanggan": [1, 2, 3, 4, 5],
        "nama":        ["Ahmad Dahlan", "Bela Pertiwi", "Chandra Wijaya", "Diana Lestari", "Eko Prasetyo"],
        "kota":        ["Semarang", "Solo", "Semarang", "Yogyakarta", "Surabaya"],
        "provinsi":    ["Jawa Tengah", "Jawa Tengah", "Jawa Tengah", "D.I. Yogyakarta", "Jawa Timur"],
        "segmen":      ["Retail", "Corporate", "Retail", "Wholesale", "Corporate"]
    })

    # Dimensi Produk (id, nama, kategori, harga)
    dim_produk = pd.DataFrame({
        "idproduk":    [101, 102, 103, 104, 105],
        "nama_produk": ["Laptop ASUS ROG", "Smart TV Samsung 43\"", "Mouse Wireless Logitech", "Keyboard Mechanical RGB", "Smartphone Xiaomi 13"],
        "kategori":    ["Komputer & Laptop", "Elektronik Rumah", "Aksesoris PC", "Aksesoris PC", "Telekomunikasi"],
        "harga":       [14000000, 4500000, 150000, 450000, 3200000]
    })

    # Dimensi Waktu (id, tanggal, tahun, bulan, kuartal) - Rentang Jan - Mar 2026
    dim_waktu = pd.DataFrame({
        "idwaktu": [1, 2, 3, 4, 5, 6],
        "tanggal": ["2026-01-10", "2026-01-25", "2026-02-05", "2026-02-18", "2026-03-08", "2026-03-24"],
        "tahun":   [2026, 2026, 2026, 2026, 2026, 2026],
        "bulan":   ["Januari", "Januari", "Februari", "Februari", "Maret", "Maret"],
        "kuartal": ["Q1", "Q1", "Q1", "Q1", "Q1", "Q1"]
    })

    print("\n--- Tabel Dimensi Pelanggan ---")
    print(dim_pelanggan)
    print("\n--- Tabel Dimensi Produk ---")
    print(dim_produk)
    print("\n--- Tabel Dimensi Waktu ---")
    print(dim_waktu)

    # --------------------------------------------------------------------------
    # 2. MEMBANGUN TABEL FAKTA PENJUALAN (14 TRANSAKSI > MINIMAL 12)
    # --------------------------------------------------------------------------
    print("\n" + "=" * 50)
    print("2. MEMBANGUN TABEL FAKTA PENJUALAN")
    print("=" * 50)

    fakta_penjualan = pd.DataFrame({
        "idtransaksi": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014],
        "idpelanggan": [1,    2,    3,    4,    5,    1,    2,    3,    4,    5,    1,    3,    4,    2],
        "idproduk":    [101,  103,  102,  104,  105,  104,  101,  105,  103,  102,  103,  101,  105,  104],
        "idwaktu":     [1,    1,    2,    2,    3,    3,    4,    4,    5,    5,    6,    6,    6,    6],
        "jumlah":      [1,    10,   1,    8,    2,    2,    2,    1,    5,    3,    4,    1,    3,    5],
    })

    # Hitung Measure total_harga = jumlah * harga (diambil dari referensi harga produk)
    harga_dict = dict(zip(dim_produk["idproduk"], dim_produk["harga"]))
    fakta_penjualan["total_harga"] = fakta_penjualan["jumlah"] * fakta_penjualan["idproduk"].map(harga_dict)

    print("\n--- Tabel Fakta Penjualan (fakta_penjualan) ---")
    print(fakta_penjualan)

    # --------------------------------------------------------------------------
    # 3. IMPLEMENTASI SKEMA STAR & AGREGASI
    # --------------------------------------------------------------------------
    print("\n" + "=" * 50)
    print("3. IMPLEMENTASI SKEMA STAR & AGREGASI")
    print("=" * 50)

    star_df = fakta_penjualan.merge(dim_pelanggan, on="idpelanggan") \
                             .merge(dim_produk, on="idproduk") \
                             .merge(dim_waktu, on="idwaktu")

    print("\n--- Cuplikan Skema Star Gabungan ---")
    print(star_df[["idtransaksi", "nama", "kota", "nama_produk", "kategori", "jumlah", "total_harga"]].head(6))

    # 3.a Total Penjualan per Kota
    print("\n[A] Total Penjualan per Kota:")
    sales_per_kota = star_df.groupby("kota")["total_harga"].sum().reset_index()
    sales_per_kota["total_harga_rp"] = sales_per_kota["total_harga"].apply(lambda x: f"Rp {x:,.0f}")
    print(sales_per_kota)

    # 3.b Total Penjualan per Kategori Produk
    print("\n[B] Total Penjualan per Kategori Produk:")
    sales_per_kat = star_df.groupby("kategori")["total_harga"].sum().reset_index()
    sales_per_kat["total_harga_rp"] = sales_per_kat["total_harga"].apply(lambda x: f"Rp {x:,.0f}")
    print(sales_per_kat)

    # --------------------------------------------------------------------------
    # 4. IMPLEMENTASI SKEMA SNOWFLAKE & ROLL-UP DIVISI
    # --------------------------------------------------------------------------
    print("\n" + "=" * 50)
    print("4. IMPLEMENTASI SKEMA SNOWFLAKE (NORMALISASI)")
    print("=" * 50)

    # Pecah tabel kategori tersendiri
    dim_kategori = pd.DataFrame({
        "idkategori": [201, 202, 203, 204],
        "kategori":   ["Komputer & Laptop", "Elektronik Rumah", "Aksesoris PC", "Telekomunikasi"],
        "divisi":     ["Divisi IT Hardware", "Divisi Consumer Electronics", "Divisi IT Hardware", "Divisi Gadget & Mobile"]
    })

    # dim_produk memegang FK idkategori
    dim_produk_snow = pd.DataFrame({
        "idproduk":    [101, 102, 103, 104, 105],
        "nama_produk": ["Laptop ASUS ROG", "Smart TV Samsung 43\"", "Mouse Wireless Logitech", "Keyboard Mechanical RGB", "Smartphone Xiaomi 13"],
        "idkategori":  [201, 202, 203, 203, 204],
        "harga":       [14000000, 4500000, 150000, 450000, 3200000]
    })

    # Join berantai: fakta -> produk -> kategori
    snow_df = fakta_penjualan.merge(dim_produk_snow, on="idproduk") \
                             .merge(dim_kategori, on="idkategori")

    print("\n--- Cuplikan Hasil Join Skema Snowflake ---")
    print(snow_df[["idtransaksi", "nama_produk", "kategori", "divisi", "total_harga"]].head(6))

    # Roll-up: Total Penjualan per Divisi
    print("\n--- Roll-Up: Total Penjualan per Divisi ---")
    sales_per_divisi = snow_df.groupby("divisi")["total_harga"].sum().reset_index()
    sales_per_divisi["total_harga_rp"] = sales_per_divisi["total_harga"].apply(lambda x: f"Rp {x:,.0f}")
    print(sales_per_divisi)

    # --------------------------------------------------------------------------
    # 5. OPERASI OLAP (DRILL-DOWN, SLICE, DICE) & INTERPRETASI
    # --------------------------------------------------------------------------
    print("\n" + "=" * 50)
    print("5. OPERASI OLAP DAN INTERPRETASI BISNIS")
    print("=" * 50)

    # 5.a Drill-down: total penjualan per segmen pelanggan
    print("\n[5.A] DRILL-DOWN: Total Penjualan per Segmen Pelanggan")
    olap_segmen = star_df.groupby("segmen")["total_harga"].sum().reset_index()
    olap_segmen["total_harga_rp"] = olap_segmen["total_harga"].apply(lambda x: f"Rp {x:,.0f}")
    print(olap_segmen)
    print("-> INTERPRETASI: Segmen Corporate dan Retail memberikan kontribusi omset yang sangat tinggi,")
    print("   terutama didorong oleh pengadaan laptop korporat dan pembeli individual setia.")

    # 5.b Slice: hanya transaksi di kota "Semarang"
    print("\n[5.B] SLICE: Transaksi Khusus di Kota Semarang")
    slice_semarang = star_df[star_df["kota"] == "Semarang"]
    print(slice_semarang[["idtransaksi", "nama", "kota", "nama_produk", "jumlah", "total_harga"]])
    total_semarang = slice_semarang["total_harga"].sum()
    print(f"Total Nilai Transaksi di Kota Semarang: Rp {total_semarang:,.0f}")
    print("-> INTERPRETASI: Kota Semarang merupakan pasar utama lokal dengan transaksi berulang dari Ahmad Dahlan")
    print("   dan Chandra Wijaya yang membeli laptop, smart TV, dan smartphone.")

    # 5.c Dice: transaksi dengan total >= 1.000.000
    print("\n[5.C] DICE: Transaksi Bernilai Besar (Total Harga >= Rp 1.000.000)")
    dice_besar = star_df[star_df["total_harga"] >= 1000000]
    print(dice_besar[["idtransaksi", "nama", "kota", "nama_produk", "segmen", "total_harga"]])
    print(f"Jumlah Transaksi bernilai >= Rp 1.000.000: {len(dice_besar)} transaksi dari total {len(star_df)} transaksi.")
    print("-> INTERPRETASI: Sebagian besar transaksi (>70%) tergolong high-value basket size karena harga barang")
    print("   elektronik utama seperti laptop, smartphone, dan TV berada di atas 1 juta rupiah.")

    # --------------------------------------------------------------------------
    # 6. MENYIMPAN KE SQLITE elektroshop.db DAN QUERY SQL JOIN
    # --------------------------------------------------------------------------
    print("\n" + "=" * 50)
    print("6. MENYIMPAN KE SQLITE (elektroshop.db) & QUERY JOIN")
    print("=" * 50)

    con_db = sqlite3.connect("elektroshop.db")
    fakta_penjualan.to_sql("fakta_penjualan", con_db, if_exists="replace", index=False)
    dim_pelanggan.to_sql("dim_pelanggan",     con_db, if_exists="replace", index=False)
    dim_produk.to_sql("dim_produk",           con_db, if_exists="replace", index=False)
    dim_waktu.to_sql("dim_waktu",             con_db, if_exists="replace", index=False)
    dim_kategori.to_sql("dim_kategori",       con_db, if_exists="replace", index=False)

    print("[OK] Seluruh tabel berhasil disimpan ke database 'elektroshop.db'.")

    # Query SQL JOIN untuk menampilkan nama produk dan total penjualannya
    sql_tugas = """
        SELECT 
            p.nama_produk,
            p.kategori,
            SUM(f.jumlah) AS total_unit_terjual,
            SUM(f.total_harga) AS total_nominal_penjualan
        FROM fakta_penjualan AS f
        JOIN dim_produk AS p ON f.idproduk = p.idproduk
        GROUP BY p.idproduk, p.nama_produk, p.kategori
        ORDER BY total_nominal_penjualan DESC
    """

    hasil_sql_tugas = pd.read_sql_query(sql_tugas, con_db)
    hasil_sql_tugas["total_nominal_rp"] = hasil_sql_tugas["total_nominal_penjualan"].apply(lambda x: f"Rp {x:,.0f}")
    print("\n--- Hasil Query SQL JOIN: Total Penjualan per Nama Produk ---")
    print(hasil_sql_tugas[["nama_produk", "kategori", "total_unit_terjual", "total_nominal_rp"]])

    con_db.close()
    print("\n[OK] Koneksi database 'elektroshop.db' berhasil ditutup.")
    print("=" * 75)
    print("TUGAS PRAKTIKUM 2 SELESAI DENGAN SEMPURNA!")
    print("=" * 75)

if __name__ == "__main__":
    main()
