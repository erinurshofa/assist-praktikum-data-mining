# ==============================================================================
# MODUL PRAKTIKUM 1: PENGENALAN DATA MINING DENGAN PYTHON
# Mata Kuliah: Data Mining - Universitas Semarang (USM)
# ==============================================================================

# ==============================================================================
# PRAKTIKUM 2: PENGOLAHAN DATA DASAR SECARA STATISTIK
# ==============================================================================

# ------------------------------------------------------------------------------
# 2.1 Membuat DataFrame Sederhana
# ------------------------------------------------------------------------------
import pandas as pd
import numpy as np

# Membuat DataFrame dari data nilai mahasiswa
data = {
    "Nama"   : ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"],
    "JK"     : ["L", "L", "P", "P", "L", "L", "P"],
    "Usia"   : [19, 20, 18, 21, 20, 19, 20],
    "UTS"    : [78, 85, 92, 60, 70, 88, 75],
    "UAS"    : [80, 88, 95, 65, 72, 84, 90]
}

df = pd.DataFrame(data)
print(df)

# ------------------------------------------------------------------------------
# 2.2 Melihat Ringkasan Data
# ------------------------------------------------------------------------------
# Menampilkan 3 baris pertama
print(df.head(3))

# Menampilkan info tipe data dan jumlah non-null
print(df.info())

# Menampilkan ringkasan statistik deskriptif
print(df.describe())

# ------------------------------------------------------------------------------
# 2.3 Ukuran Pemusatan Data (Central Tendency)
# ------------------------------------------------------------------------------
# Rata-rata (mean)
print("Rata-rata UTS :", df["UTS"].mean())

# Median
print("Median UAS    :", df["UAS"].median())

# Modus (nilai paling sering muncul)
print("Modus Usia    :")
print(df["Usia"].mode())

# Nilai minimum dan maksimum
print("Min UTS :", df["UTS"].min())
print("Max UTS :", df["UTS"].max())

# ------------------------------------------------------------------------------
# 2.4 Ukuran Penyebaran Data (Dispersion)
# ------------------------------------------------------------------------------
# Rentang (range) = max - min
rentang = df["UTS"].max() - df["UTS"].min()
print("Rentang UTS :", rentang)

# Varians
print("Varians UTS :", df["UTS"].var())

# Simpangan baku
print("Simpangan baku UTS :", df["UTS"].std())

# Kuartil
print("Kuartil UTS:")
print(df["UTS"].quantile([0.25, 0.50, 0.75]))

# ------------------------------------------------------------------------------
# 2.5 Korelasi Antar Variabel
# ------------------------------------------------------------------------------
# Matriks korelasi kolom numerik
print(df[["Usia", "UTS", "UAS"]].corr())

# ------------------------------------------------------------------------------
# 2.6 Seleksi dan Filter Data
# ------------------------------------------------------------------------------
# Memilih kolom tertentu
print(df[["Nama", "UTS"]])

# Memilih baris berdasarkan kondisi (filter)
mahasiswa_lulus = df[df["UTS"] >= 75]
print("Mahasiswa dengan UTS >= 75:")
print(mahasiswa_lulus)

# Pengelompokan berdasarkan kategori (JK)
print("Rata-rata UAS per jenis kelamin:")
print(df.groupby("JK")["UAS"].mean())

# ------------------------------------------------------------------------------
# 2.7 Latihan Ringkas (Statistik)
# ------------------------------------------------------------------------------
# 1. Rata-rata usia seluruh mahasiswa
print("Rata-rata usia seluruh mahasiswa:", df["Usia"].mean())

# 2. Mahasiswa dengan nilai UTS tertinggi
print("Mahasiswa dengan UTS tertinggi:", df.loc[df["UTS"].idxmax(), "Nama"])

# 3. Simpangan baku nilai UAS
print("Simpangan baku UAS:", df["UAS"].std())

