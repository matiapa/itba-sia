import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import sklearn
from container import * 
from grapher import * 
from normalize import * 

# Open file and transform into numpy array 
xi = pd.read_csv("TP3/inputs/TP3-ej2-Conjunto-entrenamiento.txt", sep="   ").to_numpy() 
xi_original = pd.read_csv("TP3/inputs/TP3-ej2-Conjunto-entrenamiento.txt", sep="   ").to_numpy() 


zeta = pd.read_csv("TP3/inputs/TP3-ej2-Salida-deseada.txt", sep="   ").to_numpy() 


# Apply data preprocessing 
# xi, xi_min, xi_max = scaledf(xi)
xi, xi_mu, xi_sigma = standarizedf(xi)

# zeta, zeta_min, zeta_max = scaledf(zeta)
zeta, zeta_mu, zeta_sigma = standarizedf(zeta)



# Create the perceptron container 
container = Container(
    "quadratic", 
    DenseBiasLayer(1, activation="id", eta=0.01), 
)


# Train the perceptron 
epochs = 25
for epoch in range(epochs): 

    # Feed psis in random order
    array1_shuffled, array2_shuffled = sklearn.utils.shuffle(xi, zeta)

    for xi_mu, zeta_mu in zip(xi, zeta):
        res, loss = container(xi_mu, zeta_mu, True)
        print(res, loss)





