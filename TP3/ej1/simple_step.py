import sys
sys.path.append("..")

from container import * 
from grapher import * 
import sklearn

container = Container(
    "quadratic", 
<<<<<<< HEAD:TP3/ej_1_runner_simple_perceptron.py
    DenseBiasLayer(1, activation="id"), 
    DenseBiasLayer(4, activation="relu"), 
=======
    DenseBiasLayer(1, activation="id", eta=0.01), 
>>>>>>> dd6d1d5e6146ee48b7d319f83a12e1dfcb4ccffc:TP3/ej1/simple_step.py
)

# XOR Problem
# psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
# zeta = [ [-1], [1], [1], [-1] ]

# AND Problem
psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
zeta = [ [1], [-1], [-1], [-1] ] 

epochs = 10
errors = [] 
i = 0 
for epoch in range(epochs): 

    # Feed psis in random order
    array1_shuffled, array2_shuffled = sklearn.utils.shuffle(psi, zeta)

    error = 0
    for psi_mu, zeta_mu in zip(psi, zeta):
        res, _ = container(psi_mu, zeta_mu, True)
        loss = (np.sign(res) - zeta_mu)**2  # Emulation of step activation function
        error += loss # Accumulates the error of an epoch 
        i += 1  

    # graph_simple_perceptron(container, psi, zeta, i)  
 
    errors.append(error)
    if error == 0: 
        break

plt.plot(range(len(errors)), errors, 'k-')
plt.show()
    
# to_gif("out/simple_perceptron/", i, "simple_perceptron")