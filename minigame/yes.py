#Paper, scissor, rock game.
#Aprendendo a usar os onbjetos e a aleatoriedade.

paper = "paper"
scissor = "scissor"
rock = "rock"

probabilidade_de_ganhar = {paper:"rock", scissor:"paper", rock:"scissor"}
probabilidade_de_perder = {paper:"scissor", scissor:"rock", rock:"paper"}

print(probabilidade_de_ganhar[paper])