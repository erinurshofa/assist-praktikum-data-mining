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

plt.figure(figsize=(7, 5))
plt.scatter(df["UTS"], df["UAS"], color="purple")
plt.title("Hubungan Nilai UTS dan UAS")
plt.xlabel("Nilai UTS")
plt.ylabel("Nilai UAS")
plt.show()
