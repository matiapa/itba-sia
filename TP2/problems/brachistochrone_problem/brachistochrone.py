import numpy as np 
from matplotlib import pyplot as plt
# from tokenize import Number
# from typing import Any, ClassVar, Generic, List
# from individual import *


# class Brachistochrone(Individual):

#     genes: List[float]


#     def __init__(self, genes: List[float]) -> None:
#         if genes is None:
#             genes = self._initialize_genes()

#         if len(genes) != self.genome_size():
#             raise RuntimeError("The amount of given genes differs from specified genome size")

#         self.genes = genes
#         self.start_height = 1
#         self.end_height = 0 
#         self.horizontal_length = 10
#         self.q_control_points = 25
#         self.step = self.horizontal_length / self.q_control_points 

#     """
#     Returns the amount of genes the individals that this kind of individual must have
#     """
#     @staticmethod
#     def genome_size() -> int:
#         return 25 

#     """
#     Creates a random gene set, method used for creating an initial population
#     """
#     def _initialize_genes(self):
#         self.genes = [ np.pi * x / 2 -  ( np.pi / 4) for x in  np.random.rand(23)]

#     @property
#     def control_points(self):
#         controls = [self.start_height]
#         steps = [0]
#         theta = 0
#         for delta_theta in self.genes: 
#             theta += delta_theta
#             controls.append(np.tan(theta)*self.step)
#             steps.append(steps[-1]+self.step) 



 

# class IndividualFactory():

#     def instantiate(self, genes: List[float]) -> Individual:
#         raise NotImplementedError

def plot_bch(): 
    plt.plot()

def fitness(delta_thetas, q_control_points, step, h0):
    theta = 0 
    g = 10
    v = 0 
    h = h0
    t = 0 
    for i in range(q_control_points+1):

        if i == q_control_points: 
            theta_last = -np.arctan(h/step)
            # v = v*np.cos(theta_last - theta)
            if np.abs(theta-theta_last) > 0.01: 
                return np.infty
            theta = theta_last
        else:
            theta += delta_thetas[i]
            # v = v*np.cos(delta_thetas[i])
        h += step*np.tan(theta)
        disc = v**2 - 2*g*step*np.tan(theta)

        if disc < 0: 
            return np.infty
        else:
            t1 = (v + np.sqrt(disc))/(g*np.sin(theta))
            t2 = (v - np.sqrt(disc))/(g*np.sin(theta))
            tf = 0 
            if t1 < 0: 
                tf = t2
            elif t2 < 0: 
                tf = t1 
            else: 
                tf = t1 if t1<t2 else t2
            t += tf
            v -= tf*g*np.sin(theta)

    return t
        


angle_limit = 0.001
start_height = 0
end_height = 0 
horizontal_length = 1
q_control_points = 100
step = horizontal_length / (q_control_points + 1)

best_fit = np.infty
best_genes = [] 
n = 1000000
for x in range(n):
    if x % 10000 == 0: 
        print(x/n) 
    genes = [ (2*np.pi/2) * x -  ( np.pi/2) for x in  np.random.rand(1)]+[ (2*angle_limit) * x -  ( angle_limit) for x in  np.random.rand(q_control_points-1)]
    controls = [start_height]
    steps = [0]
    theta = 0
    for delta_theta in genes: 
        theta += delta_theta
        controls.append(controls[-1]+np.tan(theta)*step)
        steps.append(steps[-1]+step)
    steps.append(steps[-1]+step)
    controls.append(end_height)
    fit = fitness(genes, q_control_points, step, start_height)

    if fit < best_fit:
        best_fit = fit 
        best_controls = controls 







# if ( best_fitness < fit): 
#     fit = best_fitness
#     best_controls = controls

# # print(steps, controls)
plt.plot(steps, best_controls, '-')
plt.show()