# 4. Apakah ada korelasi antara nilai UTS dan UAS? Interpretasikan.
print("Korelasi UTS dan UAS:", df["UTS"].corr(df["UAS"]))

# 5. Rata-rata UAS untuk mahasiswa laki-laki dan perempuan
print("Rata-rata UAS per jenis kelamin:")
print(df.groupby("JK")["UAS"].mean())


# ==============================================================================
# PRAKTIKUM 3: VISUALISASI DATA DENGAN PYTHON
# ==============================================================================
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# 3.1 Konfigurasi Awal dan Grafik Garis (Line Chart)
# ------------------------------------------------------------------------------
# Data contoh penjualan per bulan (dalam juta rupiah)
bulan    = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul"]
penjualan = [12, 15, 13, 18, 20, 17, 25]

plt.figure(figsize=(8, 5))
plt.plot(bulan, penjualan, marker="o", color="blue", linewidth=2)
plt.title("Tren Penjualan per Bulan")
plt.xlabel("Bulan")
plt.ylabel("Penjualan (juta rupiah)")
plt.grid(True)
plt.show()

# ------------------------------------------------------------------------------
# 3.2 Diagram Batang (Bar Chart)
# ------------------------------------------------------------------------------
# Rata-rata UAS per jenis kelamin
rata_per_jk = df.groupby("JK")["UAS"].mean()

plt.figure(figsize=(6, 5))
plt.bar(rata_per_jk.index, rata_per_jk.values, color=["skyblue", "salmon"])
plt.title("Rata-rata UAS Berdasarkan Jenis Kelamin")
plt.xlabel("Jenis Kelamin")
plt.ylabel("Rata-rata UAS")
plt.show()

# ------------------------------------------------------------------------------
# 3.3 Histogram dan Distribusi Data
# ------------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df["UTS"], bins=5, color="green", edgecolor="black")
plt.title("Distribusi Nilai UTS")
plt.xlabel("Nilai UTS")
plt.ylabel("Frekuensi")
plt.show()

# ------------------------------------------------------------------------------
# 3.4 Diagram Sebar (Scatter Plot)
# ------------------------------------------------------------------------------
plt.figure(figsize=(7, 5))
plt.scatter(df["UTS"], df["UAS"], color="purple")
plt.title("Hubungan Nilai UTS dan UAS")
plt.xlabel("Nilai UTS")
plt.ylabel("Nilai UAS")
plt.show()

# ------------------------------------------------------------------------------
# 3.5 Boxplot
# ------------------------------------------------------------------------------
import seaborn as sns

plt.figure(figsize=(7, 5))
sns.boxplot(y=df["UAS"], color="orange")
plt.title("Boxplot Nilai UAS")
plt.ylabel("Nilai UAS")
plt.show()

# ------------------------------------------------------------------------------
# 3.6 Diagram Lingkaran (Pie Chart)
# ------------------------------------------------------------------------------
# Komposisi jenis kelamin
komposisi = df["JK"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(komposisi.values, labels=komposisi.index, autopct="%1.1f%%",
        startangle=90, colors=["skyblue", "salmon"])
plt.title("Komposisi Jenis Kelamin Mahasiswa")
plt.show()

# ------------------------------------------------------------------------------
# 3.7 Heatmap Korelasi (Seaborn)
# ------------------------------------------------------------------------------
plt.figure(figsize=(6, 5))
sns.heatmap(df[["Usia", "UTS", "UAS"]].corr(), annot=True,
            cmap="coolwarm", fmt=".2f", square=True)
plt.title("Heatmap Korelasi Antar Variabel")
plt.show()

# ------------------------------------------------------------------------------
# 3.8 Menyimpan Gambar Hasil Visualisasi
# ------------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df["UAS"], bins=5, color="teal", edgecolor="black")
plt.title("Distribusi Nilai UAS")
plt.xlabel("Nilai UAS")
plt.ylabel("Frekuensi")
plt.savefig("histogram_uas.png", dpi=150)
plt.show()
