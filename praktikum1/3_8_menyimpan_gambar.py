# ==============================================================================
# SUB-BAB 3.8: MENYIMPAN GAMBAR HASIL VISUALISASI
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita sedang "memotret" grafik yang sudah kita buat lalu menyimpannya menjadi file gambar (PNG):
   - `plt.show()`     : Hanya memunculkan gambar sementara di layar monitor kamu (kalau jendelanya ditutup, ya hilang).
   - `plt.savefig()`  : Menyimpan gambar secara permanen ke dalam folder komputermu, persis seperti klik "Save As".
   - `dpi=150`        : Dots Per Inch (kualitas ketajaman gambar). Semakin tinggi angkanya, gambar makin jernih
                        dan tidak pecah/buram saat dizoom atau dicetak di kertas.

2. KENAPA INI PENTING BANGET?
   Karena di dunia nyata, bos atau dosen kamu tidak akan membuka kodingan Python kamu satu per satu!
   Mereka ingin melihat hasil grafikmu yang sudah ditempel rapi di laporan Word, slide presentasi PowerPoint,
   atau file dokumen PDF.

3. CONTOH DI DUNIA KERJA:
   - Membuat Laporan Otomatis Setiap Pagi: Script Python berjalan otomatis jam 6 pagi untuk mengolah data
     penjualan kemarin, membuat 5 grafik, menyimpannya jadi gambar PNG, lalu otomatis melampirkannya
     ke email laporan yang dikirim ke manajer.
   - Bikin Skripsi / Laporan Magang: Menyimpan grafik dengan `dpi=150` atau `dpi=300` agar saat laporan
     diprint, gambarnya terlihat sangat profesional dan tajam.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Inisialisasi data (dari Sub-bab 2.1)
data = {
    "Nama"   : ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"],
    "JK"     : ["L", "L", "P", "P", "L", "L", "P"],
    "Usia"   : [19, 20, 18, 21, 20, 19, 20],
    "UTS"    : [78, 85, 92, 60, 70, 88, 75],
    "UAS"    : [80, 88, 95, 65, 72, 84, 90]
}
df = pd.DataFrame(data)

# --- Kode Sub-bab 3.8 ---
plt.figure(figsize=(8, 5))
plt.hist(df["UAS"], bins=5, color="teal", edgecolor="black")
plt.title("Distribusi Nilai UAS", fontsize=14, fontweight="bold")
plt.xlabel("Nilai UAS", fontsize=11)
plt.ylabel("Frekuensi (Banyaknya Mahasiswa)", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Menyimpan grafik sebagai file gambar dengan resolusi tajam (150 DPI)
nama_file = "histogram_uas.png"
plt.savefig(nama_file, dpi=150, bbox_inches="tight")
print(f"Sukses! Gambar grafik berhasil disimpan ke folder dengan nama: '{nama_file}'")

plt.show()
