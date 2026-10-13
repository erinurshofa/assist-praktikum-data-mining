# ==============================================================================
# SUB-BAB 1.2: VERIFIKASI INSTALASI LIBRARY DATA SCIENCE
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita sedang "mengecek kelengkapan alat kerja".
   Ibarat seorang koki yang mau memasak di dapur baru, sebelum mulai memotong bahan,
   dia harus memastikan pisau, wajan, kompor, dan bumbu sudah tersedia di tempatnya.
   Di sini, kita mengimpor 5 "alat masak" data science:
   - NumPy & Pandas (alat olah data)
   - Matplotlib & Seaborn (alat gambar grafik)
   - SciPy (alat hitung rumus matematika/statistik)

2. KENAPA INI PENTING?
   Biar kita tidak panik di tengah jalan! Kalau ada alat yang belum terpasang,
   komputer akan langsung memberi tahu di awal, bukannya mendadak error
   saat kita sudah setengah jalan menganalisis ribuan data.

3. CONTOH DI DUNIA KERJA:
   Di perusahaan seperti Gojek atau Tokopedia, setiap ada karyawan/analis baru,
   hal pertama yang mereka lakukan di laptop kerja adalah mengecek alat-alat ini.
   Tujuannya agar program tim yang sudah ada bisa langsung jalan lancar tanpa macet.
"""

import numpy
import pandas
import matplotlib
import seaborn
import scipy

print("=== CEK ALAT DATA SCIENCE ===")
print("Semua alat (library) sudah terpasang dengan lengkap dan siap dipakai!\n")
print(f"Versi NumPy      : {numpy.__version__}")
print(f"Versi Pandas     : {pandas.__version__}")
print(f"Versi Matplotlib : {matplotlib.__version__}")
print(f"Versi Seaborn    : {seaborn.__version__}")
print(f"Versi SciPy      : {scipy.__version__}")
