


import tensorflow as tf

# Definir os nós de entrada
x = tf.constant(2.0, name='x')
y = tf.constant(3.0, name='y')
w = tf.constant(4.0, name='w')

# Operações do grafo
a = tf.add(x, y, name='add')
z = tf.multiply(a, w, name='multiply')

# Criar um writer para o TensorBoard
writer = tf.summary.create_file_writer('logs/grafo')

# Certifique-se de que o profiler esteja ativado e executado corretamente
tf.summary.trace_on(graph=True, profiler=True)

# Executar o grafo e obter o resultado
with writer.as_default():
    # Exportar o grafo para o TensorBoard antes de desativar o profiler
    tf.summary.trace_export(name="grafo", step=0)
    resultado = z.numpy()
    print("Resultado:", resultado)
