import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import sklearn
from sympy import xfield
from container import * 
from grapher import * 
from normalize import * 

# Open file and transform into numpy array 
xi = pd.read_csv("TP3/inputs/TP3-ej2-Conjunto-entrenamiento.txt", sep="   ").to_numpy() 
zeta = pd.read_csv("TP3/inputs/TP3-ej2-Salida-deseada.txt", sep="   ").to_numpy()

xi, zeta = sklearn.utils.shuffle(xi, zeta)
zeta, zeta_min, zeta_max = scaledf(zeta)

# # Clustering
k = 2
kid = 1 
cluster_size = int(len(zeta)/k)   
zeta_test = zeta[kid*cluster_size:(kid+1)*cluster_size]
zeta_train = np.concatenate((zeta[(-k+kid+1)*cluster_size:], zeta[:kid*cluster_size]))

xi_test = xi[kid*cluster_size:(kid+1)*cluster_size]
xi_train = np.concatenate((xi[(-k+kid+1)*cluster_size:], xi[:kid*cluster_size]))

# Hyperparameters 
epochs = 1000
sample = len(xi_train)
eta = 0.01

# Plot parameters 
fig = plt.figure()
fig.text(0.9, 0.02, "Eta = "+str(eta), ha='center')
plt.ylabel("Average global error")
plt.xlabel("Epochs (all dataset)")
plt.locator_params(axis="x", integer=True, tight=True)


# Create the perceptron container 
container = Container(
    "quadratic", 
    DenseBiasLayer(1, activation="sigmoid", eta=eta), 
)


# Train the perceptron 
global_losses = [] 
for epoch in range(epochs): 

    # Feed xis in random order
    xi_train, zeta_train = sklearn.utils.shuffle(xi, zeta)

    global_loss = 0
    for xi_mu, zeta_mu in zip(xi_train[:sample], zeta_train[:sample]):
        res, loss = container(xi_mu, zeta_mu, True)
        global_loss += loss * ( (zeta_max[0]-zeta_min[0])**2)
    global_losses.append(global_loss/len(xi_train))

print(global_loss/len(xi_train))

# Test the perceptron 
train_loss = 0
for xi_mu, zeta_mu in zip(xi_test, zeta_test):
    res, loss = container(xi_mu, zeta_mu, False)
    train_loss += loss * ( (zeta_max[0]-zeta_min[0])**2)

print(train_loss/len(xi_test))
