#while, repetição, basicamente isto. Simples e direto ao ponto.
#Tomar cuidado, pode ocasionar em repetições infinitas.
#Pode ser uma alternativa quanta a função, mas não substitui.
#Um pouco mais complexa ao meu ver.

name = input("Coloque seu nome:")

while name == "" :                          #Simples e direto.
    print(f"Seu {name} está vazio")         #Caso não coloque nada
    name = input("Coloque seu nome:")       #Retorna o name input para digitar

print(name)