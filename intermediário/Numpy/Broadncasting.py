#Broadcasting, básico
#soma de um vetor 1D para cada coluna de uma matriz 2D
import numpy as np

matriz1 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

vetor1 = np.array([10,20,30])

soma1 = matriz1 + vetor1

print(soma1)
print("//////////////////////////////////////////////////////////")

#normalização de colunas, calculando a média, o desvio padrão e dividindo ambas.
dados1 = np.array([[10, 20, 30],
                  [15, 25, 35],
                  [12, 22, 32],
                  [18, 28, 38]])

media1 = dados1.mean(axis=0) #média realizada
desvio1 = np.std(dados1, axis=0) #desvio realizado

divisao1 = (dados1 - media1) / desvio1
print(divisao1)



