#For loops, mesmo sendo baseado em repetir é diferente de while.
#A sua característica é pricipalmente em números de repetição
#É limitado a um número de números, sendo finito


#1 = início  11= final   2 = número de vezes
#for x in range(1, 11, 2):
  #  print(x)

#nested loops, são loops dentro de si mesmo, sendo tanto for loops com while loops.
for y in range(3):
    for y in range (1, 10):
        print(y, end="")
    print()