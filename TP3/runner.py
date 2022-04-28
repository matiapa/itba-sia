from container import * 
from grapher import * 
import sklearn

container = Container(
    "quadratic", 
    DenseBiasLayer(1, activation="id", eta=0.01), 
)

# psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
# zeta = [ [-1], [1], [1], [-1] ]

psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
zeta = [ [1], [-1], [-1], [-1] ] 

errors = [] 
epochs = 20
i = 0 
for epoch in range(epochs): 
    print(f'Epoch {i}')

    # Feed psis in random order
    array1_shuffled, array2_shuffled = sklearn.utils.shuffle(psi, zeta)

    error = 0
    for psi_mu, zeta_mu in zip(psi, zeta):
        res, loss = container(psi_mu, zeta_mu, True)
        loss = (np.sign(res)- zeta_mu)**2   # Emulation of step activation function
        error += loss # Accumulates the error of an epoch 

    graph_simple_perceptron(container, psi, zeta, i) 
    i += 1
    
    errors.append(error)
    if error == 0:
        break 

plt.plot(range(len(errors)), errors, 'k-')
plt.show()

to_gif("out/simple_perceptron/", i, "simple_perceptron")