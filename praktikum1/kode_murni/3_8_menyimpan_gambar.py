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

plt.figure(figsize=(8, 5))
plt.hist(df["UAS"], bins=5, color="teal", edgecolor="black")
plt.title("Distribusi Nilai UAS")
plt.xlabel("Nilai UAS")
plt.ylabel("Frekuensi")
plt.savefig("histogram_uas.png", dpi=150)
plt.show()
