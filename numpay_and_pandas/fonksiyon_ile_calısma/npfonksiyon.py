import numpy as np
import matplotlib.pyplot as plt


dizi=np.linspace(0,2*np.pi,100)
sin_dizi=np.sin(dizi)
cos_dizi=np.cos(dizi)

#matplotlib ile grafikleri çizdirme
plt.figure(figsize=(12,5))
plt.plot(dizi,sin_dizi,label="sin(x)",color="lightgreen")
plt.plot(dizi,cos_dizi,label="cos(x)",color="yellow")
plt.title("Sinüs ve Kosinüs Grafiği")
plt.xlabel("dizi (radyan)")
plt.ylabel("Değer")
plt.axhline(0, color='orange', linewidth=2, linestyle="--")
plt.gca().spines['top'].set_color('darkgreen')
plt.gca().spines['top'].set_linewidth(2)
plt.gca().spines['right'].set_color('darkgreen')
plt.gca().spines['right'].set_linewidth(2)
plt.gca().spines['bottom'].set_color('darkgreen')
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().spines['left'].set_color('darkgreen')
plt.gca().spines['left'].set_linewidth(2)
plt.legend()
plt.grid(alpha=0.6)
plt.show()
