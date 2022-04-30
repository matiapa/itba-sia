import sys
sys.path.append("..")

from container import * 
from grapher import * 
import sklearn

psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
zeta = [ [-1], [1], [1], [-1] ]

# First layer
# psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
# zeta = [ [1, 1, 0], [1, -1, 1], [-1, 1, 1], [-1, -1, 0] ]

# Second layer
# psi = [ [1, 1, 0], [1, -1, 1], [-1, 1, 1], [-1, -1, 0] ]
# zeta = [ [-1], [1], [1], [-1] ]

epochs = 100

container = Container(
    "quadratic", 
    DenseBiasLayer(3, activation="id", eta=0.01),
    DenseBiasLayer(1, activation="id", eta=0.01),
)

errors = [] 
i = 0

for epoch in range(epochs): 
    print("Epoch", epoch)

    # Feed psis in random order
    array1_shuffled, array2_shuffled = sklearn.utils.shuffle(psi, zeta)

    error = 0
    for psi_mu, zeta_mu in zip(psi, zeta):
        res, _ = container(psi_mu, zeta_mu, True)
        res = -1 if res[0] > 0 else 1
        error += (res-zeta_mu[0])**2
        
        # print(psi_mu)
        # print(res)
        # print(zeta_mu)
        # print('-------')

    # graph_simple_perceptron(container, psi, zeta, epoch)
    i += 1
 
    errors.append(error)
    if error == 0: 
        break 

plt.plot(range(len(errors)), errors, 'k-')
plt.show()
    
# to_gif("TP3/out/simple_perceptron/", epochs, "simple_perceptron")