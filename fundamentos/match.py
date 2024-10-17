#list comressions, é uma lista compacta criada em uma varíavel
#Sua fómula é
#[expression for value in iterable if condition]
#     x = 2  for   x   in range(1, 11)
#[expression for value in iterable if condition]
#     x = 2  for   x   in range(1, 11) if x < 20
#melhor para números do que para strings
#No caso das strings se trasnformam basicamente em letras
#maiusculas ou minusculas

doubles = [x + 2 for x in range(1, 11)]
print(doubles)