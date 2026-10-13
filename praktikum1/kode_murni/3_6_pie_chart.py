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

komposisi = df["JK"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(komposisi.values, labels=komposisi.index, autopct="%1.1f%%",
        startangle=90, colors=["skyblue", "salmon"])
plt.title("Komposisi Jenis Kelamin Mahasiswa")
plt.show()
