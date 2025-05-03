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
print("//////////////////////////////////////////////////////////")

#Selecção condicional de colunas, booleanas
dados2 = np.array([[101, 250.50, 5],
                   [102, 150.00, 10],
                   [103, 300.75, 3],
                   [104, 120.00, 8],
                   [105, 400.00, 6]])

dados_da_coluna = dados2[0: ,1] #vírgula obrigatória, se orientar igual ao plano cartesiano [linha, coluna]

valor_alto_200 = dados_da_coluna > 200

valor_para_dados2 = dados2[valor_alto_200] #Pegou somente valores altos com base na variável valor_alto_200, e aplicando para o resto da matriz como um conjunto inteiro
print(valor_para_dados2)
print("//////////////////////////////////////////////////////////")

#Reordenação de linhas(Indexação Fancy)
matriz_original = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9],
                            [10, 11, 12]])

matriz_reordenada = matriz_original[[3, 0, 1, 2]] #Reordenando as linhas da matriz original
print(matriz_reordenada)
print("//////////////////////////////////////////////////////////")

