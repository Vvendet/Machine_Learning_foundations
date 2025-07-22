# === Bibliotecas ===
import numpy as np
import matplotlib.pyplot as plt

# === Leitura dos dados ===
#Precisamos selecionar apenas os pontos tais que a coordenada x é maior ou igual a zero
dados = np.loadtxt("pontos.dat")  # ler informações do arquivo pontos.dat
filtro = dados[:, 0] >= 0  # Criamos um vetor booleano para filtrar os valores em que x>=0
x_linha = dados[filtro,0] #seleciona valores da coluna 0 (x) filtrados
y = dados[filtro,1] #seleciona valores da coluna 1 (y) filtrados
 
# === Configurações iniciais ===
dim = 3  # 2 variáveis + bias
npoints = len(y) #numero de pontos

# === Gerar dados ===
x = np.ones((dim + 1, npoints))  # criar uma matriz toda preenchida com 1. A primeira linha se refere ao bias.
x[1] = x_linha #preencher a segunda linha com as coordenadas x dos pontos
x[2] = y #preencher a terceira linha com as coordeandas y dos pontos


# === Classificação dos pontos: 1 ou -1 ===
x[3] = dados[filtro, 2] #seleciona elementos da coluna 2 de pontos.dat em que a coordenada x >=0

for i in range(len(x[3])): #trocar categoria 2 por -1
    if x[3][i] == 2:
        x[3][i]= -1

# === Inicializacao dos pesos ===
w = np.zeros(dim)
w[0] = 0.5 #bias    

# === Função potencial ===
def potencial(w, x):
    return np.dot(w, x[:dim])  # não usa a categoria (última linha)

# === Função de ativação degrau ===
def phi(val):
    return 1 if val >= 0 else -1

# === Treinamento ===
for k in range(1, 2001):  # 2000 épocas
    for i in range(npoints):
        pt = x[:, i]
        cat = pt[3]
        pot = potencial(w, pt)
        pred = phi(pot)
        if pred != cat: #se a previsão estiver errada
            if pred > cat:
                w -= pt[:dim]  # classificado como 1 mas era -1
            else:
                w += pt[:dim]  # classificado como -1 mas era 1


# === VISUALIZAÇÃO FINAL ===
# Separar os pontos por classe
classe_1 = x[:, x[3] == 1]
classe_m1 = x[:, x[3] == -1]

# Plotagem dos pontos
plt.figure(figsize=(8, 6))
plt.scatter(classe_1[1], classe_1[2], color='blue', label='Classe +1')
plt.scatter(classe_m1[1], classe_m1[2], color='red', label='Classe -1')

# Traçar a reta de separação final: w0 + w1*x + w2*y = 0 → y = -(w0 + w1*x)/w2
x_vals = np.linspace(0, 1, 100)
if w[2] != 0:
    y_vals = -(w[0] + w[1]*x_vals) / w[2]
    plt.plot(x_vals, y_vals, 'k--', label='Fronteira de decisão')

print("y = {a}x+({b})".format(a=(y_vals[2]-y_vals[1])/(x_vals[2]-x_vals[1]),b=y[0]))

# Detalhes do gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.title('Perceptron de Rosenblatt (2D)')
plt.legend()
plt.grid(True)
plt.show()