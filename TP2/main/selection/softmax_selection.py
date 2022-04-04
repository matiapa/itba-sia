from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import Set
import numpy as np 

class SoftmaxSelection(Selection):

    
    """
    Selects individuals based on their relative fitness
    """
    def apply(self, individuals: Set[Individual], fitness: Fitness) -> Set[Individual]:
        max = sum( np.exp(fitness.apply(individual)) for individual in individuals) 
        probabilities = [ np.exp(fitness.apply(individual)) / max for individual in individuals]
        np_array = np.random.choice(list(individuals), size=len(individuals)//2, replace=False, p=probabilities)
        return set(np_array)