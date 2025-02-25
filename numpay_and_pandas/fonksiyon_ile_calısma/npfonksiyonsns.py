import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


dizi= np.linspace(0, 2 * np.pi, 100)
sin_dizi = np.sin(dizi)
cos_dizi = np.cos(dizi)

# Veriyi bir DataFrame'e koyma
data = pd.DataFrame({"x": dizi, "Sin(x)": sin_dizi, "Cos(x)": cos_dizi})

# Seaborn çizimi
sns.lineplot(data=data, x="x", y="Sin(x)", label="Sin(x)", color="pink")
sns.lineplot(data=data, x="x", y="Cos(x)", label="Cos(x)", color="purple")

# Grafik detayları
plt.title("Sinüs ve Kosinüs Grafiği (Seaborn)")
plt.xlabel("dizi(radyan)")
plt.ylabel("Değer")

plt.axhline(0, color='darkblue', linewidth=1, linestyle="--")
plt.gca().spines['top'].set_color('blue')
plt.gca().spines['top'].set_linewidth(2)
plt.gca().spines['right'].set_color('blue')
plt.gca().spines['right'].set_linewidth(2)
plt.gca().spines['bottom'].set_color('blue')
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().spines['left'].set_color('blue')
plt.gca().spines['left'].set_linewidth(2)
plt.grid(alpha=0.6)
plt.legend()
plt.show()
