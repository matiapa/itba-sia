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

fig = plt.figure()
eta = 0.001
fig.text(0.9, 0.02, "Eta = "+str(eta), ha='center')
plt.ylabel("Average global error")
plt.xlabel("Epochs (all dataset)")

plt.locator_params(axis="x", integer=True, tight=True)

epochs = 50
sample = 200



#######################
# NONE + NONE #########
#######################

# # Create the perceptron container 
# container = Container(
#     "quadratic", 
#     DenseBiasLayer(1, activation="id", eta=eta), 
# )


# # Train the perceptron 
# global_losses = [] 
# for epoch in range(epochs): 
#     # Feed psis in random order
#     xi, zeta = sklearn.utils.shuffle(xi, zeta)

#     global_loss = 0
#     for xi_mu, zeta_mu in zip(xi[:sample], zeta[:sample]):
#         res, loss = container(xi_mu, zeta_mu, True)
#         global_loss += loss
#     global_losses.append(global_loss/len(xi))


# plt.plot(range(len(global_losses)), global_losses, 'k-')


#######################
# NONE + STANDARDIZE ##
#######################


# # Create the perceptron container 
# container = Container(
#     "quadratic", 
#     DenseBiasLayer(1, activation="id", eta=eta), 
# )

# zeta, zeta_avg, zeta_std = standarizedf(zeta)
# print("STD", zeta_std)
# # Train the perceptron 
# global_losses = [] 
# for epoch in range(epochs): 

#     # Feed psis in random order
#     xi, zeta = sklearn.utils.shuffle(xi, zeta)

#     global_loss = 0
#     for xi_mu, zeta_mu in zip(xi[:sample], zeta[:sample]):
#         res, loss = container(xi_mu, zeta_mu, True)
#         global_loss += loss * (zeta_std[0]**2)
#     global_losses.append(global_loss/len(xi))


# plt.plot(range(len(global_losses)), global_losses, 'r-')
# zeta = destandarizedf(zeta, zeta_avg, zeta_std)


# #######################
# # NONE + SCALING     ##
# #######################



# Create the perceptron container 
container = Container(
    "quadratic", 
    DenseBiasLayer(1, activation="id", eta=eta), 
)

zeta, zeta_min, zeta_max = scaledf(zeta)
# Train the perceptron 
global_losses = [] 
for epoch in range(epochs): 

    # Feed psis in random order
    xi, zeta = sklearn.utils.shuffle(xi, zeta)

    global_loss = 0
    for xi_mu, zeta_mu in zip(xi[:sample], zeta[:sample]):
        res, loss = container(xi_mu, zeta_mu, True)
        global_loss += loss * ( (zeta_max[0]-zeta_min[0])**2)
    global_losses.append(global_loss/len(xi))


plt.plot(range(len(global_losses)), global_losses, 'g-')
zeta = descaledf(zeta, zeta_min, zeta_max)


#######################
# STANDARIZE + STANDARIZE ##
#######################

# # Create the perceptron container 
# container = Container(
#     "quadratic", 
#     DenseBiasLayer(1, activation="id", eta=eta), 
# )

# zeta, zeta_avg, zeta_std = standarizedf(zeta)
# xi, xi_avg, xi_std = standarizedf(xi)

# # Train the perceptron 
# global_losses = [] 
# for epoch in range(epochs): 

#     # Feed psis in random order
#     xi, zeta = sklearn.utils.shuffle(xi, zeta)

#     global_loss = 0
#     for xi_mu, zeta_mu in zip(xi[:sample], zeta[:sample]):
#         res, loss = container(xi_mu, zeta_mu, True)
#         global_loss += loss * (zeta_std[0]**2)
#     global_losses.append(global_loss/len(xi))


# plt.plot(range(len(global_losses)), global_losses, 'c-')
# zeta = destandarizedf(zeta, zeta_avg, zeta_std)
# xi = destandarizedf(xi, xi_avg, xi_std)

# #######################
# # SCALE + SCALE ##
# #######################

# Create the perceptron container 
container = Container(
    "quadratic", 
    DenseBiasLayer(1, activation="id", eta=eta), 
)

zeta, zeta_min, zeta_max = scaledf(zeta)
xi, xi_min, xi_max = scaledf(xi)


# Train the perceptron 
global_losses = [] 
for epoch in range(epochs): 

    # Feed psis in random order
    xi, zeta = sklearn.utils.shuffle(xi, zeta)

    global_loss = 0
    for xi_mu, zeta_mu in zip(xi[:sample], zeta[:sample]):
        res, loss = container(xi_mu, zeta_mu, True)
        global_loss += loss * ( (zeta_max[0] - zeta_min[0])**2 )
    print(global_loss/len(xi))
    global_losses.append(global_loss/len(xi))


plt.plot(range(len(global_losses)), global_losses, 'y-')
zeta = descaledf(zeta, zeta_min, zeta_max)
xi = descaledf(xi, xi_min, xi_max)

# plt.legend(["None - None", "None - Standardize", "Standardize - Standardize"])
plt.legend(["None - Scaling", "Scaling - Scaling"])
plt.show()
