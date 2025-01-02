from scipy.sparse import csr_matrix
import numpy as np

linha = [0, 1, 2, 0, 1, 2] #linha x
coluna =[0, 1, 2, 1, 0, 2] # linha y
dados = [1, 2, 3, 4, 5, 6]
matriz_esparsa = csr_matrix((dados, (linha, coluna)), shape=(3, 3)) #criando a matriz esparsa
# tal que shape=(3, 3) significa que ela tem 3 linhas e 3 colunas.

print(matriz_esparsa)

matriz_densa = matriz_esparsa.toarray() #transformando a matriz esparsa em uma matriz densa
print(matriz_densa)
print("////////")

#A lógica por trás é que o valor "dado" é uma junção das coodernadas linhas e colunas, no qual o que estiver a cima e abaixo será um valor
#pegamos um exemplo da coodernada (1,1), o que estiver em baixo do valor dele será o dado que é 2,
#Vamos simplificar ele ainda mais, é só pegar as posições do array no qual a coodernada (1,1) é representada pelos array de colocação 1 e 1, então é só pegar o valor do mesmo, que é 1, dando os seguintes valores, coluna 1 = 1, linha 1 = 1 e dado 1 = 2

#multiplicação de matrizes esparsas


linha1 =  [0, 1, 2,  0, 1, 1]
coluna1 = [0, 1, 2,  1, 0, 2]
dados1 =  [4, 8, 10, 2, 5, 1]
matriz1 = csr_matrix((dados1, (linha1, coluna1)), shape=(3, 3))
tranformer1 = matriz1.toarray()
print(tranformer1)

linha2 =  [0, 1, 2,  0, 1, 1, 0]
coluna2 = [0, 1, 2,  1, 0, 2, 2]
dados2 =  [9, 7, 6 , 2, 1, 1, 7]
matriz2 = csr_matrix((dados2, (linha2, coluna2)), shape=(3, 3))
tranformer2 = matriz2.toarray()
print(tranformer2)
print("/////")

#multiplicando agora
Multiplicação = matriz1.dot(matriz2)
print(Multiplicação)
#em matriz fica
print(Multiplicação.toarray())
#somando
somando = matriz1 + matriz2
print(somando.toarray())