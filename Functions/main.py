receba = int(input("Coloque a sua idade:"))

def restrito (idade) : # idade pega o valor da variável receba, e colocando em si mesma.
    if (receba < 18 and receba > 0):
        print(f"a sua idade é de {idade}, proibido de entrar") #f faz colocar os valores da idade
    elif (receba <= 120):
        print(f"Voce tem idade o suficiente pois tens {idade} anos")
    elif (receba == 0):
        print(f"Você não nasceu, idade é igual a {idade}")
    elif (receba > 120):
        print("Você está morto")
    elif (receba > -1):
        print("??")

restrito (receba) # Chama a função3