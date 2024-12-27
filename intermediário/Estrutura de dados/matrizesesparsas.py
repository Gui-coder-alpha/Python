from scipy.sparse import csr_matrix

linha = [0, 1, 2, 0, 1, 2] #linha x
coluna =[0, 1, 2, 1, 0, 2] # linha y
dados = [1, 2, 3, 4, 5, 6]
matriz_esparsa = csr_matrix((dados, (linha, coluna)), shape=(3, 3)) #criando a matriz esparsa
# tal que shape=(3, 3) significa que ela tem 3 linhas e 3 colunas.

print(matriz_esparsa)

matriz_densa = matriz_esparsa.toarray() #transformando a matriz esparsa em uma matriz densa
print(matriz_densa)

#A lógica por trás é que o valor "dado" é uma junção das coodernadas linhas e colunas, no qual o que estiver a cima e abaixo será um valor
#pegamos um exemplo da coodernada (1,1), o que estiver em baixo do valor dele será o dado que é 2,
#Vamos simplificar ele ainda mais, é só pegar as posições do array no qual a coodernada (1,1) é representada pelos array de colocação 1 e 1, então é só pegar o valor do mesmo, que é 1, dando os seguintes valores, coluna 1 = 1, linha 1 = 1 e dado 1 = 2