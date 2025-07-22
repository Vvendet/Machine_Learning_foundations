import numpy as np
import matplotlib.pyplot as plt

# Dados extraídos do linha.dat
t = np.array([
    -1.0, -0.923076928, -0.846153855, -0.769230783, -0.692307711,
    -0.615384638, -0.538461566, -0.461538464, -0.384615391, -0.307692319,
    -0.230769232, -0.153846160, -0.0769230798, 0.0, 0.0769230798,
    0.153846160, 0.230769232, 0.307692319, 0.384615391, 0.461538464,
    0.538461566, 0.615384638, 0.692307711, 0.769230783, 0.846153855,
    0.923076928, 1.0
])
y = np.array([
    0.186205730, 0.0162617601, -0.159648612, -0.276984364, -0.292695403,
    -0.201017380, -0.0355866738, 0.0695364475, 0.169293284, 0.286522985,
    0.424286008, 0.586178899, 0.776427984, 1.0, 0.853846133,
    0.707692266, 0.561538458, 0.415384591, 0.269230783, 0.123076916,
    -0.0230770111, -0.169230819, -0.315384626, -0.461538434, -0.607692361,
    -0.753846169, -0.899999976
])
GRAU = 13
# Polinômio interpolador de grau 26
coef = np.polyfit(t, y, GRAU)  # ou deg=26

# Avaliar o polinômio em muitos pontos
t_plot = np.linspace(min(t), max(t), 500)
y_plot = np.polyval(coef, t_plot)


graus = [1,2,3,5,10, 26, 13]
for grau in graus:
    coef = np.polyfit(t, y, grau)
    y_pred = np.polyval(coef, t)
    erro = np.sum((y - y_pred)**2)
    print(f"Grau {grau:2d} -> Erro quadrático: {erro:.6e}")

# Plotar os pontos e a curva
plt.plot(t_plot, y_plot, label=f'Ajuste polinomial (grau {GRAU})', color='red')
plt.scatter(t, y, label="Pontos em linha.dat", color='blue')
plt.title("Ajuste polinomial")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
