import matplotlib.pyplot as plt

bulan     = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul"]
penjualan = [12, 15, 13, 18, 20, 17, 25]

plt.figure(figsize=(8, 5))
plt.plot(bulan, penjualan, marker="o", color="blue", linewidth=2)
plt.title("Tren Penjualan per Bulan")
plt.xlabel("Bulan")
plt.ylabel("Penjualan (juta rupiah)")
plt.grid(True)
plt.show()
