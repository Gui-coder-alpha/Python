#Machine learning com gradiente descendente,
import numpy as np
import matplotlib.pyplot as plt

#dados
features = np.array([1, 2, 3, 4, 5])
target = np.array([5, 6, 7.5, 8.5, 10])

#contrução da matriz de design
features_designX = features[:,np.newaxis]
target_designY = target[:,np.newaxis]
x = features_designX
y = target_designY
matrix_of_ones = np.ones((5, 1))
concatenationx = np.concatenate((x, matrix_of_ones), axis=1)

#parâmetros zerados
zero_parameters = np.zeros((2,1)) #valor beta

#hiperparametros do gradiente descendente
learning_rate = 0.01
iterations = 100

#função de custo
def cost_function(concatenationx, zero_parameters, y):
    #parte 1/ calcular os valores
    y_with_hat = concatenationx @ zero_parameters #valor da matriz de x multiplciado pela matriz beta
    #parte 2/calcular os erros
    y_no_hats = y - y_with_hat
    #parte3/ calcular os erros e elevar ao quadrado
    y_no_hats_squared = y_no_hats ** 2
#parte 4/ calcular a média dos erros
    y_no_hats_squared_mean = np.mean(y_no_hats_squared)
    return y_no_hats_squared_mean

custo_inicial = cost_function(concatenationx, zero_parameters, y)
print(f"Custo inicial: {custo_inicial}")

def gradient_calculus(concatenationx, zero_parameters,y):
    y_with_hat_2 = concatenationx @ zero_parameters
    y_no_hats_2 = y - y_with_hat_2
    n = concatenationx.shape[0] #quantidade de linhas é 5
    concatenationx_features = concatenationx[:,0].reshape(-1,1) #Parte difícil, basicamente pega o valor da primeira coluna, e transforma em um array 1d, para depois transformar em uma matriz 5 x 1.
    grad_m = -2/n * np.sum(concatenationx_features * y_no_hats_2)
    grad_b = -2/n * np.sum(y_no_hats_2)
    real_gradients = np.array([[grad_m], [grad_b]])
    return real_gradients

gradient_value = gradient_calculus(concatenationx, zero_parameters, y)    

#criando um loop
cost = []
for i in range(iterations):
    variable_of_errors = cost_function(concatenationx, zero_parameters, y)
    current_cost = variable_of_errors #beta_gf = zero_parameters
    cost.append(current_cost)

    call_the_gradient = gradient_calculus(concatenationx, zero_parameters, y)
    new_zero_parameters = zero_parameters - learning_rate * call_the_gradient
    if i % 100 == 0:
        print(f"Iteration {i}: {current_cost}")
    zero_parameters = new_zero_parameters


print("\nTreinamento concluído!")
print(f"Custo final: {cost[-1]:.4f}") # O ultimo custo da lista
print(f"Parâmetros finais (m e b, respectivamente):\n{zero_parameters}")

#criando um gráfico
fig, axes = plt.subplots(1,2, figsize=(12,5), layout='constrained')
axes[0].plot(cost)
axes[0].set_title("Custo") #Título
axes[0].set_xlabel("Iterações") #label X
axes[0].set_ylabel("Custo MSE") #label Y
axes[0].grid(True)

axes[1].scatter(features, target, label='Dados Originais', color='blue', alpha=0.7) # Grafico de dispersao dos dados originais


y_predicted_line = concatenationx @ zero_parameters

axes[1].plot(features, y_predicted_line, color='red', label='Linha de Regressão GD', linewidth=2) # Plotar a linha
axes[1].set_title('Regressão Linear com Gradiente Descendente') # Titulo
axes[1].set_xlabel('Horas de Estudo') # Label X
axes[1].set_ylabel('Nota na Prova') # Label Y
axes[1].legend() # Mostrar legenda
axes[1].grid(True) # Adicionar grade
plt.show()