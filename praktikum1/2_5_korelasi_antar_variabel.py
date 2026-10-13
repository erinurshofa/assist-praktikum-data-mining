# ==============================================================================
# SUB-BAB 2.5: KORELASI ANTAR VARIABEL
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita sedang mengecek: "Apakah hal A ada hubungannya dengan hal B?"
   Nilai korelasi selalu berada di antara angka -1 sampai +1:
   - Angka mendekati +1 (Korelasi Positif) : Searah. Kalau A naik, B ikut naik.
     (Contoh: Makin banyak belajar, makin tinggi nilai ujian).
   - Angka mendekati -1 (Korelasi Negatif) : Kebalikannya. Kalau A naik, B malah turun.
     (Contoh: Makin banyak main game begadang, makin turun nilai ujian).
   - Angka mendekati 0  (Tidak Ada Korelasi) : Cuek bebek, tidak ada hubungannya sama sekali.
     (Contoh: Ukuran sepatu tidak ada hubungannya dengan nilai matematika).

2. KENAPA KITA PERLU TAHU KORELASI?
   Biar kita tidak buang-buang waktu mengotak-atik variabel yang salah.
   Kalau kita ingin meningkatkan nilai UAS siswa, kita harus cari tahu faktor apa saja
   yang punya korelasi positif tinggi dengan nilai UAS.

3. CONTOH DI DUNIA KERJA:
   - Toko Online & Marketing: Menghitung korelasi antara "Besarnya Diskon" dengan "Jumlah Barang Terjual".
     Kalau korelasinya mendekati +1, berarti strategi diskon terbukti manjur mendongkrak penjualan.
   - Manajemen Baterai Smartphone: Menganalisis korelasi antara tingkat kecerahan layar HP dengan
     seberapa cepat baterai habis.
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

# --- Kode Sub-bab 2.5 ---
print("=== TABEL HUBUNGAN ANTAR ANGKA (KORELASI) ===")
print(df[["Usia", "UTS", "UAS"]].corr())
