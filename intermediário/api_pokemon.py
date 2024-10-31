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

pokemon = "clefairy"

nome = poke_achou(pokemon)

if nome:
    print(f"{nome["name"]}")
    print(f"{nome["height"]}")
    print(f"{nome["id"]}")
    print(f"{nome["types"]}")
    tipo_pokemon = [tipo["type"]["name"] for tipo in nome["types"]] #Tipo está pegando informação do dicionário type
    print(tipo_pokemon)                                             #no qual está pegando informação do dicionário
    print("---------------------------------------")                #name, encontrando o tipo do pokemon.
    
    ability_poke = [abilidade["ability"]["name"] for abilidade in nome["abilities"]] #seleciona todas as informações
    print(ability_poke)
    habilidade_1 = nome["abilities"][0]["ability"]["name"]  #seleciona apenas 1 informação
    print(habilidade_1)
    base_stat = nome["stats"][0]["base_stat"]
    print(base_stat)
    all_stats = [estatus["base_stat"] for estatus in nome["stats"]]
    print(all_stats)