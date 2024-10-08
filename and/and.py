#AND no python, deve ser usada como condição, neste caso o and deve ser true em todas as condições.
#Caso uma seja falsa, o valor da condição se dá falsa

#OR, diferente do and, também usada como condição, mas mesmo com um valor false
#Ela não vai ter valor false, mas sim true, para ser false, todas as condições dever ser false.

#Enquanto o and todas as condições devem ser true, or precisa que todas as condições
#false para ser false, uma clara diferença

x = 5
if (5 < 8 and x == 5):
    print("verdadeiro")
else: 
    print("falso")

if (x > 8 or x == 5):
    print("verdadeiro")
else: 
    print("falso")