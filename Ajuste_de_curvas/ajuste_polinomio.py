#=== BIBLIOTECAS ===
import numpy as np #Numpy é uma biblioteca que facilita o manuseio com dados em python
import matplotlib.pyplot as plt #Matplotlib é uma biblioteca muito utilizada para plotagem de gráficos

#=== Leitura dos dados ===
dados = np.loadtxt("linha.dat") #ler informações do arquivo linha.dat

t = dados[:,0] #guardar primeira coluna (0) na variável t
y = dados[:,1] #guardar segunda coluna (1) na variável y

#=== Variáveis de controle ===
N = len(t) -1 #Definindo N como sendo o número de dados, menos 1.
GRAU = N     #Grau do polinômio a ser ajustado

#=== Construir a matriz A ===

A = np.vander(t,GRAU+1,increasing=True) #A função vander() da biblioteca numpy cria rapidamente uma matriz de Vandermonde
#a partir dos valores do vetor t, com GRAU+1 colunas e, conforme avançamos as colunas, aumentamos a potência, conforme informamos no parâmetro increasing=True


#=== Contruir a transposta de A ===

Atransp =A.T #a transposta, no python, é um atributo de qualquer vetor e pode ser acessado com .T


#=== Construir a matriz de Gram K = Atrans*A

K = np.dot(Atransp, A) #a função .dot() da biblioteca numpy faz a multiplicação matricial de duas matrizes

#=== Construir novo vetor solução Atransp*y

b = np.dot(Atransp, y)

#=== Definir nosso vetor x ===

x = np.zeros(GRAU+1) #DIferentemente da função empty(), a função zeros() do numpy cria um vetor com todas as entradas iguais a zero.

#===Função para solução de sistemas ===
def sistema(N1,a1,x1,b1):
    
    for k in range(1,1000):
        for i in range(N1):
            soma = 0
            for j in range(N1):
                if i != j :
                    soma += a1[i][j]*x1[j]
            x1[i]=(b1[i]-soma)/a1[i][i]

    return x1

#=== Resolver sistema regularizado ===

x = sistema(GRAU+1,K,x,b)

#=== Plotagem do gráfico ===
# A seguir, vamos plotar a curva do polinômio ajustado juntamente dos pontos do arquivo linha.dat
# A esta altura, já temos os coeficientes do polinômio ajustado e guardado na variável x e as coordenadas dos pontos (t,y)

# Gerar pontos para a curva do polinômio
t_plot = np.linspace(min(t), max(t), 500)  # pontos ao longo do eixo x
y_plot = np.zeros_like(t_plot)

# Avalia o polinômio ajustado: P(t) = x[0] + x[1]*t + x[2]*t^2 + ...
for i in range(GRAU+1):
    y_plot += x[i] * t_plot**i

# Plota os dados originais
plt.scatter(t, y, color='blue', label='Pontos em linha.dat')

# Plota o polinômio ajustado
plt.plot(t_plot, y_plot, color='red', label=f'Ajuste polinomial (grau {GRAU})')

# Detalhes do gráfico
plt.xlabel('t')
plt.ylabel('y')
plt.title('Ajuste polinomial')
plt.legend()
plt.grid(True)
plt.show()
