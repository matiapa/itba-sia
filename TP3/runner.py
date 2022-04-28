from container import * 
from grapher import * 
import sklearn

psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
zeta = [ [-1], [1], [1], [-1] ] 

container = Container(
    "quadratic", 
    DenseBiasLayer(3, activation="sigmoid"),   
    DenseBiasLayer(100, activation="relu"),  
    DenseNoBiasLayer(1, activation="id"), 
)


epochs = 100
errors = [] 
i = 0 
for epoch in range(epochs): 

    # Feed psis in random order
    array1_shuffled, array2_shuffled = sklearn.utils.shuffle(psi, zeta)

    error = 0
    for psi_mu, zeta_mu in zip(psi, zeta):
        res, loss = container(psi_mu, zeta_mu, True)
        loss = (np.sign(res)- zeta_mu)**2
        error += loss
        print("EXPECTED", zeta_mu, " GOT", res)
        # graph_simple_perceptron(container, psi, zeta, i)  
        i += 1   

    errors.append(error)
    if error == 0: 
        break 

graph_simple_perceptron(container, psi, zeta, i)  


plt.plot(range(len(errors)), errors, 'k.')
plt.show()
    
   
to_gif("TP3/out/simple_perceptron/", i, "simple_perceptron")



