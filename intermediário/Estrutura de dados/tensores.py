#tensores é nada mais do que generalização escalar, vetores e matrizes. Representando dados
#multidimensionais
#Como exemplo temos:
#Escalar de ordem 0, com único número, como temperatura
#Vetor de ordem 1, com uma linha de números, como velocidade
#Matriz de ordem 2, sendo uma tabela de números, basicamente uma matriz, com uma imagem em cinza.
#Tensor de ordem qualquer, um objeto matemático que pode ser considerado uma generalização de vetores e matrizes 
#para mais dimensões (ex: volume de dados de imagem RGB, dados temporais, etc.).
#Praticando agora

import numpy as np

tensor = np.array([[[1, 2, 3],[2, 3, 1], [5, 2, 2]],
                   [[4, 5, 2], [3, 6, 6], [1, 1, 3]],
                   [[2, 3, 2], [5, 7, 2], [1, 1, 4]]])

print(tensor)
#É um ternsor tridimensional, sendo 3x3x3, sendo 3 linhas, 3 colunas e 3 dados

#acessando 1 elemento específico
elemento = tensor[1, 1, 1] #acessa a matriz 1, na linha 1 e coluna 1
print(elemento)
elemento2 = tensor[2, 0, 2]#acessa a matriz 2, na linha 0 e coluna 2
print(elemento2)