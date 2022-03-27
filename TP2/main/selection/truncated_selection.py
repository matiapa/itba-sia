from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import List
import numpy as np 

# TODO
class TruncatedSelection(Selection):


    def __init__(self, k: float): 
        self.k = k 


    """
    Selects individuals using Truncated Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        sorted(individuals, key=fitness.apply) # me quedan los peores primero, y los saco con el [self.k:]
        np.random.choice(individuals[self.k:], size=len(individuals)//2, replace=False) # Me da un poco de dudas 