#Convertendo números, de dólar para real.

print("Calculando real para dólar ou vice-versa")
enter_a_number = float(input("Coloque o número:"))  #Valores a serem utilizados
enter_a_value = input("Para dólar digite($) & Para real digite(R$):") #Valores a serem utilizados


if enter_a_value == "R$":            #Dolar do dia 07/10/2024 para Brasil e 10/07/2024 Real=1  dolar =5,48
    end = enter_a_number * 0.18     #Dólar=1  Real=0,18
    print(f"O valor {enter_a_number}{enter_a_value} equivale a {round(end, 2)}$")
elif enter_a_value == "$":
    end = enter_a_number * 5.48
    print(f"O valor {enter_a_number}{enter_a_value} equivale a {round(end, 2)}R$")
else:
    print("Coloque um número válido")