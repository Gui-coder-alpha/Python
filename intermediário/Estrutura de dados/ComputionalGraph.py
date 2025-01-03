#Computational graphs ou grafos computacionais é nada mais que uma forma
#de representar calculos matemáticos de forma mais atrativa, ou seja, algo mais
#visual e bem estruturada e simplificada.
#Um grafo computacional é formados por Nós (Nodes) e Arestas (Edges).
#Node é nada mais do que uma representações de operações matemáticas ou variáveis
#Edges é o fluxo de dados entre as operações, ou seja, o fluxo de informação
#
#Vamos pegar um exemplo para uma melhor viualização,
#temos os seguintes Nodes de entrada:x, y e z
#Onde queremos a seguinte expressão w = (x+z) * y
#Para representar esta expressão como um grafo computacional, teremos:
# a = x + z
# w = a * y
#basicamente criamos um gráfico onde temos um gráfico de entrada e um gráfico de saída
#
#Colocando em prática
import tensorflow as tf

#estes são os nós
x = tf.constant(2.0, name = 'x')
y = tf.constant(3.0, name = 'y')
w = tf.constant(4.0, name = 'w')

#realizando operações de grafos
a = tf.add(x, y, name = 'add')
z = tf.multiply(a, w, name = 'multiplicação')

#executando o grafo
resultado = z.numpy()
print(resultado)

print(tf.__version__)