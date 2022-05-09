import sys
sys.path.append("..")

from container import * 
from grapher import * 
import sklearn

epochs = 100


def train(psi, zeta, plot_error):

    container = Container(
        "quadratic", 
        DenseBiasLayer(50, activation="id", eta=0.01),
        DenseBiasLayer(50, activation="sigmoid", eta=0.01),
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
            res, loss = container(psi_mu, zeta_mu, True)
            error += loss

            # Habilitar si se usa la opcion chanta
            # res = -1 if res[0] > 0 else 1
            # error += (res-zeta_mu[0])**2
            
            print('In', psi_mu)
            print('ExOut', zeta_mu)
            print('ReOut', res)
            print(' ')

        # graph_simple_perceptron(container, psi, zeta, epoch)
        i += 1
    
        errors.append(error)
        if error == 0: 
            break 

        print('-------------------')

    if plot_error:
        plt.plot(range(len(errors)), errors, 'k-')
        plt.yscale("log")
        plt.xlabel('Epoch')
        plt.ylabel('Error')
        plt.show()
    
    return container

if __name__ == "__main__":
    psi = [ [1, 1], [1, -1], [-1, 1], [-1, -1]]
    zeta = [ [-1], [1], [1], [-1] ]

    container = train(psi, zeta, True)
    # to_gif("../out/simple_perceptron/", epochs, "simple_perceptron")