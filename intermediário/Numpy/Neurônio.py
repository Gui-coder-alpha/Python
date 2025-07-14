import numpy as np
import matplotlib.pyplot as plt

#Criando o gradiente
features = np.array([1.6, 2.3, 7.8, 1.2, 5.9, 9.0, 1.2, 5.7, 8.9, 9.1])
target = np.array([0, 0, 1, 1, 1, 0, 0, 1, 0, 1])

features_designX = features[:,np.newaxis]
target_designY = target[:,np.newaxis]
matrix_of_ones = np.ones((10,1))
concatenationX = np.concatenate((features_designX, matrix_of_ones), axis=1)
beta_value = np.zeros((2,1))

sum_ponderada_Z = concatenationX @ beta_value

def function_sigmoid(sum_ponderada_Z):  
    sigmoid = 1/(1 + np.exp(-sum_ponderada_Z))
    return sigmoid

sigmoid_result = function_sigmoid(sum_ponderada_Z)

#Função BCE Binary Cross-Entropy, função de custo basicamente
learning_rate = 0.01
iterations = 1

#Fórmula é
class Optmization(): 
    def __init__(self, features_designY, sigmoid_result, concatenationX, learning_rate, iterations, beta_value, sum_ponderada_Z):
        self.epsilon = 1e-10 #Importante para não dar -inf, Negative Infinite Value
        self.features_designY = features_designY
        self.sigmoid_result = sigmoid_result
        self.concatenationX = concatenationX
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.beta_value = beta_value
        self.cost = []
        self.sum_ponderada_Z = sum_ponderada_Z

    def function_sigmoid(self, sum_ponderada_Z):  
        sigmoid = 1/(1 + np.exp(-sum_ponderada_Z))
        return sigmoid


    def Binary_cost_function(self):
        #first step
        Y_multipy_log_sigmoid = self.features_designY * np.log(self.sigmoid_result + self.epsilon)
        #second step
        one_minus_Y = 1 - self.features_designY
        #third step
        log_one_minus_sigmoid = np.log(1 - self.sigmoid_result + self.epsilon)
        #fourth step
        cost_function = -(Y_multipy_log_sigmoid + one_minus_Y * log_one_minus_sigmoid)
        mean_of_values = np.mean(cost_function)
        return mean_of_values
    
    def Gradient_descent(self):
        concatenationX_transpose = self.concatenationX.transpose()
        weight_gradient = (1/len(self.features_designY)) * concatenationX_transpose @ (self.sigmoid_result - self.features_designY)
        bias_gradient = (1/len(self.features_designY)) * np.sum((self.sigmoid_result - self.features_designY))
        return weight_gradient, bias_gradient
    
    def trainement(self,learning_rate,iterations):
        for i in range(iterations):
            sum_ponderada_Z_next = self.concatenationX @ self.beta_value
            sigmoid_result_new = self.function_sigmoid(sum_ponderada_Z_next)
            calculus_of_cost = self.Binary_cost_function(sigmoid_result_new)
            calculus_of_gradient = self.Gradient_descent(sigmoid_result_new)
            new_parameters = self.beta_value - learning_rate * calculus_of_gradient
            self.cost.append(neqw_parameters)
        if i % (iterations // 10) == 0:
            print(f"Iteração {i}: Custo = {self.cost:.6f}")
            return self.beta_value, self.cost_history

datas = Optmization(target_designY, sigmoid_result, concatenationX, learning_rate, iterations, beta_value, sum_ponderada_Z)
print(datas.Binary_cost_function())

