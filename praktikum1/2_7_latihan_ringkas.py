# ==============================================================================
# SUB-BAB 2.7: LATIHAN RINGKAS (STATISTIK)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Ini adalah latihan praktik langsung untuk menjawab 5 pertanyaan umum menggunakan Python:
   - Pertanyaan 1: Berapa rata-rata usia seluruh mahasiswa? -> pakai `.mean()`
   - Pertanyaan 2: Siapa mahasiswa dengan nilai UTS tertinggi? -> pakai `.idxmax()` untuk mengambil namanya
   - Pertanyaan 3: Berapa simpangan baku nilai UAS? -> pakai `.std()`
   - Pertanyaan 4: Apakah ada hubungan antara nilai UTS dan UAS? -> pakai `.corr()`
   - Pertanyaan 5: Berapa rata-rata nilai UAS laki-laki dan perempuan? -> pakai `.groupby()`

2. KENAPA KITA HARUS BISA MENJAWAB SEPERTI INI?
   Karena seorang analis data bukan cuma tukang ketik kode, tapi orang yang bertugas
   memberikan jawaban jelas dan ringkas saat bos atau dosen bertanya.

3. CONTOH DI DUNIA KERJA:
   Saat bos bertanya: "Berapa rata-rata usia pembeli kita? Dan siapa pelanggan paling royal bulan ini?",
   kamu bisa menjawabnya dengan cepat dan tepat menggunakan kode-kode simpel di bawah ini.
"""

import pandas as pd
import numpy as np

# Inisialisasi data (dari Sub-bab 2.1)
data = {
    "Nama"   : ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"],
    "JK"     : ["L", "L", "P", "P", "L", "L", "P"],
    "Usia"   : [19, 20, 18, 21, 20, 19, 20],
    "UTS"    : [78, 85, 92, 60, 70, 88, 75],
    "UAS"    : [80, 88, 95, 65, 72, 84, 90]
}
df = pd.DataFrame(data)

# --- Kode Sub-bab 2.7: Menjawab Pertanyaan Latihan Ringkas ---
print("=== JAWABAN LATIHAN RINGKAS STATISTIK ===\n")

# 1. Berapa rata-rata usia seluruh mahasiswa?
print("1. Rata-rata usia mahasiswa :", round(df["Usia"].mean(), 1), "tahun")

# 2. Siapa mahasiswa dengan nilai UTS tertinggi?
nama_juara = df.loc[df["UTS"].idxmax(), "Nama"]
nilai_juara = df["UTS"].max()
print(f"2. Mahasiswa UTS tertinggi  : {nama_juara} (Nilai: {nilai_juara})")

# 3. Berapa simpangan baku nilai UAS?
print("3. Simpangan baku nilai UAS :", round(df["UAS"].std(), 2))

# 4. Apakah ada korelasi antara nilai UTS dan UAS? Interpretasikan.
korelasi = df["UTS"].corr(df["UAS"])
print(f"4. Nilai korelasi UTS & UAS : {korelasi:.2f}")
print("   Artinya: Hubungannya SANGAT KUAT dan POSITIF. Mahasiswa yang nilai UTS-nya bagus hampir pasti nilai UAS-nya juga bagus.")

# 5. Berapa rata-rata UAS untuk mahasiswa laki-laki dan perempuan?
print("\n5. Rata-rata UAS berdasarkan jenis kelamin:")
print(df.groupby("JK")["UAS"].mean())
