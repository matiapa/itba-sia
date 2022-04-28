from container import * 
from grapher import * 
import sklearn

container = Container(
    "quadratic", 
    DenseBiasLayer(1, activation="id", eta=0.01), 
)

psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
zeta = [ [-1], [1], [1], [-1] ] 

psi_prime = [ [1, x[0], x[1], x[0]*x[1], x[0]**2, x[1]**2] for x in psi ]


epochs = 50

for epoch in range(epochs): 

    # Feed psis in random order
    array1_shuffled, array2_shuffled = sklearn.utils.shuffle(psi, zeta)

    for psi_mu, zeta_mu in zip(psi_prime, zeta): 
        res, loss = container(psi_mu, zeta_mu, True)
        print(res, loss)
    
print(container.layers[0].w)
graph_polybasis_perceptron(container, psi, zeta, epoch)