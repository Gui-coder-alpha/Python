#Criando um Servidor com Python, simples

from http.server import SimpleHTTPRequestHandler, HTTPServer
#o http.server está importando as funções HTTPServer e SimpleHTTPRequestHandler

#HTTPServer cria um servidor, recebendo solicitações de um endereço específico
#e porta específica, e o SimpleHTTPRequestHandler cria uma resposta para essas solicitações


hostName = "localhost"
serverPort = 8080  #Número para o servidor, para testes em específico

with HTTPServer((hostName, serverPort), SimpleHTTPRequestHandler) as server:
    #Cria o servidor, passando o endereço e a porta, além de manipular as requisições

    print(f"Server started http://%s:%s" "% (hostName, serverPort)")    #Confirmar o servidor se está funcionando
                                                                        #corretamente

    server.serve_forever() #entra em loop infinito escutando as requisições HTTP
