from container import * 
from grapher import * 
import sklearn

container = Container(
    "quadratic", 
    DenseBiasLayer(1, activation="id"), 
)




psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
zeta = [ [1], [-1], [-1], [-1] ] 

epochs = 60
errors = [] 
i = 0 
for epoch in range(epochs): 
    print("epoch", epoch)

    # Feed psis in random order
    array1_shuffled, array2_shuffled = sklearn.utils.shuffle(psi, zeta)

    error = 0
    for psi_mu, zeta_mu in zip(psi, zeta):
        res, loss = container(psi_mu, zeta_mu, True)
        error += loss # Accumulates the error of an epoch 
        i += 1  

    graph_simple_perceptron(container, psi, zeta, epoch)  
 
    errors.append(error)
    if error == 0: 
        break 


plt.plot(range(len(errors)), errors, 'k-')
plt.show()
    
   
to_gif("TP3/out/simple_perceptron/", epochs, "simple_perceptron")
