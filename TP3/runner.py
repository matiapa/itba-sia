from container import * 
from grapher import * 

psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
zeta = [ [1], [-1], [-1], [-1] ] 

epochs = 15
stop_and_picture = 1

i = 0 
for epoch in range(epochs): 
    for psi_mu, zeta_mu in zip(psi, zeta): 
        res, loss = container(psi_mu, zeta_mu, True)
        graph_simple_perceptron(container, psi, zeta, int(i/stop_and_picture))
        print(res, loss)
        i += 1
    # if epoch % stop_and_picture == 0: 
        # print("COMPLETED: {0}%".format(epoch*100/epochs))
        
to_gif("TP3/out/simple_perceptron/", 35, "simple_perceptron")


# print(container.layers[0].w)

