from container import * 
from grapher import * 
import sklearn

psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
zeta = [ [1], [-1], [-1], [-1] ] 

epochs = 25
stop_and_picture = 1

i = 0 
for epoch in range(epochs): 

    # Feed psis in random order
    array1_shuffled, array2_shuffled = sklearn.utils.shuffle(psi, zeta)

    for psi_mu, zeta_mu in zip(psi, zeta): 
        res, loss = container(psi_mu, zeta_mu, True)
        graph_simple_perceptron(container, psi, zeta, int(i/stop_and_picture))
        print(res, loss)
        i += 1


        
# to_gif("TP3/out/simple_perceptron/", 35, "simple_perceptron")



