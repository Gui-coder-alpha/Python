#Paper, scissor, rock game.
#Aprendendo a usar os onbjetos e a aleatoriedade.

import random

game = ("papel", "tesoura", "pedra")

print("Jogo da velha")
print("Caso queira sair digite quit")
print("-------------")

game_you = input("Digite papel, tesoura ou pedra:")
game_bot = random.choice(game) #choice, pega valores de arrays, ou seja o objeto inserido no array
game_arm = game_you

while game_arm and game_bot:
    if game_arm == "papel" and game_bot == "pedra":
        print(game_bot)
        print("you won")
        break
    elif game_arm == "pedra" and game_bot == "tesoura":
        print(game_bot)
        print("you won")
        break
    elif game_arm == "tesoura" and game_bot == "papel":
        print(game_bot)
        print("you won")
    elif game_arm == game_bot:
        print(game_bot)
        print("Empate")
        break
    else:
        print(game_bot)
        print("you lose")
        break