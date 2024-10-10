print("Vamos somar, multilicar e subtrair os numeros") #Mensagem principal

x = int(input("Coloque o primeiro número:")) # primeiro input, colocar número, transforma string em número com int
y = int(input("Coloque o segundo número:")) # segundo input, colocar número

def calcular (receba1, receba2):    #esses valores são pegos abaixo 3.1
    soma = receba1 + receba2
    multiplicação = receba1 * receba2
    subtrair = receba1 - receba2
    print(f"{receba1} + {receba2} = {soma}")
    print(f"{receba1} * {receba2} = {multiplicação}")
    print(f"{receba1} - {receba2} = {subtrair}")

calcular(x, y)    #Colocar as variáveis, não altera a função acima, mas transporta os valores
                    #para cima 3.1




