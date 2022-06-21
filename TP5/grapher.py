from matplotlib import pyplot as plt 
import matplotlib
from container import * 

def graph_simple_perceptron(container: Container, psi, zeta, i): 
    square_len = 2
    density = 0.2
    point_density = int(square_len / density)

    # Enforce limits in axis 
    plt.xlim([-square_len, square_len])
    plt.ylim([-square_len, square_len])

    black_patch = matplotlib.patches.Patch(color='black', label='-1')
    red_patch = matplotlib.patches.Patch(color='red', label='1')
    plt.legend(handles=[red_patch, black_patch], loc='upper left')

    for x in range(-square_len*point_density, square_len*point_density): 
        for y in range(-square_len*point_density, square_len*point_density): 
            res = container.consume([x/point_density, y/point_density])
            if res >= 0:
                plt.plot(x/point_density, y/point_density, 'k.', markersize=0.25)       

    for psi_mu, zeta_mu in zip(psi, zeta): 
        plt.plot(psi_mu[0], psi_mu[1], 'rx' if zeta_mu[0] == 1 else 'ko') 

    plt.savefig('{0}.png'.format(i))
    plt.cla() 