from main.fitness import Fitness
from main.individual import Individual
from main.selection.selection import Selection
from typing import List
import numpy as np

class RouletteSelection(Selection):

    """
    Selects individuals based on their relative fitness
    """
    def apply(self, individuals: List[Individual], fitness: Fitness) -> List[Individual]:
        max = sum(fitness.apply(individual) for individual in individuals) 
        probabilities = [fitness.apply(individual) / max for individual in individuals]
        return np.random.choice(individuals, size=len(individuals)//2, replace=False, p=probabilities)
