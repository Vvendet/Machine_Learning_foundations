#=== Bibliotecas ===
import numpy as np
import matplotlib.pyplot as plt

#=== Método Gauss-Seidel ===
def gauss_seidel(A, b):
    n = len(b)    
    x = np.zeros(n) 

    for k in range(1,1000):
        for i in range(n):
            soma = 0
            for j in range(n):
                if i != j :
                    soma += A[i][j]*x[j]
            x[i]=(b[i]-soma)/A[i][i]

    return x

#=== Construção e resolução do sistema da spline ===
def spline_sistema(v):  # v pode ser t ou y
    n = len(v) #ler numero de pontos
    A = np.zeros((n, n)) #preencher a matriz dos coeficientes, inicialmente, com zeros
    b = np.zeros(n) #preencher a matriz solucao, inicialmente, com zeros

    #Primeira equacao de contorno natural:
    A[0, 0] = 2
    A[0, 1] = 1
    b[0] = 3 * (v[1] - v[0])

    #Equacoes de continuidade da derivada segunda:
    for i in range(1, n - 1):
        A[i, i - 1] = 1
        A[i, i] = 4
        A[i, i + 1] = 1
        b[i] = 3 * (v[i + 1] - v[i - 1])

    #Segunda condição de contorno natural:
    A[-1, -2] = 1
    A[-1, -1] = 2
    b[-1] = 3 * (v[-1] - v[-2])

    #Retornar solucao do sistema:
    return gauss_seidel(A, b)

#=== Calcular os coeficientes ===
def construir_splines(v, D):
    splines = [] #array para guardar todos os coeficientes

    for i in range(len(v) - 1): #laço para calcular os coeficientes
        #valores conhecidos
        vi, vi1 = v[i], v[i+1]
        Di, Di1 = D[i], D[i+1]
        #avaliando os coeficientes a partir das relações encontradas
        b = 3 * (vi1 - vi) - 2 * Di - Di1
        a = (Di1 - Di - 2 * b)/3
        c = Di
        d = vi
        #adicionando os coeficientes ao array
        splines.append((a, b, c, d))
    #retorna o array com os coeficientes:
    return splines

#=== Calcular o valor dos polinômios encontrados ===
def avaliar_spline(splines, s_values):
    result = []#Array para guardar o valor do polinomio para cada i
    for (a, b, c, d) in splines: #calcular os valores iterando em cada i
        r = a * s_values**3 + b * s_values**2 + c * s_values + d
        result.append(r) #adicionando resultado a result
    #retorna o array dos resultados:
    return np.array(result)

# ==== USO COM OS DADOS ====
dados = np.loadtxt("linha.dat")
t = dados[:, 0]
y = dados[:, 1]
n = len(t)

#=== Derivadas de t(s) e y(s) ===
Dt = spline_sistema(t)
Dy = spline_sistema(y)

#=== Construir os coeficientes das splines ===
splines_t = construir_splines(t, Dt)
splines_y = construir_splines(y, Dy)

#=== Avaliação para cada trecho ===
s_plot = np.linspace(0, 1, 100) #criar 100 pontos igualmente espaçados dentro do intervalo [0,1]
T_plot = []
Y_plot = []

for i in range(n - 1):
    T_piece = avaliar_spline([splines_t[i]], s_plot) #avaliar Ti no intervalo
    Y_piece = avaliar_spline([splines_y[i]], s_plot) #avaliar Yi no intervalo
    T_plot.extend(T_piece[0]) #guardar os valores de Ti
    Y_plot.extend(Y_piece[0]) #guardar os valores de Yi

# Plotar curva paramétrica
plt.figure(figsize=(10, 5))
plt.plot(T_plot, Y_plot, 'r-', label='Spline cúbica')
plt.plot(t, y, 'bo', label='Pontos de linha.dat')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Spline Cúbica Natural Paramétrica')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()