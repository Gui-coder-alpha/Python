#teste com min heap

import heapq

valores = [8, 5, 3, 29, 15, 21, 10, 33]
valores2 = [8, 5, 3, 29, 15, 21, 33, 10]

heapq.heapify(valores)   #transforma em min heap, uma lista do menor para o maior, raiz = 3
heapq.heapify(valores2)

print(valores) #valores já alterados
print(valores2)


heapq.heappush(valores, 4) #adiciona o 4 na árvore, sendo filho de 3
print(valores)

remover = 29 #removendo o valor determinado, é extenso
removidoagora = valores2.index(remover)     #pegando o index do valor a ser removido
valores2[removidoagora] = valores2[-1]      #colocando o ultimo valor na posição do valor a ser removido
valores2.pop()      #removendo o ultimo valor da lista
heapq.heapify(valores2) #transformando em heap
print(valores2)

#teste com o max heap

valormax1 = [8, 5, 3, 29, 15, 21, 10, 33]

valormax1_tranformação = [-x for x in valormax1]
heapq.heapify(valormax1_tranformação)

print(valormax1_tranformação)