from ast import In
from main.selection.selection import Selection
from main.fitness import Fitness
from main.individual import Individual
from typing import List
import numpy as np 

# TODO
class TournamentSelection(Selection):

    def __init__(self, u: float): 
        if u < 0.5 or u>1: 
            raise BaseException('Bad argument')
        self.u = u 

    def compete(self, i1: Individual, i2: Individual, fitness: Fitness): 
        r = np.random.uniform(0, 1)
        if r < self.u: 
            return i1 if fitness.apply(i1) > fitness.apply(i2) else i2
        else:
            return i1 if fitness.apply(i1) < fitness.apply(i2) else i2


    """
    Selects individuals using Tournament Method
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        selex = [] 
        for x in range(len(individuals)/2): 
            pairs = np.random.choice(individuals, size=4, replace=False) # PREGUNTA: deberia ser con replace true? 
            semi1 = self.compete(pairs[0], pairs[1])
            semi2 = self.compete(pairs[2], pairs[3])
            winner = self.compete(semi1, semi2)
            selex.append(winner)
        return selex 




