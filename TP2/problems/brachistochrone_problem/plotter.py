from individual import BrachistochroneIndividual 
from matplotlib import pyplot as plt 
import numpy as np 


# def cicloid(step): 
#     xs = []
#     ys = [] 

#     for t in range(10000):
#         t = t/10000
#         xs.append() 


#     return [], []

def plot_individual(individual: BrachistochroneIndividual): 
    controls = [individual.h0]
    steps = [0]
    theta = 0
    for delta_theta in individual.genes: 
        theta += delta_theta
        controls.append(controls[-1]+np.tan(theta)*individual.step)
        steps.append(steps[-1]+individual.step)
    steps.append(steps[-1]+individual.h0)
    controls.append(individual.hf)
    
    plt.plot(steps, controls, '-')


    # plt.plot(steps, )




    plt.show()
