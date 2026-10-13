# ==============================================================================
# SUB-BAB 2.4: UKURAN PENYEBARAN DATA (DISPERSION)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita ingin tahu: "Apakah data kita ini kumpulnya kompak, atau malah mencar-mencar berantakan?"
   - `Rentang (Range)` : Selisih jarak dari yang paling pintar ke yang paling kurang (Max dikurangi Min).
   - `Varians & Simpangan Baku (Standard Deviation)` : Ukuran kekompakan data.
     * Semakin KECIL angkanya = Data makin kompak, stabil, dan kemampuannya seragam.
     * Semakin BESAR angkanya = Data makin bervariasi, jomplang, dan tidak menentu.
   - `Kuartil (Q1, Q2, Q3)` : Membagi urutan data menjadi 4 bagian sama rata (seperti memotong kue jadi 4 potong).

2. KENAPA RATA-RATA SAJA TIDAK CUKUP?
   Bayangkan ada dua kelas:
   - Kelas A nilainya: 70, 70, 70, 70 (Rata-rata 70, Simpangan Baku = 0 -> Sangat kompak & stabil!)
   - Kelas B nilainya: 40, 50, 95, 95 (Rata-rata 70 juga, tapi Simpangan Baku besar -> Jomplang banget!)
   Dengan menghitung simpangan baku, kita langsung tahu bahwa Kelas B sedang punya masalah ketimpangan belajar.

3. CONTOH DI DUNIA KERJA:
   - Investasi Reksa Dana & Saham: Investor pemula sering memilih produk yang simpangan bakunya kecil
     karena grafiknya tenang dan tidak bikin jantungan naik-turun drastis.
   - Pabrik Minuman Botol: Mesin pengisi botol harus punya simpangan baku mendekati 0 agar isi setiap botol
     tepat 500 ml dan tidak ada konsumen yang merasa rugi.
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

# --- Kode Sub-bab 2.4 ---
print("=== UKURAN KEKOMPAKAN / SEBARAN DATA ===")
# Rentang (range) = max - min
rentang = df["UTS"].max() - df["UTS"].min()
print("Rentang Selisih UTS :", rentang)

# Varians
print("Varians UTS         :", df["UTS"].var())

# Simpangan baku
print("Simpangan Baku UTS  :", df["UTS"].std())

# Kuartil
print("\nKuartil UTS (Batas 25%, 50%, dan 75%):")
print(df["UTS"].quantile([0.25, 0.50, 0.75]))
