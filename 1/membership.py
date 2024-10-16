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