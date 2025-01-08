#criando um grafico computacional
class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
    
    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append(vertice2)
            self.grafo[vertice2].append(vertice1)

    def exibir(self):
        for vertice in self.grafo:
            print(f"{vertice}: {self.grafo[vertice]}")

acessando_grafo = Grafo()
acessando_grafo.adicionar_vertice('A')
acessando_grafo.adicionar_vertice('B')
acessando_grafo.adicionar_vertice('C')


acessando_grafo.adicionar_aresta('A', 'B')
acessando_grafo.adicionar_aresta('B', 'C')
acessando_grafo.adicionar_aresta('C', 'A')


acessando_grafo.exibir()

#Este é um grafo não-diracional, ou seja, as arestas não tem uma direção, se conectando através de 2 vértices.