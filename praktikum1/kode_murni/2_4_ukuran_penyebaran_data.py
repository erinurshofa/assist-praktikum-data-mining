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

rentang = df["UTS"].max() - df["UTS"].min()
print("Rentang UTS        :", rentang)
print("Varians UTS        :", df["UTS"].var())
print("Simpangan baku UTS :", df["UTS"].std())
print("Kuartil UTS:")
print(df["UTS"].quantile([0.25, 0.50, 0.75]))
