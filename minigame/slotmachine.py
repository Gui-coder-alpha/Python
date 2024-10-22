#slotmachine test
import random

caracteres_min = 1
caracteres_max = 5
ganhar = [(1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5)]

comece = input("press start(start):")

combination_1 = random.randint(caracteres_min, caracteres_max)
combination_2 = random.randint(caracteres_min, caracteres_max)
combination_3 = random.randint(caracteres_min, caracteres_max)
rede_of_combination = int(combination_1), int(combination_2), int(combination_3)

comece_comece = "start"

while comece == comece_comece:
    if rede_of_combination in ganhar :
        print(rede_of_combination)
        print("---------------------------")
        print("ganhou")
        print("---------------------------")
        comece = input("press start para começar novamente(start):")
        print("---------------------------")
        combination_1 = random.randint(caracteres_min, caracteres_max)
        combination_2 = random.randint(caracteres_min, caracteres_max)
        combination_3 = random.randint(caracteres_min, caracteres_max)
        rede_of_combination = int(combination_1), int(combination_2), int(combination_3)
    else:
        print(rede_of_combination)
        print("---------------------------")
        print("perdeu")
        print("---------------------------")
        comece = input("press start(start):")
        combination_1 = random.randint(caracteres_min, caracteres_max)
        combination_2 = random.randint(caracteres_min, caracteres_max)
        combination_3 = random.randint(caracteres_min, caracteres_max)
        rede_of_combination = int(combination_1), int(combination_2), int(combination_3)







