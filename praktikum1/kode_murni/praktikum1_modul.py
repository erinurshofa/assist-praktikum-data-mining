import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Nama"   : ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"],
    "JK"     : ["L", "L", "P", "P", "L", "L", "P"],
    "Usia"   : [19, 20, 18, 21, 20, 19, 20],
    "UTS"    : [78, 85, 92, 60, 70, 88, 75],
    "UAS"    : [80, 88, 95, 65, 72, 84, 90]
}

df = pd.DataFrame(data)
print(df)

print(df.head(3))
print(df.info())
print(df.describe())

print("Rata-rata UTS :", df["UTS"].mean())
print("Median UAS    :", df["UAS"].median())
print("Modus Usia    :")
print(df["Usia"].mode())
print("Min UTS :", df["UTS"].min())
print("Max UTS :", df["UTS"].max())

rentang = df["UTS"].max() - df["UTS"].min()
print("Rentang UTS :", rentang)
print("Varians UTS :", df["UTS"].var())
print("Simpangan baku UTS :", df["UTS"].std())
print("Kuartil UTS:")
print(df["UTS"].quantile([0.25, 0.50, 0.75]))

print(df[["Usia", "UTS", "UAS"]].corr())

print(df[["Nama", "UTS"]])
mahasiswa_lulus = df[df["UTS"] >= 75]
print("Mahasiswa dengan UTS >= 75:")
print(mahasiswa_lulus)
print("Rata-rata UAS per jenis kelamin:")
print(df.groupby("JK")["UAS"].mean())

print("Rata-rata usia seluruh mahasiswa:", df["Usia"].mean())
print("Mahasiswa dengan UTS tertinggi:", df.loc[df["UTS"].idxmax(), "Nama"])
print("Simpangan baku UAS:", df["UAS"].std())
print("Korelasi UTS dan UAS:", df["UTS"].corr(df["UAS"]))
print("Rata-rata UAS per jenis kelamin:")
print(df.groupby("JK")["UAS"].mean())

bulan     = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul"]
penjualan = [12, 15, 13, 18, 20, 17, 25]
plt.figure(figsize=(8, 5))
plt.plot(bulan, penjualan, marker="o", color="blue", linewidth=2)
plt.title("Tren Penjualan per Bulan")
plt.xlabel("Bulan")
plt.ylabel("Penjualan (juta rupiah)")
plt.grid(True)
plt.show()

rata_per_jk = df.groupby("JK")["UAS"].mean()
plt.figure(figsize=(6, 5))
plt.bar(rata_per_jk.index, rata_per_jk.values, color=["skyblue", "salmon"])
plt.title("Rata-rata UAS Berdasarkan Jenis Kelamin")
plt.xlabel("Jenis Kelamin")
plt.ylabel("Rata-rata UAS")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["UTS"], bins=5, color="green", edgecolor="black")
plt.title("Distribusi Nilai UTS")
plt.xlabel("Nilai UTS")
plt.ylabel("Frekuensi")
plt.show()

plt.figure(figsize=(7, 5))
plt.scatter(df["UTS"], df["UAS"], color="purple")
plt.title("Hubungan Nilai UTS dan UAS")
plt.xlabel("Nilai UTS")
plt.ylabel("Nilai UAS")
plt.show()

plt.figure(figsize=(7, 5))
sns.boxplot(y=df["UAS"], color="orange")
plt.title("Boxplot Nilai UAS")
plt.ylabel("Nilai UAS")
plt.show()

komposisi = df["JK"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(komposisi.values, labels=komposisi.index, autopct="%1.1f%%",
        startangle=90, colors=["skyblue", "salmon"])
plt.title("Komposisi Jenis Kelamin Mahasiswa")
plt.show()

plt.figure(figsize=(6, 5))
sns.heatmap(df[["Usia", "UTS", "UAS"]].corr(), annot=True,
            cmap="coolwarm", fmt=".2f", square=True)
plt.title("Heatmap Korelasi Antar Variabel")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["UAS"], bins=5, color="teal", edgecolor="black")
plt.title("Distribusi Nilai UAS")
plt.xlabel("Nilai UAS")
plt.ylabel("Frekuensi")
plt.savefig("histogram_uas.png", dpi=150)
plt.show()
