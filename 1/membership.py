#membership operators é usado para encontrar o valor de uma variável
#na sequência. usando o in ou not in
#in quando está dentro
#not in quando não está dentro

words = ("apple", "banana", "pear", "dragon fruit")

escreva = input("Coloque o nome de uma fruta in english:")

if escreva in words:
    print(f"Yes, the fruit {escreva} here.")
else:
    print(f"Don't have this fruit")


#Dica caso seja dicionário
# grades = {"garry":"a", "patrick": "b", "gui": "c"}
#Para encontrar o valor do dicionário, que seria a b ou c
#basta colocar da seguinte maneira
#grades[student]
#student = inut("your friend")