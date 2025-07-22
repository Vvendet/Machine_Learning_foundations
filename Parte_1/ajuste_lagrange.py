# === BIBLIOTECAS ===
import numpy as np
import matplotlib.pyplot as plt

# === Leitura dos dados ===
dados = np.loadtxt("linha.dat")  # ler informações do arquivo linha.dat
t = dados[:, 0]  # coordenadas t (x)
y = dados[:, 1]  # coordenadas y

# === Interpolador de Lagrange ===
def lagrange_interpolador(t_pontos, y_pontos, t_val):
    soma = 0 #variável onde será guardado o somatório
    n = len(t_pontos)
    for i in range(n): #O polinômio é construído termo a termo
        Li = 1 #Variável onde será guardado os produtórios
        for j in range(n):
            if i != j:
                Li *= (t_val - t_pontos[j]) / (t_pontos[i] - t_pontos[j])
        soma += y_pontos[i] * Li
    return soma

# === Geração de pontos para a curva do polinômio ===
t_plot = np.linspace(min(t), max(t), 500)  # pontos para avaliar a curva
y_plot = np.array([lagrange_interpolador(t, y, ti) for ti in t_plot])  # avalia o polinômio

# === Plotagem do gráfico ===
plt.figure(figsize=(8, 5))
plt.plot(t_plot, y_plot, color='red', label='Ajuste polinomial')
plt.scatter(t, y, color='blue', label='Pontos em linha.dat')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Ajuste Polinomial')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()