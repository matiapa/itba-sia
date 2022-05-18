import sys
sys.path.append("..")

import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import sklearn
from container import * 
from grapher import * 
from normalize import * 

# Open file and transform into numpy array 
xi = pd.read_csv("../inputs/TP3-ej2-Conjunto-entrenamiento.txt", sep="   ").to_numpy() 
zeta = pd.read_csv("../inputs/TP3-ej2-Salida-deseada.txt", sep="   ").to_numpy()

xi, zeta = sklearn.utils.shuffle(xi, zeta)
zeta, zeta_min, zeta_max = scaledf(zeta)

# Hyperparameters 
epochs = 100
eta = 0.01

# Train and test the perceptron with different sets

avg_test_losses = []
avg_train_losses = []

for k in range(2, 11):
    print(f'Trying k={k}')
    cluster_size = int(len(zeta)/k)

    min_avg_train_loss = np.Infinity
    min_avg_test_loss = np.Infinity

    for kid in range(k):
        print(f'Trying kid={kid}')

        container = Container(
            "quadratic", 
            DenseBiasLayer(1, activation="sigmoid", eta=eta), 
        )

        # Train the perceptron

        zeta_test = zeta[kid*cluster_size : (kid+1)*cluster_size]
        zeta_train = np.concatenate((zeta[(-k+kid+1)*cluster_size:], zeta[:kid*cluster_size]))

        xi_test = xi[kid*cluster_size : (kid+1)*cluster_size]
        xi_train = np.concatenate((xi[(-k+kid+1)*cluster_size:], xi[:kid*cluster_size]))

        train_losses = []
        for epoch in range(epochs):
            # Feed xis in random order
            xi_train, zeta_train = sklearn.utils.shuffle(xi_train, zeta_train)

            global_loss = 0
            for xi_mu, zeta_mu in zip(xi_train, zeta_train):
                res, loss = container(xi_mu, zeta_mu, True)
                global_loss += loss * ( (zeta_max[0]-zeta_min[0])**2)
            train_losses.append(global_loss/len(xi_train))
        
        # Test the perceptron with train set

        train_loss = 0
        for xi_mu, zeta_mu in zip(xi_test, zeta_test):
            res, loss = container(xi_mu, zeta_mu, False)
            train_loss += loss * ( (zeta_max[0]-zeta_min[0])**2)
        min_avg_train_loss = min(min_avg_train_loss, train_loss/len(xi_train))

        # Test the perceptron with test set

        test_loss = 0
        for xi_mu, zeta_mu in zip(xi_test, zeta_test):
            res, loss = container(xi_mu, zeta_mu, False)
            test_loss += loss * ( (zeta_max[0]-zeta_min[0])**2)
        min_avg_test_loss = min(min_avg_test_loss, test_loss/len(xi_test))
    
    avg_train_losses.append(min_avg_train_loss)
    avg_test_losses.append(min_avg_test_loss)

plt.xlabel('Number of folds (k)')
plt.ylabel('Best average test error')
plt.scatter(range(2, 11), avg_test_losses, label='Test')
plt.scatter(range(2, 11), avg_train_losses, label='Train')

plt.legend()
plt.show()