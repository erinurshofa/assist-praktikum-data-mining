import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Nama"   : ["Andi", "Budi", "Citra", "Dewi", "Eko", "Fajar", "Gita"],
    "JK"     : ["L", "L", "P", "P", "L", "L", "P"],
    "Usia"   : [19, 20, 18, 21, 20, 19, 20],
    "UTS"    : [78, 85, 92, 60, 70, 88, 75],
    "UAS"    : [80, 88, 95, 65, 72, 84, 90]
}
df = pd.DataFrame(data)

rata_per_jk = df.groupby("JK")["UAS"].mean()

plt.figure(figsize=(6, 5))
plt.bar(rata_per_jk.index, rata_per_jk.values, color=["skyblue", "salmon"])
plt.title("Rata-rata UAS Berdasarkan Jenis Kelamin")
plt.xlabel("Jenis Kelamin")
plt.ylabel("Rata-rata UAS")
plt.show()
