#Pilhas em python ou chamadas de stacks, são estruturas que permitem
#a manipulação de elementos, que têm o princípio LIFO (Last In First Out),
#ou seja, o ultimo a entrar, vai ser o primeiro a sair
#Pense nela como uma pilha de pratos: você sempre coloca o último prato no topo e tira o prato do topo primeiro

#Ela tem várias aplicações sendo uma delas Algoritmos de Backtracking,para gerenciar os
#estados anteriores durante a exploração de problemas, como a resolução de labirintos.
#Recursão, sendo uma pilha de chamadas (call stack) mantém o controle de funções recursivas.
#Verificação de Parênteses Balanceados para verificar a correção de expressões matemáticas e código fonte.
#Conversão e Avaliação de Expressões, convertendo expressões infix para postfix e avaliam essas expressões.
#e por fim navegação em Browsers, implementando a funcionalidade de "voltar" e "avançar" nos navegadores.

class Browsers:
    def __init__(self):
        self.armazenados = [] #armazenados
        self.avançar = [] #avançar

    def visitar(self, url):
        if self.armazenados:
            print(f"saindo da url: {self.armazenados[-1]}")
        self.armazenados.append(url)  #adicionando na pilha armazenados
        self.avançar.clear()           #limpando a pilha avançar
        print(f"Entrando na url: {url}")

#Exclusão de avançar(exclui tudo nele), para colocá-lo em armazenados || Limpeza no avançar

    def voltando_ao_inicio(self):
        if len(self.armazenados) > 1: #maior que 1
            exclusão_url_armazenados = self.armazenados.pop() #removendo a url da pilha armazenados
            self.avançar.append(exclusão_url_armazenados) #adicionando na pilha avançar, o valor removido, para uso futuro
            print(f"saindo da url: {exclusão_url_armazenados}")
            print(f"Entrando na url: {self.armazenados[-1]}")
        else:
            print("não tem urls para voltar")

#Exclusão do valor armazenados, para colocá-lo em avançar || Exclui elemento de armazenados, e coloca em avançar

    def avançando(self):
        if self.avançar:
            exclusão_url_avançar = self.avançar.pop() #removendo a url da pilha avançar
            self.armazenados.append(exclusão_url_avançar) #adicionando na pilha armazenados, o valor removido, para uso futuro
            print(f"Entrando na url: {exclusão_url_avançar}")
        else:
            print("não tem urls para avançar")  

#Exclusão do valor avançar, para colocá-lo em armazenados || Exclui elemento de avançar, e coloca em armazenados

#testando

browser = Browsers()
browser.visitar("www.google.com")
browser.visitar("www.youtube.com")
browser.visitar("www.facebook.com")
browser.voltando_ao_inicio() #voltando para youtube
browser.voltando_ao_inicio() #voltando para google
browser.avançando() #volta para o youtube
browser.visitar("www.instagram.com")
browser.avançando() #não tem urls para avançar, exclusão do facebook para sempre