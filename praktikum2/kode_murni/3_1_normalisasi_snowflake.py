import pandas as pd

# Tabel kategori (dimensi ke-2 hasil normalisasi produk)
dim_kategori = pd.DataFrame({
    "id_kategori": [10, 20],
    "kategori":    ["Elektronik", "Perlengkapan"],
    "divisi":      ["Teknologi", "Logistik"],
})

# dim_produk sekarang memegang Foreign Key (FK) id_kategori, bukan menempel kategori langsung
dim_produk_snow = pd.DataFrame({
    "id_produk":    [1, 2, 3],
    "nama_produk":  ["Laptop", "Printer", "Tinta"],
    "id_kategori":  [10, 10, 20],
    "harga_satuan": [8000000, 1500000, 25000],
})

print("=" * 60)
print("HASIL LANGKAH 3.1: STRUKTUR NORMALISASI DIMENSI SNOWFLAKE")
print("=" * 60)

print("\n--- [1] TABEL DIM_KATEGORI (Level Lebih Tinggi) ---")
print(dim_kategori)

print("\n--- [2] TABEL DIM_PRODUK (Memegang FK id_kategori) ---")
print(dim_produk_snow)
