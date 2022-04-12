from individual import BrachistochroneIndividual 
from matplotlib import pyplot as plt 
import numpy as np 


def cicloid(): 
    
    xs = [] 
    ys = [] 
    x = 0 
    while x<2*np.pi:
        xs.append(x-np.sin(x))
        ys.append(-1*(1-np.cos(x)))
        x += 0.1
    return xs, ys

def plot_individual(individual: BrachistochroneIndividual): 
    controls = [individual.h0]
    steps = [0]
    theta = 0
    for delta_theta in individual.genes: 
        theta += delta_theta
        controls.append(controls[-1]+np.tan(theta)*individual.step)
        steps.append(steps[-1]+individual.step)
    steps.append(steps[-1]+individual.step)
    controls.append(individual.hf)
    
    plt.plot(steps, controls, '-')

    h, h2 = cicloid()
    plt.plot(h, h2, 'r-')
    plt.show()
