#aprendendo a ler api, palavras em ingles buscando-as

import json
import requests

api_use = "https://api.dictionaryapi.dev/api/v2/entries"
word = "hello"

def achar(name):
    api_complete = f"{api_use}/en/{name}"
    response = requests.get(api_complete)

    if response.status_code == 200:
        trasformar_json = response.json()
        return trasformar_json
    
    else:
        print("[ERROR][ERROR][ERROR]")

encontrado = achar(word)

if encontrado:
    print(f"{encontrado[0]["word"]}")
    print(f"{encontrado[0]["phonetics"][0]["audio"]}")
    print(f"{encontrado[0]["meanings"][0]["definitions"][0]["definition"]}")
    print(f"{encontrado[0]["meanings"][1]["definitions"][0]["definition"]}")
    print(f"{encontrado[0]["meanings"][2]["definitions"][0]["definition"]}")