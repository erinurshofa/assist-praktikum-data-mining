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

print("Rata-rata UTS :", df["UTS"].mean())
print("Median UAS    :", df["UAS"].median())
print("Modus Usia    :")
print(df["Usia"].mode())
print("Min UTS :", df["UTS"].min())
print("Max UTS :", df["UTS"].max())
