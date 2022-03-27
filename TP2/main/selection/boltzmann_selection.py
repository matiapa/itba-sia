from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import List
import numpy as np 


class BoltzmannSelection(Selection):


    def __init__(self, tc: float, to: float, k: float): 
        self.tc = tc 
        self.to = to 
        self.k = k
        self.t = 0

    @property
    def temperature(self): 
        return self.tc+(self.to-self.tc)*np.exp(-self.k*self.t)


    """
    Selects individuals using Boltzmann Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        max = sum(np.exp(fitness.apply(individual)/self.temperature) for individual in individuals) 
        probabilities = [np.exp(fitness.apply(individual)/self.temperature) / max for individual in individuals]
        np_array = np.random.choice(individuals, size=len(individuals)//2, replace=False, p=probabilities)
        return list(np_array)