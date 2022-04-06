from individual import BrachistochroneIndividual
from main.fitness import Fitness
import numpy as np 

class BrachistochroneFitness(Fitness): 

    def apply(self, individual: BrachistochroneIndividual) -> float:

        infinity = 0.1 # np.infty
        q_control_points = len(individual.genes)
        h = individual.h0 
        step = individual.step
        delta_thetas = individual.genes 


        theta = 0 
        g = 10
        v = 0 
        t = 0 
        for i in range(q_control_points+1):

            if i == q_control_points: 
                theta_last = -np.arctan(h/step)
                # v = v*np.cos(theta_last - theta)
                if np.abs(theta-theta_last) > 0.01: 
                    return infinity
                theta = theta_last
            else:
                theta += delta_thetas[i]
                # v = v*np.cos(delta_thetas[i])
            h += step*np.tan(theta)
            disc = v**2 - 2*g*step*np.tan(theta)

            if disc < 0: 
                return infinity
            else:
                
                t1 = (v + np.sqrt(disc))/(g*np.sin(theta))
                t2 = (v - np.sqrt(disc))/(g*np.sin(theta))
                
                tf = 0 
                if t1 < 0 and t2 < 0:
                    return infinity 
                elif t1 < 0 and t2 > 0:
                    tf = t2
                elif t1 > 0 and t2 < 0: 
                    tf = t1
                else: 
                    tf = t1 if t1<t2 else t2
                t += tf
                v -= tf*g*np.sin(theta)


        return 0.1+1/t

