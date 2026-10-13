# ==============================================================================
# SUB-BAB 3.6: DIAGRAM LINGKARAN (PIE CHART)
# ==============================================================================
"""
[PENJELASAN RAMAH PEMULA]

1. APA MAKSUD KODE INI?
   Kita sedang memotong kue tart (lingkaran 100%) menjadi potongan-potongan pizza
   sesuai porsi persentase masing-masing kategori:
   - `autopct='%1.1f%%'` : Perintah otomatis menghitung dan menulis angka persen di setiap potongan kue.
   - Di sini kita melihat porsi mahasiswa Laki-laki vs Perempuan dalam kelas.

2. TIPS PENTING BUAT PEMULA:
   Gunakan Pie Chart HANYA kalau kategorinya sedikit (misal 2 sampai 4 kategori saja).
   Kalau kategorinya ada 10 (misal: 10 warna baju berbeda), potongan kuenya jadi tipis-tipis
   seperti jarum jam dan mata manusia akan pusing membedakannya. Untuk kasus begitu, pakai Bar Chart!

3. CONTOH DI DUNIA KERJA:
   - Manajemen Keuangan Pribadi / Perusahaan: Menampilkan porsi ke mana perginya gaji bulanan
     (misal: 50% Kebutuhan Pokok, 30% Cicilan & Tabungan, 20% Liburan/Jajan).
   - Lembaga Survei Pemilu (Quick Count): Menampilkan persentase perolehan suara pasangan calon presiden.
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

# --- Kode Sub-bab 3.6 ---
# Menghitung banyaknya mahasiswa tiap jenis kelamin
komposisi = df["JK"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    komposisi.values,
    labels=komposisi.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["skyblue", "salmon"],
    wedgeprops={"edgecolor": "black", "linewidth": 1}
)
plt.title("Komposisi Jenis Kelamin Mahasiswa", fontsize=14, fontweight="bold")
plt.show()
