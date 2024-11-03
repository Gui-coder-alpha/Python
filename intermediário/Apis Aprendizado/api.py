import requests
import json

response = requests.get("https://randomfox.ca/floof")

print(response.text)
print("-----------------------------------------------------")
print(response.status_code) #Apareceu 200, código bem sucedido, e está no formato JSON
print("-----------------------------------------------------")
print(response.json())#Observa-se os dados recebidos
print("-----------------------------------------------------")
#JSON (JavaScript Object Notation) é a linguagem das APIs.
#Ela codifica estruturas de dados para fácil legibilidade para a máquina.
#A APi passam dados de um lado para o outro no formato JSON.


def atual(obj):
    texto = json.dumps(obj, sort_keys = True, indent = 4)
    print(texto) #A função imprime uma string, ou 1 dicionário, depende.
    print("-----------------------------------------------------")
    return texto

valor_raposas = atual(response.json())
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
raposas = input("pressione start para receber uma imagem de uma raposa:")

if raposas == "start":
    print(valor_raposas)