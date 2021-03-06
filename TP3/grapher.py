from matplotlib import pyplot as plt
import matplotlib
from container import Container
import imageio
import numpy as np 

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

    plt.savefig('../out/simple_perceptron/{0}.png'.format(i))
    plt.cla() 

def graph_bound_perceptron(container: Container, psi, zeta, i): 
    square_len = 2
    density = 0.05
    point_density = int(square_len / density)

    # Enforce limits in axis 
    plt.xlim([-square_len, square_len])
    plt.ylim([-square_len, square_len])

    # Graph metadata 
    plt.title("XOR Problem - Step activation function")

    for x in range(-square_len*point_density, square_len*point_density): 
        for y in range(-square_len*point_density, square_len*point_density): 
            res = container.consume([x/point_density, y/point_density, 0])
            plt.plot(x/point_density, y/point_density, alpha=res[0], markersize=0.25)       

    for psi_mu, zeta_mu in zip(psi, zeta): 
        plt.plot(psi_mu[0], psi_mu[1], 'rx' if zeta_mu[0] >= 0.5 else 'ko') 

    plt.savefig('TP3/out/simple_perceptron/{0}.png'.format(i))
    plt.cla() 




def graph_polybasis_perceptron(container: Container, psi, zeta, i): 
    square_len = 2
    density = 0.05
    point_density = int(square_len / density)

    # Enforce limits in axis 
    plt.xlim([-square_len, square_len])
    plt.ylim([-square_len, square_len])

    black_patch = matplotlib.patches.Patch(color='black', label='-1')
    red_patch = matplotlib.patches.Patch(color='red', label='1')
    plt.legend(handles=[red_patch, black_patch], loc='upper left')

    for x in range(-square_len*point_density, square_len*point_density): 
        for y in range(-square_len*point_density, square_len*point_density): 
            t = [x/point_density, y/point_density]
            res = container.consume( [1, t[0], t[1], t[0]*t[1], t[0]**2, t[1]**2])
            if res >= 0:
                plt.plot(x/point_density, y/point_density, 'k.', markersize=0.25)       

    for psi_mu, zeta_mu in zip(psi, zeta): 
        plt.plot(psi_mu[0], psi_mu[1], 'rx' if zeta_mu[0] == 1 else 'ko') 

    plt.savefig('out/simple_perceptron/{0}.png'.format(i))
    plt.cla() 


def to_gif(path: str, qty: int, name: str):
    images = []
    for i in range(qty):
        images.append(imageio.imread(path+"{0}.png".format(i)))
    imageio.mimsave('../out/gifs/{0}.gif'.format(name), images, fps=4)


def graph_confusion_matrix(title, labels, matrix):
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap="YlGn")

    ax.set_xticks(np.arange(len(labels)), labels=labels)
    ax.set_yticks(np.arange(len(labels)), labels=labels)
    ax.set_title(title)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, round(matrix[i][j]), ha="center", va="center", color="r")
    
    fig.tight_layout()
    plt.show()