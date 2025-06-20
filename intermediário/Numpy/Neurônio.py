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