# BUKU PANDUAN LENGKAP PRAKTIKUM 2
## DATA WAREHOUSE DAN SKEMA STAR & SNOWFLAKE DENGAN PYTHON
**Mata Kuliah:** Data Mining  
**Program Studi:** S1 Teknik Informatika, Universitas Semarang (USM)  
**Waktu Pelaksanaan:** 13 Oktober 2026  
**Perangkat:** Komputer/Laptop, Python 3, Pandas, NumPy, SQLite3  

---

## 📌 DAFTAR ISI
1. [Pendahuluan & Konsep Data Warehouse](#1-pendahuluan--konsep-data-warehouse)
2. [Tabel Fakta vs Tabel Dimensi](#2-tabel-fakta-vs-tabel-dimensi)
3. [Arsitektur Skema: Star vs Snowflake](#3-arsitektur-skema-star-vs-snowflake)
4. [Operasi Analisis OLAP Multidimensi](#4-operasi-analisis-olap-multidimensi)
5. [Daftar File Praktikum & Struktur Folder](#5-daftar-file-praktikum--struktur-folder)
6. [Panduan Langkah Demi Langkah Modul](#6-panduan-langkah-demi-langkah-modul)
   - [Langkah 1: Membangun Tabel Fakta dan Dimensi](#langkah-1-membangun-tabel-fakta-dan-dimensi)
   - [Langkah 2: Implementasi Skema Star](#langkah-2-implementasi-skema-star)
   - [Langkah 3: Implementasi Skema Snowflake](#langkah-3-implementasi-skema-snowflake)
   - [Langkah 4: Operasi OLAP (Roll-up, Drill-down, Slice, Dice)](#langkah-4-operasi-olap)
   - [Langkah 5: Persistensi ke Database SQLite & Query JOIN](#langkah-5-persistensi-ke-database-sqlite)
7. [Penyelesaian Tugas Studi Kasus: Toko Online ElektroShop](#7-penyelesaian-tugas-studi-kasus-elektroshop)
8. [Rangkuman & Referensi](#8-rangkuman--referensi)

---

## 1. PENDAHULUAN & KONSEP DATA WAREHOUSE

### Apa itu Data Warehouse?
**Data Warehouse (Gudang Data)** adalah sistem basis data yang dirancang khusus untuk memfasilitasi pelaporan analisis (**OLAP - Online Analytical Processing**) dan pengambilan keputusan strategis manajerial bisnis, bukan untuk pemrosesan transaksi operasional detik demi detik (**OLTP - Online Transaction Processing**).

### Tiga Prinsip Utama Data Warehouse (W.H. Inmon):
1. **Subject-Oriented:** Data disusun dan dikelompokkan berdasarkan entitas bisnis utama (misalnya: *Penjualan*, *Pelanggan*, *Produk*), bukan berdasarkan alur aplikasi.
2. **Integrated:** Data dikumpulkan dan diseragamkan formatnya dari berbagai sumber heterogen (misalnya CRM, kasir POS, database website toko).
3. **Time-Variant:** Data menyimpan histori rentang waktu (misalnya kuartal, bulan, tahun) sehingga tren masa lalu dapat dibandingkan secara akurat.
4. **Non-Volatile:** Data bersifat stabil; setelah dimuat, data tidak diedit atau dihapus secara sembarangan, melainkan hanya dibaca untuk analisis (*read-only*).

---

## 2. TABEL FAKTA VS TABEL DIMENSI

Dalam pemodelan data multidimensi, tabel diklasifikasikan menjadi dua jenis utama:

| Komponen | Definisi & Karakteristik | Isi & Contoh Kolom |
| :--- | :--- | :--- |
| **Tabel Fakta (*Fact Table*)** | Tabel utama di pusat model data yang mencatat peristiwa kuantitatif bisnis yang terjadi. | **Measures:** Jumlah terjual, harga satuan, total harga.<br>**Foreign Keys (FK):** `id_pelanggan`, `id_produk`, `id_waktu`. |
| **Tabel Dimensi (*Dimension Table*)** | Tabel pendukung yang memberikan konteks deskriptif (*siapa, apa, kapan, di mana*) terhadap angka pada tabel fakta. | **Atribut Deskriptif:** Nama pelanggan, kota, segmen, nama produk, kategori barang, tanggal, bulan, kuartal. |

---

## 3. ARSITEKTUR SKEMA: STAR VS SNOWFLAKE

```
SKEMA STAR                                 SKEMA SNOWFLAKE
====================================       ==========================================
             dim_produk                                dim_kategori <--- dim_produk
            ┌───────────────┐                         ┌────────────┐    ┌───────────────┐
            │ id_produk     │                         │ id_kategori│    │ id_produk     │
            │ nama_produk   │                         │ kategori   │    │ nama_produk   │
            │ kategori      │                         │ divisi     │    │ id_kategori   │
            │ harga_satuan  │                         └────────────┘    │ harga_satuan  │
            └───────┬───────┘                                           └───────┬───────┘
                    │                                                           │
┌──────────────┐    │                                      ┌──────────────┐     │
│dim_pelanggan │    ▼                                      │dim_pelanggan │     ▼
│id_pelanggan  │   FACT (sales)                            │id_pelanggan  │    FACT (sales)
│nama          ├──►┌──────────────┐                        │nama          ├───►┌──────────────┐
│kota          │   │ id_transaksi │                        │kota          │    │ id_transaksi │
│segmen        │   │ id_pelanggan │                        │segmen        │    │ id_pelanggan │
└──────────────┘   │ id_produk    │                        └──────────────┘    │ id_produk    │
                   │ id_waktu     │                                            │ id_waktu     │
┌──────────────┐   │ jumlah       │                        ┌──────────────┐    │ jumlah       │
│dim_waktu     ├──►│ total_harga  │                        │dim_waktu     ├───►│ total_harga  │
│id_waktu      │   └──────────────┘                        │id_waktu      │    └──────────────┘
│tanggal, bulan│                                           │tanggal, bulan│
└──────────────┘                                           └──────────────┘
(Dimensi Tidak Dinormalisasi / Denormalized)                (Dimensi Dinormalisasi / Normalized)
```

### Perbandingan Karakteristik:
- **Skema Star:**
  - Tabel dimensi bersifat **denormalized** (tidak dinormalisasi), sehingga atribut tersimpan langsung di satu tabel.
  - Kelebihan: Relasi sederhana (1 hop join), performa query analitis sangat cepat.
  - Kekurangan: Ada redundansi data teks pada tabel dimensi.
- **Skema Snowflake:**
  - Tabel dimensi **dinormalisasi** (dipecah menjadi beberapa tabel hirarkis bertingkat, misal: `dim_produk` dihubungkan ke `dim_kategori`).
  - Kelebihan: Menghilangkan redundansi data dan menghemat ruang penyimpanan.
  - Kekurangan: Query membutuhkan join berantai (*multi-hop join*) sehingga sedikit lebih lambat.

---

## 4. OPERASI ANALISIS OLAP MULTIDIMENSI

1. **Roll-up:** Meringkas data ke level hierarki yang lebih tinggi (agregasi generalisasi).  
   *Contoh:* Dari level transaksi produk harian diringkas menjadi total penjualan per Kota atau Divisi.
2. **Drill-down:** Membedah data ke level hierarki yang lebih rinci (spesifikasi detail).  
   *Contoh:* Dari level Kota digali rinciannya ke masing-masing Segmen Pelanggan.
3. **Slice:** Mengambil satu "iris" data berdasarkan tepat **satu nilai pada satu dimensi**.  
   *Contoh:* Menampilkan hanya transaksi untuk `kota == 'Semarang'`.
4. **Dice:** Mengambil sub-kubus data berdasarkan **kombinasi dua atau lebih kriteria filter**.  
   *Contoh:* Transaksi yang terjadi di `kota == 'Semarang'` DAN `total_harga > 500.000`.

---

## 5. DAFTAR FILE PRAKTIKUM & STRUKTUR FOLDER

Proyek ini telah disusun dengan struktur yang sangat rapi dan lengkap:

```
praktikum2/
├── praktikum2.docx                  # Dokumen modul asli
├── praktikum2.ipynb                 # Jupyter Notebook interaktif lengkap
├── praktikum2_modul.py              # Skrip gabungan modul langkah 1 s/d 5
├── tugas_praktikum2.py              # Skrip penyelesaian studi kasus ElektroShop
├── data_warehouse.db                # Database SQLite hasil ekspor modul
├── elektroshop.db                   # Database SQLite hasil ekspor tugas ElektroShop
├── BUKU_PANDUAN_PRAKTIKUM_2.md      # Buku panduan lengkap (file ini)
│
├── 1_1_tabel_fakta.py               # Langkah 1.1: Pembuatan tabel fakta & measure
├── 1_2_tabel_dimensi.py             # Langkah 1.2: Pembuatan dimensi pelanggan, produk, waktu
├── 1_3_struktur_data_warehouse.py   # Langkah 1.3: Verifikasi shape & dtypes
├── 2_1_skema_star.py                # Langkah 2.1: Merge fakta & dimensi skema star
├── 2_2_agregasi_skema_star.py       # Langkah 2.2: Agregasi per kota & segmen
├── 3_1_normalisasi_snowflake.py     # Langkah 3.1: Normalisasi produk & kategori
├── 3_2_join_dan_agregasi_snowflake.py # Langkah 3.2: Multi-join & roll-up divisi
├── 4_1_olap_rollup.py               # Langkah 4.1: Kubus data & operasi Roll-up
├── 4_2_olap_drilldown.py            # Langkah 4.2: Operasi Drill-down & Pivot 2D
├── 4_3_olap_slice.py                # Langkah 4.3: Operasi Slice kota Semarang
├── 4_4_olap_dice.py                 # Langkah 4.4: Operasi Dice ganda
├── 5_1_simpan_sqlite.py             # Langkah 5.1: Ekspor tabel ke SQLite (to_sql)
├── 5_2_query_sql_join.py            # Langkah 5.2: Query SQL JOIN langsung
│
└── kode_murni/                      # Folder versi kode bersih (tanpa docstring panjang)
    ├── 1_1_tabel_fakta.py
    ├── 1_2_tabel_dimensi.py
    ├── 1_3_struktur_data_warehouse.py
    ├── 2_1_skema_star.py
    ├── 2_2_agregasi_skema_star.py
    ├── 3_1_normalisasi_snowflake.py
    ├── 3_2_join_dan_agregasi_snowflake.py
    ├── 4_1_olap_rollup.py
    ├── 4_2_olap_drilldown.py
    ├── 4_3_olap_slice.py
    ├── 4_4_olap_dice.py
    ├── 5_1_simpan_sqlite.py
    ├── 5_2_query_sql_join.py
    ├── praktikum2_modul.py
    └── tugas_praktikum2.py
```

---

## 6. PANDUAN LANGKAH DEMI LANGKAH MODUL

### Langkah 1: Membangun Tabel Fakta dan Dimensi
- **Tabel Fakta (`sales`):**
  Menyimpan 8 transaksi penjualan dengan FK `id_pelanggan`, `id_produk`, dan `id_waktu`.
  Measure dihitung: `total_harga = jumlah * harga_satuan`.
- **Tabel Dimensi:**
  - `dim_pelanggan`: Atribut nama, kota, provinsi, segmen.
  - `dim_produk`: Atribut nama produk, kategori, harga satuan.
  - `dim_waktu`: Atribut tanggal, tahun, bulan, kuartal, hari.

### Langkah 2: Implementasi Skema Star
- Penggabungan (*merge*) tabel fakta `sales` ke `dim_pelanggan` dan `dim_waktu`.
- Agregasi bisnis:
  - Total penjualan per kota: `star.groupby("kota")["total_harga"].sum()`
  - Total penjualan per segmen: `star.groupby("segmen")["total_harga"].sum()`

### Langkah 3: Implementasi Skema Snowflake
- Memecah dimensi produk menjadi dua tabel: `dim_produk_snow` dan `dim_kategori`.
- Join berantai 3 tabel: `sales -> dim_produk_snow -> dim_kategori`.
- Roll-up omset per divisi: `snow.groupby("divisi")["total_harga"].sum()`.

### Langkah 4: Operasi OLAP
- Merakit kubus data lengkap (menggabungkan seluruh dimensi ke tabel fakta).
- **Roll-up:** Agregasi omset per kota.
- **Drill-down:** Agregasi per segmen pelanggan dan Pivot Table Matriks 2D (Kota vs Kategori).
- **Slice:** Filter khusus wilayah Semarang.
- **Dice:** Filter wilayah Semarang dengan nilai transaksi di atas Rp 500.000.

### Langkah 5: Persistensi ke Database SQLite
- Menyimpan DataFrames ke basis data menggunakan `df.to_sql(table_name, con, if_exists="replace", index=False)`.
- Mengakses kembali data menggunakan query SQL murni dengan `pd.read_sql_query(query, con)`.

---

## 7. PENYELESAIAN TUGAS STUDI KASUS: ELEKTROSHOP

### Deskripsi & Ketentuan Tugas:
- **Entitas:** Toko Online ElektroShop (Januari – Maret 2026 / Q1 2026).
- **Tabel Fakta:** 14 Transaksi penjualan (memenuhi syarat minimal 12).
- **Tabel Dimensi:** Pelanggan (5 pelanggan), Produk (5 produk), Waktu (6 pencatatan rentang Jan-Mar 2026).
- **Hasil Agregasi Skema Star:**
  - Penjualan per Kota: Semarang (Rp 37.200.000), Solo (Rp 31.750.000), Surabaya (Rp 19.900.000), Yogyakarta (Rp 13.950.000).
  - Penjualan per Kategori: Komputer & Laptop (Rp 56.000.000), Telekomunikasi (Rp 19.200.000), Elektronik Rumah (Rp 18.000.000), Aksesoris PC (Rp 9.600.000).
- **Hasil Skema Snowflake (Roll-up Divisi):**
  - Divisi IT Hardware: Rp 65.600.000
  - Divisi Gadget & Mobile: Rp 19.200.000
  - Divisi Consumer Electronics: Rp 18.000.000
- **Hasil Analisis OLAP:**
  - *Drill-down Segmen:* Corporate (Rp 51.650.000), Retail (Rp 37.200.000), Wholesale (Rp 13.950.000).
  - *Slice Semarang:* 6 transaksi dengan total transaksi Rp 37.200.000.
  - *Dice (>= 1.000.000):* 11 transaksi bernilai besar didominasi unit laptop, TV, dan smartphone.
- **Persistensi Database:** Tersimpan lengkap pada database `elektroshop.db`.

---

## 8. RANGKUMAN & REFERENSI
- Modul ini mengokohkan pemahaman mendasar bahwa arsitektur data analitis modern memisahkan fakta kuantitatif dan konteks dimensi.
- Skema Star adalah pilihan terbaik untuk kecepatan akses pelaporan, sedangkan Skema Snowflake efektif ketika normalisasi dan penghematan memori menjadi prioritas utama.
- Library **Pandas** dan **SQLite** di Python memberikan ekosistem yang fleksibel untuk memodelkan proses ETL secara menyeluruh.

---
*Laboratorium Data Mining — Program Studi Teknik Informatika, Universitas Semarang (USM)*
