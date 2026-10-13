# ==============================================================================
# SUB-BAB 3.1: KONFIGURASI AWAL DAN GRAFIK GARIS (LINE CHART)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita sedang menggambar grafik garis dari data urutan waktu (dari Januari sampai Juli).
   - `plt.plot(...)`   : Perintah menghubungkan titik-titik data dengan garis lurus.
   - `marker='o'`      : Memberi bulatan kecil di setiap titik bulan agar jelas posisinya.
   - `plt.grid(True)`  : Menampilkan garis kotak-kotak latar belakang (seperti buku strimin) agar mudah dibaca.
   - `plt.show()`      : Perintah "Tampilkan gambarnya di layar!".

2. KAPAN KITA HARUS PAKAI GRAFIK GARIS?
   Gunakan grafik garis saat datanya punya URUTAN WAKTU (hari, bulan, atau tahun).
   Grafik ini paling jago memperlihatkan apakah trennya sedang naik, turun, atau mendatar.

3. CONTOH DI DUNIA KERJA:
   - Toko Online & Pebisnis: Memantau grafik omset penjualan setiap bulan.
     Kalau garisnya menukik tajam ke bawah di bulan Juni, bos bisa langsung tahu ada masalah
     dan cepat-cepat bikin promo baru.
   - Cuaca & Suhu: Memantau naik-turunnya suhu udara dari pagi sampai malam.
"""

import matplotlib.pyplot as plt

# Data contoh penjualan per bulan (dalam juta rupiah)
bulan     = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul"]
penjualan = [12, 15, 13, 18, 20, 17, 25]

plt.figure(figsize=(8, 5))
plt.plot(bulan, penjualan, marker="o", color="blue", linewidth=2)
plt.title("Tren Penjualan per Bulan", fontsize=14, fontweight="bold")
plt.xlabel("Bulan", fontsize=11)
plt.ylabel("Penjualan (juta rupiah)", fontsize=11)
plt.grid(True)
plt.show()
