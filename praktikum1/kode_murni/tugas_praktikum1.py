import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_tugas = {
    "Nama": [
        "Andi", "Budi", "Citra", "Dewi", "Eko", 
        "Fajar", "Gita", "Hadi", "Indah", "Joko"
    ],
    "JK": ["L", "L", "P", "P", "L", "L", "P", "L", "P", "L"],
    "Usia": [19, 20, 18, 21, 20, 19, 20, 22, 19, 21],
    "UTS": [78, 85, 92, 60, 70, 88, 75, 82, 90, 65],
    "UAS": [80, 88, 95, 65, 72, 84, 90, 85, 92, 70],
    "Absensi": [85, 90, 95, 70, 75, 90, 85, 88, 95, 72]
}

df_tugas = pd.DataFrame(data_tugas)
print("=== 1. DATA 10 MAHASISWA ===")
print(df_tugas)

print("\n=== 2. RINGKASAN STATISTIK (describe()) ===")
print(df_tugas.describe())

print("\n=== 3. STATISTIK DESKRIPTIF KOLOM UTS & UAS ===")
for col in ["UTS", "UAS"]:
    print(f"--- Statistik {col} ---")
    print(f"Rata-rata (Mean)      : {df_tugas[col].mean():.2f}")
    print(f"Median                : {df_tugas[col].median():.2f}")
    print(f"Modus                 : {list(df_tugas[col].mode())}")
    print(f"Varians               : {df_tugas[col].var():.2f}")
    print(f"Simpangan Baku (std)  : {df_tugas[col].std():.2f}")
    print()

korelasi_absensi_uas = df_tugas["Absensi"].corr(df_tugas["UAS"])
print("=== 4. KORELASI ABSENSI DAN UAS ===")
print(f"Korelasi antara Absensi dan UAS: {korelasi_absensi_uas:.4f}")

print("\n=== 5. MEMBUAT DAN MENYIMPAN 5 VISUALISASI ===")

plt.figure(figsize=(8, 5))
plt.hist(df_tugas["UTS"], bins=5, color="seagreen", edgecolor="black")
plt.title("Histogram Nilai UTS", fontsize=14, fontweight="bold")
plt.xlabel("Nilai UTS", fontsize=11)
plt.ylabel("Frekuensi", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("tugas_1_histogram_uts.png", dpi=150, bbox_inches="tight")
plt.close()

plt.figure(figsize=(7, 5))
sns.boxplot(y=df_tugas["UAS"], color="orange")
plt.title("Boxplot Nilai UAS", fontsize=14, fontweight="bold")
plt.ylabel("Nilai UAS", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("tugas_2_boxplot_uas.png", dpi=150, bbox_inches="tight")
plt.close()

plt.figure(figsize=(7, 5))
plt.scatter(df_tugas["UTS"], df_tugas["UAS"], color="purple", s=80, alpha=0.8, edgecolors="black")
plt.title("Scatter Plot: Nilai UTS vs UAS", fontsize=14, fontweight="bold")
plt.xlabel("Nilai UTS", fontsize=11)
plt.ylabel("Nilai UAS", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("tugas_3_scatter_uts_uas.png", dpi=150, bbox_inches="tight")
plt.close()

rata_per_jk = df_tugas.groupby("JK")["UAS"].mean()
plt.figure(figsize=(6, 5))
bars = plt.bar(rata_per_jk.index, rata_per_jk.values, color=["skyblue", "salmon"], edgecolor="black")
plt.title("Rata-rata UAS Berdasarkan Jenis Kelamin", fontsize=14, fontweight="bold")
plt.xlabel("Jenis Kelamin", fontsize=11)
plt.ylabel("Rata-rata UAS", fontsize=11)
plt.ylim(0, 100)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f"{yval:.2f}", ha="center", va="bottom", fontweight="bold")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("tugas_4_barchart_uas_jk.png", dpi=150, bbox_inches="tight")
plt.close()

plt.figure(figsize=(7, 6))
numeric_cols = df_tugas[["Usia", "UTS", "UAS", "Absensi"]]
sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm", fmt=".2f", square=True, linewidths=0.5)
plt.title("Heatmap Korelasi Seluruh Kolom Numerik", fontsize=14, fontweight="bold")
plt.savefig("tugas_5_heatmap_korelasi.png", dpi=150, bbox_inches="tight")
plt.close()

print("Semua visualisasi berhasil disimpan!")
