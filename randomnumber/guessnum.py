#Encontre o número
    #print(f"Yes, correct number {random_number}")

import random

low_number = 1
high_number = 100

random_number = random.randint(low_number, high_number)

print("---------------------")
print("Guess the number!")
print("---------------------")


number_input = int(input("Press the number:"))
print("---------------------")


while number_input != random_number:
    if number_input < random_number:
        print(f"O número {number_input} está abaixo do valor")
        print("---------------------")
        number_input = int(input("Press the number:"))
        print("---------------------")
    elif number_input > random_number:
        print(f"O número {number_input} está acima do valor")
        print("---------------------")
        number_input = int(input("Press the number:"))
        print("--------------------")
    

    while number_input == random_number:
        print("-------Correct-------")
        print("---------------------")
        print(f"The correct number is {random_number}")
        print("---------------------")
        break