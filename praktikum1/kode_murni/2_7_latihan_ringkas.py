import pandas as pd
import numpy as np

data = {
    "Nama"   : ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"],
    "JK"     : ["L", "L", "P", "P", "L", "L", "P"],
    "Usia"   : [19, 20, 18, 21, 20, 19, 20],
    "UTS"    : [78, 85, 92, 60, 70, 88, 75],
    "UAS"    : [80, 88, 95, 65, 72, 84, 90]
}
df = pd.DataFrame(data)

print("1. Rata-rata usia seluruh mahasiswa:", df["Usia"].mean())
print("2. Mahasiswa dengan UTS tertinggi:", df.loc[df["UTS"].idxmax(), "Nama"])
print("3. Simpangan baku nilai UAS:", df["UAS"].std())
print("4. Korelasi UTS dan UAS:", df["UTS"].corr(df["UAS"]))
print("5. Rata-rata UAS per jenis kelamin:")
print(df.groupby("JK")["UAS"].mean())
