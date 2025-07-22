import numpy as np
import matplotlib.pyplot as plt

# === Parâmetros do problema ===
dim = 3          # 2 variáveis + bias
npoints = 100    # número de pontos
np.random.seed(0)

# === Geração de dados ===
x = np.ones((dim + 1, npoints))   # (4, npoints): [bias, x, y, classe]
x[1] = np.random.rand(npoints)    # valores de x
x[2] = np.random.rand(npoints)    # valores de y
x[3] = np.where(x[2] >= 0.5 * x[1] + 0.2, 1, -1)  # rótulos

# === Inicialização dos pesos ===
w = np.zeros(dim)  # [w0, w1, w2] → bias, peso_x, peso_y

# === Funções ===
def potencial(w, xi):
    return np.dot(w, xi[:dim])

def phi(p):
    return 1 if p >= 0 else -1

# === Treinamento do perceptron ===
for epoch in range(200):
    for i in range(npoints):
        xi = x[:, i]
        label = xi[3]
        p = potencial(w, xi)
        pred = phi(p)
        if pred != label:
            w += (label - pred) * xi[:dim]  # Atualização com taxa de aprendizado = 1

# === Visualização final ===
classe_1 = x[:, x[3] == 1]
classe_m1 = x[:, x[3] == -1]

plt.figure(figsize=(8, 6))
plt.scatter(classe_1[1], classe_1[2], color='blue', label='Classe +1')
plt.scatter(classe_m1[1], classe_m1[2], color='red', label='Classe -1')

# Reta de separação: w0 + w1*x + w2*y = 0  → y = -(w0 + w1*x)/w2
x_vals = np.linspace(0, 1, 100)
if w[2] != 0:
    y_vals = -(w[0] + w[1]*x_vals) / w[2]
    plt.plot(x_vals, y_vals, 'k--', label='Fronteira de decisão')

# Detalhes do gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.title('Perceptron de Rosenblatt (2D)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
