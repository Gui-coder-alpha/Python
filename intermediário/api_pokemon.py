#API sobre pokemon, aprendizado

import json
import requests

poke_api = "https://pokeapi.co/api/v2/"

def poke_achou(name):
    poke_yep = f'{poke_api}/pokemon/{name}'
    response = requests.get(poke_yep)

    if response.status_code == 200:
        pokemon_status = response.json()
        return pokemon_status

pokemon = "mewtwo"

nome = poke_achou(pokemon)

if nome:
    print(f"{nome["name"]}")
    print(f"{nome["height"]}")
    print(f"{nome["id"]}")
    print(f"{nome["types"]}")
    tipo_pokemon = [tipo["type"]["name"] for tipo in nome["types"]]
    print(tipo_pokemon)

