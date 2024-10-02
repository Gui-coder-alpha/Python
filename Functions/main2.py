print("Vamos somar, multilicar e subtrair os numeros") #Mensagem principal

receba1 = int(input("Coloque o primeiro número:")) # primeiro input, colocar número, transforma string em número com int
receba2 = int(input("Coloque o segundo número:")) # segundo input, colocar número

def calcular (receba1, receba2):
    soma = receba1 + receba2
    multiplicação = receba1 * receba2
    subtrair = receba1 - receba2
    print(f"{receba1} + {receba2} = {soma}")
    print(f"{receba1} * {receba2} = {multiplicação}")
    print(f"{receba1} - {receba2} = {subtrair}")

calcular(receba1, receba2)