#Machine learning simples,
import numpy as np

#dados
features = np.array([1, 2, 3, 4, 5])
target = np.array([5, 6, 7.5, 8.5, 10])

#contrução da matriz de design
features_designX = features[:,np.newaxis]
target_designY = target[:,np.newaxis]
ones = np.ones((5, 1))

#fórmula (xT * x) ^-1  * xT * y)
features_designX_with_ones = np.concatenate((ones, features_designX), axis=1)

Trasnpose_of_designX_with_one = np.transpose(features_designX_with_ones)

operation_1_have_changes = Trasnpose_of_designX_with_one @ features_designX_with_ones

inversal_operation_one = np.linalg.inv(operation_1_have_changes) #parte calculada entre parenteses

operation_two_with_the_target = Trasnpose_of_designX_with_one @ target_designY # parte fora dos parenteses

Together_operation_result = inversal_operation_one @ operation_two_with_the_target

print(Together_operation_result)


#visualizar os dados resultantes com Matplotlib
import matplotlib.pyplot as plt

plt.scatter(features, target)

#fórmula da equação linear é y = mx + b
#separando a matriz together_operation_result

m = Together_operation_result[0][0] #separados, não esquecer disso importante
b = Together_operation_result[1][0]
x = np.array([1, 2, 3, 4, 5, 6])

y = m * x + b

plt.scatter(features, target)
plt.plot(x, y)
plt.show()



