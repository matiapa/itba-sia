import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import sklearn
from container import * 
from grapher import * 


# Function for standardization 
def standarizedf(dataframe): 
    x = dataframe.transpose()
    for t in range(len(x)):  
        x[t] = (x[t] - np.mean(x[t]))/np.std(x[t])
    return x.transpose()

# Function for normalization  
def normalizedf(dataframe): 
    x = dataframe.transpose()
    for t in range(len(x)):  
        x[t] = (x[t] - np.min(x[t]))/(np.max(x[t]) - np.min(x[t]))
    return x.transpose()

# Open file and transform into numpy array 
xi = pd.read_csv("TP3/inputs/TP3-ej2-Conjunto-entrenamiento.txt", sep="   ").to_numpy() 
zeta = pd.read_csv("TP3/inputs/TP3-ej2-Salida-deseada.txt", sep="   ").to_numpy() 

# xi = standarizedf(xi)
zeta = normalizedf(zeta)

# Create the perceptron container 
container = Container(
    "quadratic", 
    DenseBiasLayer(1, activation="sigmoid"), 
)

# Train the perceptron 
epochs = 100
errors = [] 
for epoch in range(epochs): 

    # Feed psis in random order
    array1_shuffled, array2_shuffled = sklearn.utils.shuffle(xi, zeta)

    error = 0
    for psi_mu, zeta_mu in zip(xi, zeta):
        res, loss = container(psi_mu, zeta_mu, True)
        error += loss # Accumulates the error of an epoch 

    errors.append(error/len(xi))
    print("EPOCH", epoch)
    print("Mean error in epoch:", error/len(xi))
    print("Weights:", container.layers[0].w)
    print("--------------------") 

# graph_bound_perceptron(container, xi, zeta, 420)
# plt.plot(range(len(errors)), errors, 'k-')
# plt.show()


# for (x,y,z) in zip(x,y,z):
#     print(z)
#     plt.plot(x, y, 'k.', alpha=z, markersize=0.25)
# plt.show()