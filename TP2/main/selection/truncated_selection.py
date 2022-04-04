from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import Set
import numpy as np 

# TODO
class TruncatedSelection(Selection):

    def __str__(self):
        return "Truncated" + ' (k = ' + str(self.k) + ')'

    def __init__(self, k: float): 
        self.k = k 


    """
    Selects individuals using Truncated Method
    """
    def apply(self, individuals: Set[Individual], fitness: Fitness) -> Set[Individual]:
        individuals = sorted(individuals, key=fitness.apply)
        np_array = np.random.choice(individuals[self.k:], size=len(individuals)//2, replace=False)
        return set(np_array)