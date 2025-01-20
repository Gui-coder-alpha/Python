#Árvores de decisão é feita especialmente para machine learning, ara classificar
#e regredir

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#Vamos carregar o dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

#Dividindo o dataset em 1 conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

#Criando um classificador
clf = DecisionTreeClassifier()

#Treinando o classificador
clf.fit(X_train, y_train)

#Previsões
y_pred = clf.predict(X_test)

#A precisão calculada
precisão = accuracy_score(y_test, y_pred)
print(precisão)   