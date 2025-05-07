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

#Cálculo a distância pairwise, manipulção de array e broadcating
vetor1 = np.array([10, 20, 30])
vetor2 = np.array([5, 15, 25, 35])

vetor1_coluna = vetor1[:,np.newaxis] #newaxis tem a função de transformar um vetor em uma coluna, ou seja vetor coluna, para vetor D1
vetor2_linha = vetor2[np.newaxis,:] #newaxis tem a função de transformar um vetor em uma linha, ou seja vetor linha, para vetor D1

diferença_absoluta = np.abs(vetor1_coluna - vetor2_linha)
print(diferença_absoluta)
print("//////////////////////////////////////////////////////////")

#Operação de álgebra Linear
matriz3 = np.array([[1, 2],
                    [3, 4]])

matriz4 = np.array([[5, 6],
                    [7, 8]])

produto_de_matriz = matriz3 @ matriz4
inversa_da_matriz3 = np.linalg.inv(matriz3) #Invertendo a matriz
inversa_da_matriz4 = np.linalg.inv(matriz4)

determinante_da_matriz3 = np.linalg.det(matriz3) #Determinante da matriz
determinante_da_matriz4 = np.linalg.det(matriz4) #Determinante da matriz
print(determinante_da_matriz3)
print(determinante_da_matriz4)
#tudo nos conformes
print("//////////////////////////////////////////////////////////")

#Simulação de passo de rede neural(foward pass simple)
entrada = np.array([1, 2, 3]) # Vetor de entrada (forma (3,)),  estes são as entradas para os pesos somado ao bias
pesos = np.array([[0.1, 0.2],
                  [0.3, 0.4],
                  [0.5, 0.6]]) # Matriz de pesos (forma (3, 2)) este aqui, é os neurônios, tal que as linhas são as entradas, e as colunas os neurônios
bias = np.array([0.5, 1.0]) # Vetor de bias (forma (2,)) bias, para cada neurônio, tal que [0] e [1] para o primeiro e segundo neurônios respectivamente

somatorio_ponderado = np.dot(entrada, pesos) #Está multiplicando as duas matrizes, entrada e os pesos, transformando em uma única matriz, que é 1x2, ou seja (,2)

saida_total = somatorio_ponderado + bias #somando o valor da soma ponderada com o bias, tal que duas tem apenas uma linha e bias
#NOTA: O bias deve ter a mesma quantidade que os neurônios, ou seja bias = quantidade de neurônios, sempre estão juntos, caso se diferem, ocorrerá erro.
print(saida_total)
#tudo nos conformes
#Melhor conteúdo aprendido até agora, com numpy
