#Método herança, é quando uma classe herda outra classe, sendo reutilizável

class Humano: #classe princial, herdeiro
    def __init__(self, nome, cor, tamanho, peso):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.peso = peso

    def caractristicas(self):
        return f"A pessoa se chama {self.nome}, e tem {self.tamanho} metros e {self.peso} KG, sua cor é {self.cor}"
        #este return, retorna o valor para o Animal, por meio do super(), sendo uma ponte da informação

class Animal(Humano):  #subclasse, ou herdado
    def __init__(self,nome, cor, tamanho, peso, cachorro, gato):
        super().__init__(nome, cor, tamanho, peso)  #super chama faz a ligação da subclasse para a classe principal
        self.nome_cachorro = cachorro               #Fazendo o __init__, da classe Humano iniciar o atibuto
        self.nome_gato = gato           #e garantindo que o Animal tenha o acesso também

    def retornetudo(self):
        return f"{super().caractristicas()}, o cachorro se chama {self.nome_cachorro} e o gato se chama {self.nome_gato}"
    

name1 = input("name:")
cor1 = input("cor:")
altura1 = input("altura:")
peso1 = input("peso:")
gato1 = input("gato:")
cachorro1 = input("cachorro:")

#human = Animal("Mike Afton", "roxo", 1.79, 64.05, "Garfield", "Rex") Valores determinado
human = Animal(name1, cor1, altura1, peso1, cachorro1, gato1)
print(human.retornetudo())